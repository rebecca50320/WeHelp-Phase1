schedule = []

#紀錄已預約時間  
def record_booking(name,booking_time):
        for item in schedule:
            if item['name']== name:
                item["booked"].extend(i for i in booking_time)
                
def book(consultants, hour, duration, criteria):
    #生成consultants班表
    if len(schedule) >0:
        pass
    else:
        for i in range(len(consultants)):
            schedule.append({"name":consultants[i]["name"],"booked":[]})

    #計算想預約的時間
    booking_time = [hour]
    for i in range(duration-1):
        hour+=1
        booking_time.append(hour)
    
    #判斷誰有空
    available = []
    for i in range(len(schedule)):
        cnt = 0 #時間是否有重疊的dummy
        for time in booking_time:
            for item in schedule[i]['booked']:
                if item == time:
                    cnt = 1
                    break
                
        if cnt == 0:
            available.append(schedule[i]['name'])        
    
    if len(available) == 0:
        print("No Service")
    else:
        #依criteria選best_fit
        if criteria == "price":
            best_fit = min(consultants, key=lambda x: x['price'] if x['name'] in available else float('inf'))
            record_booking(best_fit['name'],booking_time)
            print(best_fit['name'])

        elif criteria == "rate":
            best_fit = max(consultants, key=lambda x: x['rate'] if x['name'] in available else float('-inf'))
            record_booking(best_fit['name'],booking_time)
            print(best_fit['name'])
       

consultants=[
{"name":"John", "rate":4.5, "price":1000}, 
{"name":"Bob", "rate":3, "price":1200}, 
{"name":"Jenny", "rate":3.8, "price":800}
]


book(consultants, 15, 1, "price") # Jenny 
book(consultants, 11, 2, "price") # Jenny 
book(consultants, 10, 2, "price") # John 
book(consultants, 20, 2, "rate") # John 
book(consultants, 11, 1, "rate") # Bob 
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John