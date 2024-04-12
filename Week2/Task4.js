function getNumber(index){
    let num;
    if (index%3 ===1){
        num = 4 + 7* Math.floor(index/3);
    }else if (index%3 ===2){
        num = 8 + 7* Math.floor(index/3);
    }else{
        num = 7* Math.floor(index/3)
    }
    console.log(num)
}



getNumber(1); // print 4 
getNumber(5); // print 15 
getNumber(10); // print 25 
getNumber(30); // print 70