let schedule = [];

//紀錄已預約時間
function recordBooking(name,bookingTime){
    for (let item of schedule) {
        if (item['name'] === name) {
            item["booked"].push(...bookingTime);
        }
    }
}

function book(consultants, hour, duration, criteria){
    //生成顧問班表
    if (schedule.length >0){
        //以生成則不用        
    }else{
        for (let i=0; i<consultants.length; i++){
            schedule.push({"name":consultants[i]["name"],"booked":[]});
        }
    }
    //計算想預約的時間
    const bookingTime = [hour];
    for (let i=0; i<(duration-1); i++){
        hour++;
        bookingTime.push(hour);
    }
    //判斷誰有空
    let available = [];
    for (let i=0; i< schedule.length; i++){
        let cnt = 0;
        for (item of bookingTime){
            if (schedule[i]["booked"].includes(item)){
                cnt = 1;
                break
            }
        }
        if (cnt ===0){
            available.push(schedule[i]["name"]);
        }     
    }

    //依criteria選best_fit
    if (available.length ===0){ //沒有人有空直接印no service 
        console.log("No Service");
    }else{
        //available篩選出有空的顧問進行比較
        let possibleList = consultants.filter(consultants => available.includes(consultants.name))
        
        if (criteria==="rate"){
            let maxRateName = possibleList.sort((a, b) => b.rate - a.rate)[0].name;
            console.log(maxRateName);
            recordBooking(maxRateName, bookingTime);
           
        }else if (criteria==="price"){
            let minPriceName = possibleList.sort((a, b) => a.price - b.price)[0].name;
            console.log(minPriceName);
            recordBooking(minPriceName, bookingTime);
            
        }
    }
}


const consultants=[
{"name":"John", "rate":4.5, "price":1000}, 
{"name":"Bob", "rate":3, "price":1200}, 
{"name":"Jenny", "rate":3.8, "price":800}
];

book(consultants, 15, 1, "price"); // Jenny 
book(consultants, 11, 2, "price"); // Jenny 
book(consultants, 10, 2, "price"); // John 
book(consultants, 20, 2, "rate"); // John 
book(consultants, 11, 1, "rate"); // Bob 
book(consultants, 11, 2, "rate"); // No Service 
book(consultants, 14, 3, "price"); // John


