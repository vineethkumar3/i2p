import json
import subprocess

import boto3
from bs4 import BeautifulSoup
from own_routerid import own_routerinfo
from helper_functions import functions
from datetime import datetime
class router_info:



    def read_html(self,filePath):

        with open(filePath, 'r', encoding='utf-8') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    def read_table(self,url):
        soup=functions().get_table_htmlfile(url)
        tables = soup.find(class_="tunneldisplay tunnels_client")
        router_id={}
        for i,row in enumerate(tables.find_all('tr'),1):

            table_key=f"table_{i}"
            new_json={table_key:[]}
            table_data=row.find_all('td')

            for data in table_data:
                other_router = data.find('span', class_='tunnel_peer')

                if other_router:
                    a_element=other_router.find('a')
                    if a_element and 'href' in a_element.attrs:
                        href_value = a_element['href'].split('netdb?r=')[1]
                        new_json[table_key].append(href_value)

                local_router = data.find('span',class_='tunnel_peer tunnel_local')

                if local_router:
                    object = own_routerinfo()
                    own_routerId = object.routerId()
                    new_json[table_key].append(own_routerId)

            router_id.update(new_json)
        print(router_id)
        return router_id


    def update_jsonfile(self,jsonFile,tableData):

        try:
            with open(jsonFile, 'r') as read_file:
                old_data = json.load(read_file)

        except json.decoder.JSONDecodeError:
            # Handle the case when the file is empty or contains invalid JSON
            old_data = {}
            print(f"The JSON file '{jsonFile}' is empty or contains invalid JSON.")
        except FileNotFoundError:
            # Handle the case when the file does not exist
            old_data = {}
            print(f"The JSON file '{jsonFile}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


        try:
            with open(jsonFile, 'w') as write_file:
                #  Create new key as router ID and its value is the router table data and
                #  add that to the old data. In this way each router will has the sepate key, value pair.
                object=own_routerinfo()
                own_routerId=object.routerId()
                new_data={own_routerId:tableData}
                old_data.update(new_data)
                json.dump(old_data, write_file, indent=2)
        except json.decoder.JSONDecodeError:
            # Handle the case when the file is empty or contains invalid JSON
            old_data = {}
            print(f"The JSON file '{jsonFile}' is empty or contains invalid JSON.")
        except FileNotFoundError:
            # Handle the case when the file does not exist
            old_data = {}
            print(f"The JSON file '{jsonFile}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def upload_to_S3(self):

        try:
            date=datetime.now().strftime("%Y-%m-%d")
            object = own_routerinfo()
            own_routerId = object.routerId()


            s3 = boto3.client('s3')

            bucket_name = 'i2p'
            file_path = '/home/ubuntu/script/data.json'
            s3_key = f'results/{date}/{own_routerId}/data.json'

            # Upload the file
            s3.upload_file(file_path, bucket_name, s3_key)

        except subprocess.CalledProcessError as e:
            print(f"An error occured : {e}")


if __name__=="__main__":

    object=router_info()
    tableData=object.read_table("http://127.0.0.1:7657/tunnels")
    #object.update_jsonfile("./data.json",tableData)
    helper_obj=functions()
    obj_own=own_routerinfo()
    id=obj_own.routerId()
    finalData={id:tableData}
    helper_obj.write_json_file(finalData,"data.json","/home/ubuntu/script/")
    object.upload_to_S3()
