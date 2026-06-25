import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

"可以添加一些描述，以便于更好的操作程序"
"更多想法：我是否可以选择特定文件后缀进行删除呢"

print("请输入文件夹的绝对位置：")
path=input().strip()
print("请输入你想要批量输入的前缀名：")
cinname=input().strip()
print("输入希望的文件后缀名，如果是全部所有后缀名的话就直接回车")
extname=input().strip()

folder_path=path
"目标路径"
pre_name=cinname
"统一命名 exp:序列号"

goalfoderpath=r"D:\test"
"写入路径"
count = 1
try:
    os.chdir(folder_path)
except:
    print("找不到文件夹！")
    sys.exit()

allfiles=os.listdir()
def search(filename):
    lst=filename.split(".")
    return lst

for filename in allfiles:
    if os.path.isfile(filename) and filename!="一键命名.py":
        try:
            if extname =="":
                "不符合的情况""os.path.isfile(filename)等价函数？"
                # root=search(filename)[0]
                ext=search(filename)[1]
                newname=f"{pre_name}{count}{"."}{ext}"
                os.rename(filename,newname)
                print(f"文件：{filename}——————修改为：{newname}")
                count+=1
            else:
                ext = search(filename)[1]
                newname = f"{pre_name}{count}{"."}{ext}"
                if extname==ext:
                    os.rename(filename,newname)
                    print(f"文件：{filename}——————修改为：{newname}")
                    count += 1
                else:
                    print(2)
                    continue
        except:
            print(f"文件{filename}修改失败！")
print("操作完成！")

a=input("按下任意键关闭")