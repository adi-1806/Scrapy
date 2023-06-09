import scrapy

class Chocolatespider(scrapy.Spider):
    name = 'Chocolate'
    allowed_domains = ['chocolate.co.uk']
    start_urls = ['https://www.chocolate.co.uk/collections/all']
    
    def parse(self, response):
        products =response.css('product-item')

        for product in products:

            yield{
                'name' : product.css('a.product-item-meta__title::text').get()
            }