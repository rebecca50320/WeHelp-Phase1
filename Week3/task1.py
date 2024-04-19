import urllib.request as req
import json

def open_file(file_url):
    with req.urlopen(file_url) as response:
        return json.load(response)

def get_spot(data):
    spot_list = data["data"]["results"]
    for spot in spot_list:
        dist = get_dist(spot["SERIAL_NO"], mrt_data["data"])
        img = get_imgURL(spot["filelist"])
        file.write(spot["stitle"]+"," + dist +","+ spot["longitude"]+ "," + spot["latitude"]+ ","+ img+"\n")

def get_dist(id,mrt_data): #用serial_no對應出景點的捷運站和其地址，回傳地址中的行政區
    for item in mrt_data:
        if item["SERIAL_NO"] == id:
            address = item["address"]
            return address[5:8]

def get_imgURL(urls): #切開filelist中的url, 回傳第一張
    splitted_urls = urls.split("https://")
    img_url = "https://" + splitted_urls[1]
    return img_url

def get_mrt(spot_list,mrt_list):
    #取得所有捷運站
    mrt_station = []
    for item in mrt_list:
        mrt_station.append(item["MRT"])
    mrt_station = list(set(mrt_station))
    #依照捷運站存所有景點
    mrt_spot = {}
    for station in mrt_station:
        mrt_spot[station] = []
        for item in mrt_list:
            if station == item["MRT"]:
                stitle = id2stitle(item["SERIAL_NO"])
                mrt_spot[station].append(stitle)
    return mrt_spot
        
def id2stitle(id): #serial no 換景點
    for item in spot_data["data"]["results"]:
        if item["SERIAL_NO"] == id:
            #print(item["stitle"])
            return item["stitle"]
   


### Main Code ###
src_1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
spot_data = open_file(src_1)
src_2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
mrt_data = open_file(src_2)

#Task 1-1
with open("spot.csv","w",encoding="utf-8") as file:
    get_spot(spot_data)

#Task 1-2
result = get_mrt(spot_data["data"]["results"],mrt_data["data"])
with open("mrt.csv","w",encoding="utf-8") as file:
    for key,value in result.items():
        file.write(key)
        for item in value:
            file.write(","+item)
        file.write("\n")
    




