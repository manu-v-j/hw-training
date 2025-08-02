import scrapy
import re 

class SpencerSpider(scrapy.Spider):
    name = "spencer"
    allowed_domains = ["www.marksandspencer.com"]
    start_urls = ["https://www.marksandspencer.com/l/men/mens-shirts#intid=gnav_men_core_clothing_shirts"]

    def parse(self, response):
        products = response.xpath("//div[@class='product-card_rootBox__BcM9P']")
        for product in products:
            product_url = product.xpath(".//a/@href").get()
            if product_url:
                full_url = 'https://www.marksandspencer.com' + product_url
                yield response.follow(full_url, callback=self.parse_product_page)

        next_page = response.xpath("//a[contains(@class,'pagination')]/@href").get()
        if next_page:
            full_next = 'https://www.marksandspencer.com' + next_page
            yield response.follow(full_next, callback=self.parse)

    def parse_product_page(self, response):
        aria_label = response.xpath("//div[contains(@class, 'star-rating_wrapper__')]/@aria-label").get()
        if aria_label:
            match=re.search(r'Average rating:\s*([0-9.]+)', aria_label)
            rating=float(match.group(1))
        raw_reviews=response.xpath("//span[contains(@class,'media-0_textSm__Q52Mz media-0_strong__aXigV')]/text()").get()
        reviews=re.search('d+',raw_reviews)
        if reviews:
            reviews=reviews.find()
        yield {
            "unique_id": response.xpath("//p[contains(@class,'media-0_textXs')]/text()[2]").get(),
            "brand":response.xpath("//p[contains(@class,'brand-title_title')]/text()").get(),
            "price":response.xpath("//div[contains(@class,'product-intro_priceWrappe')]/p/text()").get(),
            "promotional_description":response.xpath("//div[contains(@class,'product-intro_slot')][2]/h1/text()").get(),
            "currency":response.xpath("//div[contains(@class,'product-intro_priceWrappe')]/p/text()").get()[0],
            "breadcrumb":response.xpath("//ul[contains(@class,'breadcrumb_list')]/li/a/text()").getall(),
            "pdp_url":response.url,
            "product_description":response.xpath("//p[contains(@class,'media-0_textSm__Q52Mz')][2]/text()").get(),
            "color":response.xpath("//p[contains(@class,'selector-group_legend')]/span[2]/text()").get(),
            'rating':rating,
            

        }
