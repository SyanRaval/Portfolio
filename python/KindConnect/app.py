# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
from db import init_db, add_act, get_all_acts, get_act, vote_on_act

app = Flask(__name__)
init_db()                                   # create tables if they don't exist


@app.route("/")
def home():
    """Show the main page with a form + leaderboard."""
    acts = get_all_acts()
    return render_template("index.html", acts=acts)


@app.route("/submit", methods=["POST"])
def submit():
    """
    Expected JSON:
    {
        "entity": "Norway",               # person / corp / country / state
        "description": "Resettled 20k refugees",
        "impact": 95                      # 1-100 (how big was the help?)
    }
    """
    data = request.get_json()
    if not data or "entity" not in data or "impact" not in data:
        return jsonify({"error": "Missing fields"}), 400

    act_id = add_act(
        entity=data["entity"].strip(),
        description=data.get("description", "").strip(),
        impact=int(data["impact"])
    )
    return jsonify({"act_id": act_id, "message": "Act recorded"}), 201


# app.py  (replace the /vote route)

@app.route("/vote/<int:act_id>", methods=["POST"])
def vote(act_id):
    data = request.get_json()
    direction = data.get("direction")
    if direction not in ("up", "down"):
        return jsonify({"error": "direction must be 'up' or 'down'"}), 400

    updated_act = vote_on_act(act_id, direction == "up")
    if not updated_act:
        return jsonify({"error": "Act not found"}), 404

    return jsonify({
        "act_id": updated_act["id"],
        "upvotes": updated_act["upvotes"],
        "downvotes": updated_act["downvotes"],
        "net_votes": updated_act["net_votes"],
        "kind_score": updated_act["kind_score"]
    })


def calculate_kind_score(impact: int, net_votes: int) -> int:
    """
    KindScore = impact × (1 + net_votes / 10)
    Net votes = upvotes - downvotes  (never < 0)
    """
    net = max(net_votes, 0)
    return round(impact * (1 + net / 10.0))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
