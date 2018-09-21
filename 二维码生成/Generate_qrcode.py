import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import qrcode


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


def generateQrCode():
    str_content = qrContent.get().strip()
    if str_content:
        img = qrcode.make(str_content)
        img.show()
    else:
        tkinter.messagebox.showinfo("提示", "请输入内容后点击生成按钮")
    return


root = tk.Tk()
root.wm_title("简易二维码生成")
center_window(root, 400, 300)
root.resizable(width=False, height=False)
root.protocol('WM_DELETE_WINDOW', closeWindow)


tk.Label(root, text="输入需要生成的二维码内容：").grid(row=1, column=0)

qrContent = tk.Entry(root)
qrContent.grid(row=1, column=3)

btn_generate = tk.Button(root, text="生成", command=generateQrCode)
btn_generate.grid(row=3, column=0)

root.mainloop()
