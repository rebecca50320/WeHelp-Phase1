def find_and_print(messages, current_station):
    #建立station list
    station_lst = ["Songshan","Nanjing Shanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"]
    #轉換current station
    if current_station == "Xiaobitan":
        current = station_lst.index("Qizhang")
    else:
        current = station_lst.index(current_station)
    #轉換message成為[name,station,index]
    friend_location = []
    for key, value in messages.items():
        friend_location.append([key,value])
    
    #取出message裡的station關鍵字並加入station index後計算距離
    for friend in friend_location:
        #處理小碧潭，index同七張
        if "Xiaobitan" in friend[1]:
            friend[1] = friend[1].replace(friend[1],"Xiaobitan")
            friend.append(abs(current - station_lst.index("Qizhang"))+1)
        else:
            for station in station_lst:
                if station in friend[1]:
                    friend[1] = friend[1].replace(friend[1],station)
            friend.append(abs(current -station_lst.index(friend[1])))
             
    #找出距離最短的並回傳key(name)
    result_dict = {item[0]: [item[2]] for item in friend_location}
    print(result_dict)
    print(min(result_dict, key=result_dict.get))             

messages={
    "Leslie":"I'm at home near Xiaobitan station.", 
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian

