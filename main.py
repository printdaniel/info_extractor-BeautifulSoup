""" App extrae los títulos de los diarios"""
import requests
from bs4 import BeautifulSoup
URL_LA_NACION = 'https://www.lanacion.com.ar/'
URL_PAGINA = 'https://www.pagina12.com.ar/'
class ExtractTitulos:
    def __init__(self): 
        pass

    def Soup_extractor(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content,"html.parser")
        return soup


    def Nacion_titulos(self):
        soup = self.Soup_extractor(URL_LA_NACION)
        content_titulos = soup.find_all('h2',"com-title")
        for t in content_titulos:
            sub = t.find_all('a')
            print(sub[0].attrs.get('title'))

    def Pagina_titulos(self):
        #article-title
        #aref
        #element title
        soup = self.Soup_extractor(URL_PAGINA)
        content_titulos = soup.find_all('div','element title')
        for i in content_titulos:
            print(i.get_text())



if __name__ == '__main__':
    ln = ExtractTitulos()
    ln.Pagina_titulos()
    
    
