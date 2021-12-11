from task1 import task1data
import pprint
import json
from bs4 import BeautifulSoup
import requests
import os
import random
import time


def get_movie_list_details(movies):
    if os.path.exists("/home/vinaata/Desktop/vaishnavi_webscrapping/task5.json")==True:
        with open("/home/vinaata/Desktop/vaishnavi_webscrapping/task5.json","r") as file:
            data=file.read()
            list=json.loads(data)
        return list
    else:
        time_sleep=random.randint(1,3)
        j=0
        list=[]
        while j<len(movies):
            newurl=movies[j]["movie_urls"]
            if os.path.exists("/home/vinaata/Desktop/vaishnavi_webscrapping/"+newurl[33:]+".json")==True:
                with open ("/home/vinaata/Desktop/vaishnavi_webscrapping/"+newurl[33:]+".json","r") as file:
                    data=file.read()
                    dic=json.loads(data)
                list.append(dic)
            else:
                time.sleep(time_sleep)
                x=requests.get(newurl)
                soup=BeautifulSoup(x.text,"html.parser")
                main=soup.find("ul",class_="content-meta info")
                all=main.find_all("li",class_="meta-row clearfix")
                my_dict={}
                for i in all:
                    my_dict[i.find("div",class_="meta-label subtle").get_text().strip()]=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
                title=soup.find("h1")
                my_dict["name"]=title.text
                list.append(my_dict)
                j+=1
                # with open("/home/vinaata/Desktop/vaishnavi_webscrapping/"+newurl[33:]+".json","w")as f:
                #     json.dump(list,f,indent=4)
        with open("/home/vinaata/Desktop/vaishnavi_webscrapping/task5.json","w") as file:
            json.dump(list,file,indent=2)
        return list
# pprint.pprint(get_movie_list_details(task1data))

t5=get_movie_list_details(task1data)




