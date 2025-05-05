
from parsel import Selector
import json
all_data = []

def parser(pdp_content):
    selector = Selector(text=pdp_content)

    property_type = selector.xpath("//div[contains(@class,'page-title')]/h1/text()").get()
    price = selector.xpath("//ul[contains(@class,'item-price-wrap')]//span/strong/text()").get()
    property_id = selector.xpath("//ul[contains(@class,'flex-fill')]/li[@class='property-overview-item']/strong/text()").get()
    property_usage = selector.xpath("//ul[contains(@class,'flex-fill')][2]/li[@id='usage']//strong/text()").get()
    property_size = selector.xpath("//ul[contains(@class,'flex-fill')]//li[contains(text(), 'Property Size')]/preceding-sibling::li/strong/text()").get()
    built_status = selector.xpath("//ul[contains(@class,'flex-fill')]//li[contains(text(), 'Built-up status')]/preceding-sibling::li/strong/text()").get()
    bed_rooms = selector.xpath("//ul[contains(@class,'flex-fill')]//li[contains(text(),'Bedrooms')]/preceding-sibling::li/strong/text()").get()
    halls = selector.xpath("//ul[contains(@class,'flex-fill')]//li[contains(text(),'Hall')]/preceding-sibling::li/strong/text()").get()
    bathrooms = selector.xpath("//ul[contains(@class,'flex-fill')]//li[contains(text(),'Bathrooms')]/preceding-sibling::li/strong/text()").get()
    no_of_floors = selector.xpath("//ul[contains(@class,'flex-fill')]//li[contains(text(),'No. of Floors')]/preceding-sibling::li/strong/text()").get()
    no_of_roads = selector.xpath("//ul[contains(@class,'flex-fill')]//li[contains(text(),'No. of Roads')]/preceding-sibling::li/strong/text()").get()
    images=selector.xpath("//a[contains(@class,'houzez-trigger-popup-slider-js')]/img/@src").getall()

    data={
            "Type": property_type,
            "Price": price,
            "ID": property_id,
            "Usage": property_usage,
            "Size": property_size,
            "Status": built_status,
            "Bedrooms": bed_rooms,
            "Halls": halls,
            "Bathrooms": bathrooms,
            "Floors": no_of_floors,
            "Roads": no_of_roads,
            "Images": images
        }
    all_data.append(data)
    with open('output.json','w') as f:
        json.dump(all_data,f,indent=4)