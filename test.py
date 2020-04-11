# import requests
# import json


# data = {
#     "username": "chr",
#     "password": "chr",
# }


# res = requests.get("http://127.0.0.1:3000/api/v3/fk", params=data )
# print(res.text)

try :
    # 尝试以只读的二进制格式打开 record.ms
    file = open("record.ms","rb")
    # 如果打开成功有file返回值通过pickle.load反序列化，prev_run是序列化后的结果
    prev_run = pickle.load(file)
    # 打印下一结果
    print("Previous solution", prev_run)
    # 关闭打开的文件
    file.close()
# 如果程序抛出了FileNotFoundError异常进行捕获，打印  A new file is created
except FileNotFoundError :
    print("A new file is created")

# 向record.ms二进制写文件
file = open("record.ms","wb")
# 序列化file， 这个sol没有定义不知道是什么，这里写错了
pickle.dump(sol,file)
# 关闭文件
file.close()
