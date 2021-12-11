import json
import requests

from bs4 import BeautifulSoup
import os
def movie_details(url):
    id=url[33:]
    if os.path.exists("/home/vinaata/Desktop/vaishnavi_webscrapping/"+id+".json")==True:
                with open("/home/vinaata/Desktop/vaishnavi_webscrapping/"+id+".json","r") as movieDataFile:
                    data=movieDataFile.read()
                    final=json.loads(data)
    else:
                final={}
                LinkData=requests.get(url)
                soup=BeautifulSoup(LinkData.text,"html.parser")
                final["name"]=soup.find("h1").text
                main=soup.find("ul",class_="content-meta info")
                all=main.find_all("li",class_="meta-row clearfix")
                for i in all:
                    final[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.strip()
                with open("/home/vinaata/Desktop/vaishnavi_webscrapping/"+id+".json","w") as file:
                    json.dump(final,file,indent=2)
    return final
