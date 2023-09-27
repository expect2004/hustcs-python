import json

def Func():
    data = open("step2/2017.txt","r",encoding = "utf-8")

    obj = json.load(data)

    data.close()
    
    #********** Begin *********#
    for item in obj["infos"]:
        item["age"] += 1
    obj["infos"].append({"name": "叶良辰", "age": 17, "height": 1.87, "sex": "男性"})
    obj["count"] = 4
    #********** End **********#
    output = open("step2/2018.txt","w",encoding = "utf-8")
    json.dump(obj,output) #输出到文件
    output.close()
