import scrapy
from scrapy_selenium import SeleniumRequest


class ImgSpider(scrapy.Spider):
    name = 'img'

    def start_requests(self):
        #url = 'https://4kwallpapers.com/wallpaper/Winter'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'}
        
        for i in range(1, 7):
            url = f'https://4kwallpapers.com/wallpaper/Winter?page={i}'
            yield SeleniumRequest(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        raw_img = response.xpath('//p[@itemprop="associatedMedia"]/a/span/img/@src').getall()
        yield {
            'image_urls': raw_img
        }
