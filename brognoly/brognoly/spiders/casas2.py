import scrapy

def concatenate_list_data(list,char=''):
     result= ''
     for element in list:
         if element == list[-1]:
             result += str(element)
         else:
             result += str(element)+char
     return result


class CitacoesSpider(scrapy.Spider):
    name = "casas2"

    start_urls = [
        "https://www.brognoli.com.br/imovel/comprar-casa-36389/",
        "https://www.brognoli.com.br/imovel/comprar-casa-32042/",
    ]

    def parse(self, response):
        dados = response.css('li div::text').re('\S+')
        aux = []
        for i in range(0,len(dados),2):
            aux.append(dados[i] +' '+ dados[i+1])
        yield {
            "title": response.css('title::text').extract(),
            "house_information": aux,
            "adress": concatenate_list_data(response.css('div.PrevAddress::text').re('\S+'),'-'),
            "description": response.css('blockquote::text').extract(),
            "announce_ID": response.css('div.list-property-code span::text').extract(),
            "Price":concatenate_list_data(response.css('div.price::text').re('\w+|\$'))
        }
