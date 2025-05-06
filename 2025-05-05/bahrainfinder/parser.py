
from parsel import Selector


def parser(pdp_content):
    selector = Selector(text=pdp_content)

    property_type=selector.xpath("//div[@class='page-title']/h1/text()").get()
    price=selector.xpath("//div[@class='page-title']/ul/span/strong/text()").get()
    currency=selector.xpath("//div[@class='page-title']/ul/span/text()").get()
    currency=currency.replace('BHD.','BHD')
    property_id=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'BF ID')]/preceding-sibling::li/strong/text()").get()
    property_usage=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Property Usage')]/preceding-sibling::li/strong/text()").get()
    property_size=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Property Size')]/preceding-sibling::li/strong/text()").get()
    built_status=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Built-up status')]/preceding-sibling::li/strong/text()").get()
    bedrooms=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Bedrooms')]/preceding-sibling::li/strong/text()").get()
    halls=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Hall')]/preceding-sibling::li/strong/text()").get()
    bathrooms=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Bathrooms')]/preceding-sibling::li/strong/text()").get()
    furnish=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Furnish')]/preceding-sibling::li/strong/text()").get()
    garage=selector.xpath("//ul[contains(@class,'flex-fill')]/li[contains(text(),'Garage')]/preceding-sibling::li/strong/text()").get()
    images=selector.xpath("//a[contains(@class,'houzez-trigger-popup-slider-js')]/img/@src").getall()
    agent=selector.xpath("//p[@class='agent-name']/text()").get()
    agent_no=selector.xpath("//div[contains(@class,'clearfix')]/form/a/span[2]/text()").get()
    features=selector.xpath("//h2[text()='Features']/ancestor::div[@class='block-wrap-features']//ul/li/a/text()").getall()


    data={
        "Property_id":property_id,
        "Property_type":property_type,
        "Price":price,
        "Currency":currency,
        "Property_usage":property_usage,
        "Property_size":property_size,
        "Built_status":built_status,
        "Bedrooms":bedrooms,
        "Halls":halls,
        "Bathrooms":bathrooms,
        "Furnish":furnish,
        "Garage":garage,
        "Images":images,
        "Agent":agent,
        "Agent_no":agent_no,
        "Features":features

    }
    return data