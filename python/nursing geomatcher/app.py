from flask import Flask, render_template, jsonify
from flask_socketio import SocketIo, emit
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from sqlalchemy import func
from geopy.geocoders import Nominatim
import os
import subprocess # For triggering Scrapy locally; use Lambda in prod
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    company = db.Column(db.String(255))
    location = db.Column(db.String(255))
    salary = db.Column(db.String(100))
    geom = db.Column(Geometry('POINT', srid=4326)) # Lat/long point

    def to_geojson(self):
        return {
            "type" : "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [self.geom.x, self.geom.y] if self.geom else None
            },
            "properties": {
                "id": self.id,
                "title": self.title,
                "company": self.company,
                "location": self.location,
                "salary": self.salary
            }
        }

# Geocode function
def geocode_location(location):
    geolocator = Nominatim(user_agent=Config.USER_AGENT)
    try:
        loc = geolocator.geocode(location)
        if loc:
            return f'POINT({loc.longitude} {loc.latitude})'
    except:
        pass
    return None

# Route for frontend
@app.route('/')
def index():
    return render_template('index.html')

# API for jobs as GeoJSON
@app.route('/api/jobs')
def get_jobs():
    jobs = Job.query.all()
    features = [job.to_geojson() for job in jobs]
    return jsonify({"type": "FeatureCollection", "features": features})

# Trigger scrape (for dev; use AWS Lambda in prod)
@app.route('/scrape', methods=['POST'])
def trigger_scrape():
    # Run  scrapy spider
    subprocess.run(['scrapy', 'crawl', 'indeed_nursing', '-o', 'jobs.json'], cwd='scrapy_spider/nursing_jobs')

    # Load scraped JSON and insert to DB with geocoding
    if os.path.exists('scrapy_spider/nursing_jobs/jobs.json'):
        import json
        with open('scrapy_spider/nursing_jobs/jobs.json') as f:
            new_jobs = json.load(f)

        added = False
        for item in new_jobs:
            existing = Job.query.filter_by(title=item['title'], company=item['company']).first()
            if not existing:
                geom = geocode_location(item['location'])
                job = Job(title=item['title'], company=item['company'], location=item['location'], salary=item.get('salary'), geom=geom)
                db.session.add(job)
                added = True

        db.session.commit()

        if added:
            #Emit realtime update
            socketio.emit('new_jobs', {'message': 'New jobs added!'})

        os.remove('scrapy_spider/nursing_jobs/jobs.json')

    return {'status': 'done'}

@socketio.on('connect')
def handle_connect():
    emit('connected', {'data': 'Connected'})

if __name__ == '__main__':
    db.create_all() # Create tables if not exist
    socketio.run(app, debug=True)

