import requests
from bs4 import BeautifulSoup

title = str(input("enter your artical_name :")).replace(" ", "+")

link = "https://www.google.com/search?q=" + title + "wikipedia"

res = requests.get(link)
soup = BeautifulSoup(res.text , "html.parser")

for sp in soup.find_all("div"):
    try:
        link= sp.find("a").get("href")
        if ("en.wikipedia.org" in link):
            print(link)
            break
    except:
        pass
final_link = link[7 : ].split("&")[0]

res_2 = requests.get(final_link)

soup_2 = BeautifulSoup(res_2.text , "html.parser")

name = soup_2.find("h1").text
corpus_2 = ''
for sp_2 in soup_2.find_all("p"):
    corpus_2 += sp_2.text
    corpus_2 += "\n"

corpus_2 = corpus_2.strip()

for i in range(0 , 1000):
   corpus_2 = corpus_2.replace("["+str(i)+"]" , " ")
print(corpus_2)

# file = open(name +".txt" , "w")
# file.write(corpus_2)
# file.close()




    
 




# https://en.wikipedia.org/wiki/Mahatma_Gandhi

# link = "https://en.wikipedia.org/wiki/Mahatma_Gandhi"

# res = requests.get(link)
# soup = BeautifulSoup(res.text , "html.parser")

# artical_name = soup.find("h1").text
# print(artical_name)

# corpus = ''
# for p in soup.find_all("p"):
#     corpus += p.text
#     corpus += "\n"
    
# corpus = corpus.strip()
# print(corpus)

# file = open(artical_name + ".txt" , "w")
# file.write(corpus)
# file.close()

# https://www.google.com/search?q=mahatma+gandhi+wikipedia

# https://en.wikipedia.org/wiki/Mahatma_Gandhi

# https://en.wikipedia.org/wiki/Martin_Luther

# https://en.wikipedia.org/wiki/Abraham_Lincoln