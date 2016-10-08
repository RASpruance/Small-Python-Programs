import re
import os
from urllib.request import urlopen

url1 = 'https://rss.sciencedaily.com/top.xml' # Put your web page address here
url2 = 'http://www.news.com.au/national/rss'

# Read the contents of the web page as a character string
url=url1
web_url_open=urlopen(url)

web_page_contents_bytes = urlopen(url).read()
web_page_contents=web_page_contents_bytes .decode('UTF-8')
p1=re.compile(r'(?<=<item>)(.*?)(?=</item>)')
print(web_page_contents_bytes)
items=p1.findall(web_page_contents)
p1=re.compile(r'(?<=<title>)(.*?)(?=</title>)')
titles=p1.findall(web_page_contents)
p1=re.compile(r'(?<=<link>)(.*?)(?=</link>)')
links=p1.findall(web_page_contents)
p1=re.compile(r'(?<=<description>)(.*?)(?=</description>)')
descriptions=p1.findall(web_page_contents)
p1=re.compile(r'(?<=<media:thumbnail)(.*?)(?=/>)')
images=p1.findall(web_page_contents)
# Display the downloaded web page
#print (web_page_contents)
#print(items)
#print(titles)
#print(links)
#print(descriptions)
print(images)
aftersplit=web_page_contents.split('<item>')
print(aftersplit)
print(len(aftersplit))
features=[titles,links,descriptions,images]
for item in features:
    print(len(item))
TheNewsWithImages=[]
for i in images:
    for j in aftersplit:
        if j.find(i)!=-1 :
            TheNewsWithImages.append(j)
            break;

homedir = os.getcwd()
count=0
for item in TheNewsWithImages:
    p1 = re.compile(r'(?<=<title>)(.*?)(?=</title>)')
    titles = p1.findall(item)
    p1 = re.compile(r'(?<=<link>)(.*?)(?=</link>)')
    links = p1.findall(item)
    p1 = re.compile(r'(?<=<description>)(.*?)(?=</description>)')
    descriptions = p1.findall(item)
    p1 = re.compile(r'(?<=<media:thumbnail)(.*?)(?=/>)')
    str_head="<html><head><title>"+titles[0]+"</title><style>body{background-color:beige;}hr{border-style:solid;margin-top:2em;margin-bottom:2em}</style></head>"
    str_body_newspaper_title='<body><p align = "center"><span style = "font-size:50px; font-family:Times">'+titles[0] +'</span></p>'
    image_url=images[count]
    p1 = re.compile(r'(?<=url=")(.*?)(?=" height=)')
    image_url = p1.findall(image_url)
    str_body_image='<p align = "center"><img src ="' + image_url[0]+'"style="border:3px solid black"></p>'
    str_body_story='<p align = "center"><span style = "font-size:25px; font-family:Times">'+descriptions[0] +'</span></p>'
    str_body_source='<a href="'+links[0]+'"></a>'
    str_body_end='</body>'
    f=open(homedir+"\\test"+str(count)+".html",'w')
    f.write(str_head+str_body_newspaper_title+str_body_image+str_body_story+str_body_source+str_body_end)
    f.close()
    count=count+1


#print("length of the news with pictures"+str(len(TheNewsWithImages)))

#website_string = web_page_contents.decode('utf-8','ignore')
#f.write(web_page_contents)
#f.close()
