""" App extrae los títulos de los diarios"""
import requests
from bs4 import BeautifulSoup
URL_LA_NACION = 'https://www.lanacion.com.ar/'
URL_PAGINA = 'https://www.pagina12.com.ar/'
URL_INFOBAE = 'https://www.infobae.com/'
URL_TIEMPOARG = 'https://www.tiempoar.com.ar/informacion-general/'

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
        soup = self.Soup_extractor(URL_PAGINA)
        content_titulos = soup.find_all('div','element title')
        for i in content_titulos:
            print(i.get_text())

    def InfoBae_titulos(self):
        soup = self.Soup_extractor(URL_INFOBAE)
        content_titulos = soup.find_all('div','tcc_itm tcc_bc')
        for i in content_titulos:
            print(i.get_text())


    def Tiempo_titulos(self):
        soup = self.Soup_extractor(URL_TIEMPOARG)
        content_titulos = soup.find_all('div',attrs={'title'})
        try:
            for i in content_titulos:
                print(i.find('p').get_text())
        except AttributeError :
            print("\n")


    def Main(self):
        print("\n TITULOS LA NACION")
        self.Nacion_titulos()
        print("\n TITULOS LA PAGINA 12")
        self.Pagina_titulos() 
        print("\n TITULOS LA INFOBAE") 
        self.InfoBae_titulos()
        print("\n TITULOS LA TIEMPO ARGENTINO")
        self.Tiempo_titulos()


if __name__ == '__main__':
    ln = ExtractTitulos()
    ln.Main()
