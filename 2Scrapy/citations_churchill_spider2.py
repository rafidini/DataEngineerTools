import scrapy

class ChurchillQuotesSpider2(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//article'):
            text_value = cit.xpath('//div[@class="figsco__quote__text"]/a/text()').extract_first()
            author_value = cit.xpath('//div[@class="figsco__fake__col-9"]/a/text()').extract_first()
            if text_value is not None:
                text_value = text_value.replace(u"\u201C", "")
                text_value = text_value.replace(u"\u201D","")
            yield { 'text' : text_value,
                     'author' : author_value}
