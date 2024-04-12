function func(...data){
    //取出middle name
    let nameList = [];
    for (let item of data){
        nameList.push(item);
    }
    let wordList = [];
    for (let item of nameList){
        if (item.length <= 3){
            wordList.push(item[1]);
        }else if(3 < item.length <= 5){
            wordList.push(item[2]);
        }
    }
    //找uniq
    wordList.sort();
    let uniq = [];
    for (let i=0; i<wordList.length; i++){
        if (i ===0){
            if (wordList[i] != wordList[i+1]){
                uniq.push(wordList[i]);
            }
        }else if (i === wordList.length -1){
            if (wordList[i] != wordList[i-1]){
                uniq.push(wordList[i]);
            }
        }else{
            if (wordList[i-1] != wordList[i] && wordList[i] != wordList[i+1] ){
                uniq.push(wordList[i]);
            }
        }
    }
    //找全名
    if (uniq.length <1){
        console.log("沒有");
    }else{
        for (let name of nameList){
            if (name.includes(uniq[0])){
                console.log(name);
            }
        }
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安