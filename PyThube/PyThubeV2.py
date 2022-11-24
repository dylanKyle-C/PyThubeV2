from tkinter import *
from tkinter import Tk, ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from pytube import YouTube
import shutil
import os
# ===================================================


def selectDir():
    dirpth = filedialog.askdirectory()
    dir.config(text=dirpth)


def dload():
    # user selected path

    apth = os.path.expanduser(os.sep.join(
        ["~", "Downloads", "fromYT"]))
    vpth = os.path.expanduser(os.sep.join(
        ["~", "Downloads", "fromYT", "Videos"]))
    # get yt video link
    vlink = ytLink.get()
    try:
        yt = YouTube(vlink)
    except:
        stat.config(text="Download Error: Please check the URL.", fg="red")
    if format.get() == "---":
        stat.config(
            text="Error: Please Select a File Type/Format", fg="red")
# Download file Audio
    if format.get() == "Audio":
        dl = yt.streams.get_audio_only()

        out_file = dl.download(output_path=apth)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        ytTitle.config(text=yt.title)
        stat.config(text="Audio Downloaded", fg="green")
        shutil.move(dl, apth)

# Download file Video
    if format.get() == "Video":
        dl = yt.streams.get_by_resolution(resolution="720p")
        dl.download(vpth)
        stat.config(text="Video Downloaded", fg="green")
        shutil.move(dl, vpth)


# ================================================================
root = Tk()
root.geometry("600x270")
root.minsize(600, 320)
root.maxsize(600, 320)
root.title("PyThube")
root.iconbitmap("C:/Program Files/PyThube/favicon.ico")
root.configure(bg="#2C3639")

frmt = ["---", "Audio", "Video"]
f = StringVar()
f.set("---")

logo = Image.open(
    "C:/Program Files/PyThube/pythube-logo.png")
lresize = logo.resize((150, 100))
logor = ImageTk.PhotoImage(lresize)
logolable = Label(image=logor, background="#2C3639", )
logolable.place(relx=.5, y=30, anchor=CENTER)

ytTitle = Label(root, text="", font=('Arial 10'), bg="#2C3639", fg="white")
ytTitle.place(relx=.5, y=65, anchor=CENTER)

url = Label(root, text="URL: ", font=('Arial 12 bold'),
            bg="#2C3639", fg="white").place(x=20, y=90)

ytLink = Entry(root, bd=1, width=75)
ytLink.place(x=70, y=92)

type = Label(root, text="Select Type", font='Arial 12 bold',
             bg="#2C3639", fg="white").place(x=20, y=120)

format = ttk.Combobox(root, values=frmt, textvariable=f, width=6)
format.bind()
format.place(x=116, y=122)
format['state'] = 'readonly'

download = Button(root, text="Download", font='Arial 10 bold', padx=10, pady=6,
                  fg="white", bg="red", command=dload).place(relx=.5, y=250, anchor=CENTER)

stat = Label(root, text='', font=('Arial 14 bold'), bg="#2C3639")
stat.place(relx=.5, y=290, anchor=CENTER)

root.mainloop()
