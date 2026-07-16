import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

"可以添加一些描述，以便于更好的操作程序"
"更多想法：我是否可以选择特定文件后缀进行删除呢"

def search(filename):
    lst=filename.split(".")
    return lst

"---------------------------------------------"
class rename:
    def __init__(self):
        "设置自己的成员"
        self.foleder_path="一键命名.py"
        self.pre_name="一键命名.py"
        self.count = 1
    def Setrename(self):
        print("请输入文件夹的绝对位置：")
        path = input()
        self.folder_path=path
        print("请输入你想要批量输入的前缀名：")
        cinname = input()
        self.pre_name=cinname
        try:
            os.chdir(self.folder_path)
        except:
            print("找不到文件夹！")
            sys.exit()
        allfiles = os.listdir()
        for filename in allfiles:
            if os.path.isfile(filename) and filename != "一键命名.py":
                try:
                    "不符合的情况""os.path.isfile(filename)等价函数？"
                    # root=search(filename)[0]
                    ext = search(filename)[1]
                    newname = f"{self.pre_name}{self.count}.{ext}"
                    # os.rename(filename,newname)
                    print(f"文件：{filename}——————修改为：{newname}")
                    self.count += 1
                except:
                    print(f"文件{filename}修改失败！")
        print("操作完成！")
"----------------------------------------------"

if __name__=="__main__":
    obj=rename()
    obj.Setrename()
