import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from PyPDF2 import PdfFileWriter, PdfFileReader

global output
output = PdfFileWriter()

global pdf_file
pdf_file = None

global pdf_pages_len
pdf_pages_len = 0


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


def openpdf():
    global output
    global pdf_file
    global pdf_pages_len
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    pdf_file = PdfFileReader(open(filename, "rb"))
    pdf_pages_len = pdf_file.getNumPages()
    label_pdf_pages_len['text'] = "该文件总页数为：" + str(pdf_pages_len)
    return


def savepdf():
    global output
    global pdf_file
    global pdf_pages_len
    start = 0
    end = 0
    try:
        start = int(entry_start.get())
        end = int(entry_end.get())
    except:
        pass

    if not pdf_file:
        tkinter.messagebox.showinfo("提示", "请先打开PDF文件")
        return
    elif end <= start or end > pdf_pages_len or start > pdf_pages_len:
        tkinter.messagebox.showinfo("提示", "请输入正确的截取页码")
        return
    else:
        filename = filedialog.asksaveasfilename(
            initialdir="/", title="Select file", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        for i in range(start - 1, end - 1):
            output.addPage(pdf_file.getPage(i))

        outputStream = open(filename+'.pdf', "wb")
        output.write(outputStream)
        return


root = tk.Tk()
root.wm_title("PDF文件截取")
center_window(root, 400, 300)
root.resizable(width=False, height=False)
root.protocol('WM_DELETE_WINDOW', closeWindow)

btn_open = tk.Button(root, text="打开PDF文件", command=openpdf)
btn_open.grid(row=0, column=0)

label_pdf_pages_len = tk.Label(root, text="")
label_pdf_pages_len.grid(row=0, column=1)

tk.Label(root, text="输入需要截取的页码编号").grid(row=1, column=0)

entry_start = tk.Entry(root)
entry_start.grid(row=1, column=1)

tk.Label(root, text=" : ").grid(row=1, column=2)

entry_end = tk.Entry(root)
entry_end.grid(row=1, column=3)

btn_save = tk.Button(root, text="保存截取后的PDF文件", command=savepdf)
btn_save.grid(row=3, column=0)

root.mainloop()
