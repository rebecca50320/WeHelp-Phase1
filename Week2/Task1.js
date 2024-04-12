function findAndPrint(messages, currentStation){
    //建立station list
    const stationList = ["Songshan","Nanjing Shanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"];
    //轉換current station
    let current;
    if (currentStation === "Xiaobitan") {
        current = stationList.indexOf("Qizhang");
    } else {
        current = stationList.indexOf(currentStation);
    }
   
    //轉換message成為[name,station,index]
    let friendLocation = [];
    for (let key in messages) {
        friendLocation.push([key, messages[key]]);
    }

    //取出message裡的station關鍵字並加入station index後計算距離
    for (friend of friendLocation){
        if (friend[1].includes("Xiaobitan")){
            friend[1] = "Xiaobitan";
            friend.push(Math.abs(current - stationList.indexOf("Qizhang")) + 1);
        } else{
           for (station of stationList){
                if(friend[1].includes(station)){
                    friend[1] = station;
                }
           }
           friend.push(Math.abs(current - stationList.indexOf(friend[1])));
        }
    }
    console.log(friendLocation);
    //找出距離最短的並回傳name
    let min_index = 0;
    for (let i=0; i< friendLocation.length; i++){
        if (friendLocation[i][2] < friendLocation[min_index][2]){
            min_index = i;
        }
    }
    let ans = friendLocation[min_index][0];
    console.log(ans);
}


const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.", 
    "Copper":"I just saw a concert at Taipei Arena.", 
    "Leslie":"I'm at home near Xiaobitan station.", 
    "Vivian":"I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary 
findAndPrint(messages, "Songshan"); // print Copper 
findAndPrint(messages, "Qizhang"); // print Leslie 
findAndPrint(messages, "Ximen"); // print Bob 
findAndPrint(messages, "Xindian City Hall"); // print Vivian