def func(*data):
    #取出middle name
    name_list = []
    for item in data:
        name_list.append(item)
    word_list = []
    for item in name_list:
        if len(item)<= 3:
            word_list.append(item[1])
        elif 3< len(item) <=5:
            word_list.append(item[2])
    #找uniq
    word_list.sort()
    uniq = []
    for i in range(len(word_list)):
        if i == 0:
            if word_list[i] != word_list[i+1]:
                uniq.append(word_list[i])
        elif i == len(word_list)-1:
            if word_list[i] != word_list[i-1]:
                uniq.append(word_list[i])
        else:
            if word_list[i-1] != word_list[i] and word_list[i] != word_list[i+1]:
                uniq.append(word_list[i])  
    print(uniq)  
    #找全名
    if len(uniq) <1:
        print("沒有")
    else:
        for name in name_list:
            if uniq[0] in name:
                print(name)
        
            

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安