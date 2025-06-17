from ttkbootstrap import Style
import ttkbootstrap as ttkb
from tkinter import ttk
from tkinter import messagebox as msgbox
import yt_dlp

style = Style(theme='vapor')
window = style.master
window.title('Zap Youtube Download')
window.geometry('210x30')

url_input = ttkb.Entry(bootstyle='dark')
url_input.grid(column=1, row=0, sticky="")


def download():
    url = url_input.get()
    if url == ''.strip(' '):
        msgbox.showerror('Zap [Error]', 'Please input a video URL.')
    if not url.startswith('https://'):
        temp_url = 'https://' + url
        url = temp_url

    msgbox.showinfo('Zap [Information]', 'Please wait for the download to finish. There will be a popup when it is finished downloading.')
    try:
        yt_dlp.YoutubeDL().download([url])
    except Exception as e:
        msgbox.showerror('Zap [Error]', 'Error: ' + e)
    msgbox.showinfo('Zap [Information]', 'Successfully downloaded!')

ttkb.Button(window, text='Download', style='success.Outline.TButton', command=download).grid(column=0, row=0, sticky="")
window.mainloop()
