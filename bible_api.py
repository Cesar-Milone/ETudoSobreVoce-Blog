import requests
from bs4 import BeautifulSoup


class Bible:
    def __init__(self):
        self.versivulo = []
        self.salmo = []
        self.get_versivulo()

    def get_versivulo(self):
        response = requests.get(url="https://www.bibliaonline.com.br/")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        self.versiculo = soup.find_all(class_="jss39")
        self.salmo = soup.find_all(class_="jss29 jss43")

    def print_versivulo(self):
        i = 0
        for ver in self.versiculo:
            print(ver.text)
            print(self.salmo[i].text)
            i += 1

    def json(self):
        dictionary = {}
        i = 0
        for ver in self.versiculo:
            dictionary[ver.text] = self.salmo[i].text
        return dictionary
