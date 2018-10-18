import scrapy

#URL geral
#'https://www.brognoli.com.br/imoveis/?filtering=off&sort=newest&ini=1&search_type=16&search_category=445&gsearch_city=FLORIAN%C3%93POLIS&search_city=FLORIAN%C3%93POLIS&search_neighborhood%5B%5D='

class SpiderCitacoes(scrapy.Spider):
    """
    Classe para realização de crawler no site quotes.toscrape.com
    """
    # Definindo o nome do Spider
    name = "casas1"
    
    start_urls = ['https://www.brognoli.com.br/imovel/comprar-casa-36389/',
                  'https://www.brognoli.com.br/imovel/comprar-casa-32042/'
            ]
        
    def parse(self, resposta):
        pagina = resposta.url.split("/")[-2]
        nome_arquivo = f'Casa-{pagina}.html'
        with open(nome_arquivo, 'wb') as f:
            f.write(resposta.body)
        
        self.log(f'Arquivo salvo {nome_arquivo}')
