# Scrapy

This is a Web Scraping project.

In this project, Chocolate names from 'chocolate.co.uk' crawled and stored into json or csv files.

Extracted data is saved in mydata.csv and mydata.json files

To Execute code:
  1. Install Scrapy in your local system
  2. The execute following command: 'scrapy crawl Chocolate'
  3. To store data either into json or csv files execute following:
      'scrapy crawl Chocolate -O filename.json'
              or
      'scrapy crawl Chocolate -O filename.csv'
    
  Note: In the above commands, 'Chocolate' is name of the spider created.
