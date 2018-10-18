import scrapy

def concatenate_list_data(list,char=''):
     result= ''
     for element in list:
         if element == list[-1]:
             result += str(element)
         else:
             result += str(element)+char
     return result

#start_urls = response.css('a.btn-pc::attr(href)').extract()

class CitacoesSpider(scrapy.Spider):
    name = "casas3"

    start_urls = ['https://www.brognoli.com.br/imoveis/?filtering=off&sort=newest&ini=1&search_type=16&search_category=445&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B%5D=']

    #Step1
    def parse(self, response):
        for url in response.css('a.btn-pc::attr(href)').extract():
            print('\n Parse url:',url)
            yield scrapy.Request(response.urljoin(url), callback=self.parse_houseinfo)
            
    #Step2
    def parse_houseinfo(self, response):
        print('\n Parse_Houseinfo')
        dados = response.css('li div::text').re('\S+')
        aux = []
        for i in range(0,len(dados),2):
            aux.append(dados[i] +' '+ dados[i+1])
        yield {
            "title": response.css('title::text').extract(),
            "realty_info": aux,
            "realty_type":response.css("div.preview-show div.pull-left a::text").extract_first(),
            "adress": concatenate_list_data(response.css('div.PrevAddress::text').re('\S+'),'-'),
            "description": response.css('blockquote::text').extract(),
#            "announce_ID": response.css('div.list-property-code span::text').extract(),
            "announce_ID": response.css('div span.code::text').extract_first(),
            "Price":concatenate_list_data(response.css('div.price::text').re('\w+|\$')),
            "URL": response.url
        }
