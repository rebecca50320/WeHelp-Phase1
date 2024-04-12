function find(spaces, stat, n){
    //相乘找available
    let available = [];
    for (let i=0; i<spaces.length; i++ ){
        available.push(spaces[i]*stat[i]);
    }
    //best fit
    if (n > Math.max(...available)){
        console.log(-1);
    }else{
        while (n <= Math.max(...available)){
            if (available.includes(n)){
                console.log(available.indexOf(n));
                break
            }else{
                n++;
            }
        }
    }
}
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5 
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1 
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2