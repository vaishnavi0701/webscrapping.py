from bs4 import BeautifulSoup
import requests
import os.path
import json
import pprint
import re

def scrap_top_list():
    if os.path.exists("task1.json"):
        with open("task1.json","r") as file:
	        read=file.read()
	        data=json.loads(read)
        return(data)

    else:
        url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
        sample=requests.get(url)
        soup=BeautifulSoup(sample.text,"html.parser")
        div=soup.find("table",class_="table")
        main_div=div.find_all("tr")
        movie_ranks=[]
        movie_names=[]
        no_of_Reviews=[]
        movie_urls=[]
        movie_ratings=[]
        year_of_realease=[]


    
        for i in main_div[1:]:
            movie_rank = i.find("td", class_="bold").text
            movie_ranks.append(movie_rank)
            # print(main_div)
            # print(movie_ranks)
            movie_name = i.find("a", class_="unstyled articleLink").text.strip()
            # print(movie_name) 
            name=movie_name
            # print(name)
            movie_name=re.split('(\d+)',name)
            year_of_realease.append(movie_name[-2])
            # print(year_of_realease)

            names=movie_name[0]
            namename=names.replace("(","")
            movie_names.append(namename)
            # print(movie_names)
            
            movie_review= i.find("td",class_="right hidden-xs").get_text()
            no_of_Reviews.append(movie_review)
            # print(no_of_Reviews)

            movie_rating = i.find("span",class_="tMeterScore").get_text().strip()
            movie_ratings.append(movie_rating)
            # print(movie_rating)

            movie_link=i.find("a")['href']
            movie_urls.append("https://www.rottentomatoes.com"+movie_link)
            # print(movie_urls)

    
        Top_Movies=[]
        details={'rank':'','Rating':'','Name':'','year':"",'movie_Reviews':'',"movie_urls":""}
        for i in range(0,len(movie_ranks)):
            details['rank']=str(movie_ranks[i])
            details['Rating']=str(movie_ratings[i])
            details['Name']=str(movie_names[i])
            details['year']=str(year_of_realease[i])
            details['movie_Reviews']=str(no_of_Reviews[i])
            details["movie_urls"]=str(movie_urls[i])

            
            Top_Movies.append(details.copy())
        
        with open("task1.json","w")as file:
            data=json.dump(Top_Movies,file,indent=4)
        return Top_Movies     


# pprint.pprint(scrap_top_list())
task1data=scrap_top_list()






































































































































































































































































































































# from bs4 import BeautifulSoup
# import requests
# import json
# import pprint

# # def adventure_movie():
# #     adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
#     adventure_api=requests.get(adventure_url)
#     htmlcontent=adventure_api.content
#     soup=BeautifulSoup(htmlcontent,"html.parser")
#     table_tag=soup.find("table",class_="table")
#     tr=table_tag.find_all("tr")
#     top_movie=[]
#     serial_no=1
#     for i in tr():
#         movie_rank=i.find_all("td",class_="bold")
#         for j in movie_rank:
#             rank=j.get_text()
#         movie_rating=i.find_all("span",class_="tMeterScore")
#         for rate in  movie_rating:
#             rating=rate.get_text().strip()
#         movie_name=i.find_all("a",class_="unstyled articleLink")
#         for name in movie_name:
#             title=name.get_text().strip()
#             list=title.split()
#             year=list[-1][1:5]
#             year1=int(year)
#             name_lenght=len(list)-1
#             name=""
#             for l in range(name_lenght):
#                 name+=""
#                 name+=list[l]
#             movie_name=name
#         movie_reviews=i.find_all("td",class_="right hidden-xs")
#         for rev in movie_reviews:
#             reviews=rev.get_text()
#         url=i.find_all("a",class_="unstyled articleLink")
#         for i in url:
#             link=i["href"]
#             movie_link="https://www.rottentomatoes.com"+link
#             details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie_URL":"","year":""}
#             details["movie_rank"]=rank
#             details["movie_rating"]=rating
#             details["movie_name"]=movie_name
#             details["movie_reviews"]=reviews
#             details["movie URL"]=movie_link
#             details["year"]=year1
#             top_movie.append(details.copy())
#         details={'position':'',"name":'','year':'','rating':'','url':''}
#         with open("task1.json","w") as file:
#             json.dump(top_movie,file,indent=2)
#         return top_movie

# pprint.pprint(adventure_movie)

















# # import os.path
# # import json
# # print(("welcome to login signup"))
# # user=input("you wants to login or signup:")
# # file_exists=os.path.exists("text.json")
# # if user=="signup":
# #     user1=input("enter user name")
# #     pass1=input("enter password")
# #     pass2=input("enter your confirm password")
# #     if pass1==pass2:
# #         print("your password is confirmed")
# #         birth=input("enter birthdate")
# #         contactno=int(input("enter number"))
# #         gender=input("enter the gender f/m")
# #         hobbies=input("enter your hobbies")
# #         qualification=input("enter your qualification")
# #         dict={"username":user1,"pass2":pass2,"birth":birth,"contactno":contactno,"gender":gender,"hobbies":hobbies,"qualification":qualification}
# #         if file_exists==True:
# #             with open("text.json","r") as file:
# #                 f=file.read()
# #                 p=json.loads(f)
# #                 p.append(dict)
# #             with open("text.json","w") as d:
# #                 json.dump(p,d,indent=2)
# #         else:
# #             with open("text.json","w") as d:
# #                 json.dump([dict],d,indent=2)

# #     else:
# #         print("wrong password")
# # else:
# #     if user=="login":
# #         usr_name=input("enter the usr_name:-")
# #         if file_exists==True:
# #             password=input("enter usr password:-")
# #             with open("text.json","r")as file:
# #                 a=file.read()
# #                 d=json.loads(a)
# #                 for i in range(len(d)):
# #                     if d[i]["username"]==usr_name:
# #                         if d[i]["pass2"]==password:
# #                             print("login successful")
# #                         else:
# #                             print("wrong password")
# #                     elif i == len(d)-1 and d[i]["username"]!=usr_name:
# #                         print("Wrong ID")

# #         else:
# #             print("Wrong details")




