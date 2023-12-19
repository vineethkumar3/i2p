from bs4 import BeautifulSoup
import requests
import json
class functions:

    def read_html(self, filePath):
        with open(filePath, 'r', encoding='utf-8') as file:
          html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    def get_table_htmlfile(self, url):

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
            else:
                print(f"Error: {response.status_code}")
                soup = BeautifulSoup(response.text, 'html.parser')

        except requests.RequestException as e:
            print(f"Error making request: {e}")
        return soup

    def write_json_file(self,data,filename,path):
        with open(f"{path}/{filename}", 'w') as file:
            json.dump(data,file,indent=2)