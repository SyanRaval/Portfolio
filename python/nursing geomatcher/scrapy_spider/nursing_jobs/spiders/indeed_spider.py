import scrapy
from nursing_jobs.items import NursingJobsItem

class IndeedNursingSpider(scrapy.Spider):
    name = 'indeed_nursing'
    start_urls = ['https://www.indeed.com/jobs?q=nursing']  # Add &l= for location if needed
    custom_settings = {'ROBOTSTXT_OBEY': True, 'USER_AGENT': 'nursing_jobs_mvp/1.0'}

    def parse(self, response):
        # Select job cards
        for card in response.css('div.jobsearch-SerpJobCard'):
            item = NursingJobsItem()
            item['title'] = card.css('h2.jobTitle a span::text').get()
            item['company'] = card.css('span.companyName::text').get()
            item['location'] = card.css('div.companyLocation::text').get()  # Updated from .location
            item['salary'] = card.css('div.salary-snippet-container::text').get()  # Updated selector
            item['link'] = response.urljoin(card.css('h2.jobTitle a::attr(href)').get())
            yield item

        # Pagination (MVP: first page only; extend for more)
        # next_page = response.css('a[data-testid="pagination-page-next"]::attr(href)').get()
        # if next_page:
        #     yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
