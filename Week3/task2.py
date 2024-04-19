import urllib.request as req
from bs4 import BeautifulSoup

#抓ptt的網頁原始碼
def getData(url):
    root = open_page(url)
    #觀察html標籤指定抓取title, like, datetime
    title_div = root.find_all("div" ,class_="title") 
    for title in title_div:
        if title.a != None: #排除已刪除文章
            post_url = "https://www.ptt.cc"+ title.a["href"]
            date = get_datetime(post_url)
            like = count_like(post_url)
            file.write(title.a.string +"," + like +"," + date + "\n")
            
            
    #抓下一頁
    nextLink = root.find("a",string="‹ 上頁")
    return nextLink["href"] if nextLink else ""

def get_datetime(url):
    post_root = open_page(url)
    #取datetime
    container_div = post_root.find("div",class_="bbs-screen bbs-content")
    element = container_div.find_all("div",class_="article-metaline")
    if len(element)>=3:
        datetime = element[2].find("span",class_="article-meta-value")
        return datetime.string if datetime.string else ""
    else:
        return ""
    

def count_like(url):
    post_root = open_page(url)
    #計算推文＋噓文
    container_div = post_root.find("div",class_="bbs-screen bbs-content")
    push_div = container_div.find_all("div",class_="push")
    cnt = 0
    for push in push_div:
        if push.find("span",class_="hl push-tag") != None:
            like_str = str(push.find("span",class_="hl push-tag").string)
            if push.find("span",class_="hl push-tag").string == "推 ":
                cnt +=1
        elif push.find("span",class_="f1 hl push-tag") != None:
            dislike_str = str(push.find("span",class_="f1 hl push-tag").string)
            if push.find("span",class_="f1 hl push-tag").string == "噓":
                cnt +=1      
    return str(cnt)

def open_page(url):
    #建立request物件 附加request header的資訊模擬人類拜訪網站
    request = req.Request(url,headers={
        "Cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
    })
    #將爬到的資料存在data
    with req.urlopen(request) as reponse:
        data= reponse.read().decode("utf-8")    
    root = BeautifulSoup(data,"html.parser")
    return root


#主code
pageURL = "https://www.ptt.cc/bbs/Lottery/index.html"
with open("article.csv","w",encoding="utf-8") as file:
    cnt = 0
    while cnt <3:
        pageURL = "https://www.ptt.cc"+ getData(pageURL)
        cnt+=1
