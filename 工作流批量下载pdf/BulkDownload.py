import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import os
import codecs
import re
import webbrowser
import requests

global file_path
file_path = ''


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)


def closeWindow():
    ans = tkinter.messagebox.askokcancel('提示', '关闭此窗体?')
    if ans:
        root.destroy()
    else:
        return


def openDir():
    global file_path
    file_path = filedialog.askdirectory()
    return file_path



def downloadpdf():
    global file_path

    if not file_path:
        tkinter.messagebox.showinfo("提示", "请先打开文件夹")
        return
    elif str_cookie.get().strip() == '':
        tkinter.messagebox.showinfo("提示", "请输入cookie")
        return
    else:
        file_list = os.listdir(file_path)
        root_path = file_path
        for tmp in file_list:
            match_list_0 = []
            match_list_1 = []
            match_list_2 = []
            try:
                file_path = root_path + "/" +tmp
                for c in ('utf-8', 'gbk', 'gb2312', 'gb18030', 'utf-16'):
                    try:
                        with codecs.open(file_path, 'rb', c) as file_object:
                            content = file_object.read()
                            match_list_0 = re.findall("FileClass=(.*?)&", content)
                            match_list_1 = re.findall("key1=(.*?)&", content)
                            match_list_2 = re.findall("key2=(.*?)'", content)
                            break
                    except:
                        pass
                print("This Page include " + str(len(match_list_0)) + " file")
            except:
                pass
            for i in range(len(match_list_1)):
                str_file_info = "http://192.168.1.100/APPForm/src/DMS/DMSCA/DMSCA.aspx?FormType=Info&Status=Edit&Porwer=r&FileClass=" + \
                    match_list_0[i] + "&fileID=0&fileNo=1&key1=" + \
                    match_list_1[i] + "&key2=" + match_list_2[i]
                try:
                    r = requests.get(str_file_info, headers={"Cookie": str_cookie.get().strip()})
                    match_list = re.findall("InlineDownFile(.*?);", r.text)
                    arr = match_list[0].replace("'", "").replace(
                        "(", "").replace(")", "").split(',')
                    str_download = "http://192.168.1.100/APPForm/src/DMS/DMSCA/InlineOpenFile.aspx?key1=" + \
                        arr[0] + "&key2=" + arr[1] + "&key3=" + arr[2]
                    print(str_download)
                    ie = webbrowser.get(webbrowser.iexplore)
                    ie.open(str_download, new=0)
                except:
                    print("Download Fialed...")
        return


root = tk.Tk()
root.wm_title("PDF文件截取")
center_window(root, 400, 300)
root.resizable(width=False, height=False)
root.protocol('WM_DELETE_WINDOW', closeWindow)

btn_open = tk.Button(root, text="打开源文件所在文件夹", command=openDir)
btn_open.grid(row=0, column=0)

tk.Label(root, text="输入Cookie").grid(row=1, column=0)

str_cookie = tk.Entry(root)
str_cookie.grid(row=1, column=1)

btn_save = tk.Button(root, text="下载PDF文件", command=downloadpdf)
btn_save.grid(row=2, column=0)

root.mainloop()
