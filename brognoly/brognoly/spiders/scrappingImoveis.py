import scrapy
import requests

# In[]: Function used to get the adress information with Google API Geocode
def getAdress(address,GoogleKey):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" +
                     address + "&key=" + GoogleKey)
    return r.json()

# In[]: Function used to build the adress retrieved from scrapping WebSites
def concatenate_list_data(list,char=''):
     result= ''
     for element in list:
         if element == list[-1]:
             result += str(element)
         else:
             result += str(element)+char
     return [result]
 
# In[]: Function used to organize information about Houses/Apartments retrieved from scrapping WebSites
def vec_concat(vector): #This function concatenates some strings together
    aux = []
    for i in range(0,len(vector),2):
        aux.append(vector[i] +' '+ vector[i+1])
    return aux

# In[]: Spider Body
#start_urls = response.css('a.btn-pc::attr(href)').extract()
all_urls = []
class CitacoesSpider(scrapy.Spider):
    name = "scrappingImoveis"

# In[]: Starting URLs | Sales
    URL_Apartments = 'https://www.brognoli.com.br/imoveis/page/1/?filtering=off&sort=newest&ini=1&search_type=16&search_category=444&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B0%5D'
    URL_Houses = 'https://www.brognoli.com.br/imoveis/page/1/?filtering=off&sort=newest&ini=1&search_type=16&search_category=445&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B0%5D'
    URL_Everything = 'https://www.brognoli.com.br/imoveis/page/1/?filtering=off&sort=newest&ini=1&search_type=16&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B0%5D'
    
# In[]: Starting URLs | Rents
#    URL_Apartments = 'https://www.brognoli.com.br/imoveis/page/1/?filtering=off&sort=newest&ini=1&search_type=16&search_category=444&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B0%5D'
#    URL_Houses = 'https://www.brognoli.com.br/imoveis/page/1/?filtering=off&sort=newest&ini=1&search_type=16&search_category=445&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B0%5D'
    URL_Everything_Rent = 'https://www.brognoli.com.br/imoveis/page/1/?filtering=off&sort=newest&ini=1&search_type=3&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B0%5D'
    
    start_urls = [URL_Everything_Rent]

    #Step1 - In this step we will search for all URL's of houses in all pages
    def parse(self, response):
        global all_urls
        if len(response.css('a.btn-pc::attr(href)').extract())>0: #Se houver algum link de casa nessa pagina
            urls = response.css('a.btn-pc::attr(href)').extract()
            all_urls =  all_urls + urls
            next_page = response.css('div.navigation a::attr(href)').extract_first()
            print('The Next Page is not None, URL is:',next_page)
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
        else:
            print('The Next Page is None! Parse Finalized!')
            for url in all_urls:
                yield scrapy.Request(response.urljoin(url), callback=self.parse_houseinfo)
                
    #Step2 - Retreive information from each of the houses URL links
    def parse_houseinfo(self, response):
        
        data = response.css('li div::text').re('\S+')
        realty_info = vec_concat(data)
        
        realty_type = response.css("div.preview-show div.pull-left a::text").extract_first()
        
        neighborhood = concatenate_list_data(response.css('div.PrevAddress::text').re('\S+'),'-') #Adress part from Scrapy URL
        
        street = response.css('div.PrevAddress span::text').re('\S+')#Adress part from Scrapy URL
        
        address = street + neighborhood #Adress combination from other parts
        
        UserKey = 'AIzaSyCXqBCa5QqZ3QwJESDYS4ldIewnUnHcfEU'
        google_request = getAdress(concatenate_list_data(address,'-')[0],UserKey) #Google API Geocode Request
        lat = google_request.get('results')[0]['geometry']['location']['lat'] #latitude from adress
        lng = google_request.get('results')[0]['geometry']['location']['lng'] #longitude from adress
        
        description = response.css('blockquote::text').extract()
        
        announce_ID = response.css('div span.code::text').extract_first()
        
        Price = concatenate_list_data(response.css('div.price::text').re('\w+|\$'))
        
        yield {
            "title": response.css('title::text').extract(),
            "realty_info": realty_info,
            "realty_type":realty_type,
            "neighborhood": neighborhood,
            "street": street,
            "address": address,
            "description": description,
            "latitude": lat,
            "longitude": lng,
            "announce_ID": announce_ID,
            "Price":Price,
            "URL": response.url
        }