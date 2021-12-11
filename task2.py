from task1 import scrap_top_list
import json
import pprint

data=scrap_top_list()

def group_by_year(data):
    movies=[]

    for i in data:
        year=i["year"]
        # print(i)
        # print(year)
        if year not in movies:
            movies.append(year)
            # print(movies)

    movie_dict={}
    for j in movies:
        movie_list=[]
        for k in data:
            # movie_list=[]
            if k["year"]==j:
                movie_list.append(k)
        movie_dict.update({j:movie_list})
        pprint.pprint(movie_dict)
    return movie_dict
    

d=group_by_year(data)

f=open('task2.json', 'w')
f.write(json.dumps(d,indent=4))
f.close()





































































































# from task1 import adventure_movie
# import json
# #from pprint import pprint
# data=adventure_movie()
# # def realeas_yr():
#     # years=[]
# def scrape_top_list(movie):
#     years=[]
#     for i in movie:
#         year=i["year"]
#         if year not in years:
#         # for j in i:
#         #     if i['year'] not in year:
#             years.append(year)
#     # year=sorted(year)
#     movie_dict={i:[] for i in years}
#     for i in movie:
#         year=i['year']
#         for x in movie_dict:
#             if str(x)==str(year):
#                 movie_dict[x].append(i)
#         # with open("movie_name.json","w")as h:
#         #     json.dump(movie_dict,h,indent=4)
#     return movie_dict
# d=scrape_top_list(data)
# # d=realeas_yr()
# f=open('task2.json', 'w')
# f.write(json.dumps(d,indent=4))
# f.close()
# # pprint.pprint(realeas_yr)