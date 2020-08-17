from tkinter.ttk import *
import tkinter as tk
import pafy 
import vlc 
import time
import os
from tkinter import messagebox

win = tk.Tk()
win.resizable(False, False) 
win.title("YouTube Streamer")
win.geometry('665x360')

Instance = vlc.Instance() 
player = Instance.media_player_new()
if not os.path.exists('downloads'):
        os.makedirs('downloads')  
folder = 'downloads' 
directory = os.getcwd() 
SAVE_PATH = os.path.join(directory, folder)

try:
    try:
        def Search():
             url = txt.get() 
             video = pafy.new(url)
             best_quality_video = video.getbestvideo()
             value = video.length
             ty_res = time.gmtime(value) 
             res = time.strftime("%H:%M:%S",ty_res)
             lbl = Label(win, text=res)
             lbl.grid(column = 1, row = 2, sticky = 'w', padx = 7, pady = 3)
             title = video.title
             lbl = Label(win, text=title)
             lbl.grid(column = 1, row = 3, sticky = 'w', padx = 7, pady = 3)
             author = video.author
             lbl = Label(win, text=author)
             lbl.grid(column = 1, row = 4, sticky = 'w', padx = 7, pady = 3)
             category = video.category
             lbl = Label(win, text=category)
             lbl.grid(column = 1, row = 5, sticky = 'w', padx = 7, pady = 3)
             best = video.getbest() 
             res = best.resolution
             lbl = Label(win, text=res)
             lbl.grid(column = 1, row = 6 , sticky = 'w', padx = 7, pady = 3)
             url = txt.get() 
             video = pafy.new(url)
             best_quality_video = video.getbestvideo()
             siz = (str((best_quality_video.get_filesize()) / 1024000) + "  MB" )
             lbl = Label(win, text=siz)
             lbl.grid(column = 1, row = 8, sticky = 'w', padx = 7, pady = 3)
             url = txt.get() 
             audio = pafy.new(url)
             best_quality_audio = audio.getbestaudio()
             siz = (str((best_quality_audio.get_filesize()) / 1024000) + "  MB" )
             lbl = Label(win, text=siz)
             lbl.grid(column = 1, row = 7, sticky = 'w', padx = 7, pady = 3)
    except EXCEPTION as e :
        messagebox.showerror("showerror", "the link was wrong") 
        
     
    def streamvideo():
    
        url = txt.get() 
        video = pafy.new(url)
        best_quality_video = video.getbestvideo()
        siz = (str((best_quality_video.get_filesize()) / 1024000) + "  MB" )
        lbl = Label(win, text=siz)
        lbl.grid(column = 1, row = 8, sticky = 'w', padx = 7, pady = 3)
        value = video.length
        ty_res = time.gmtime(value) 
        res = time.strftime("%H:%M:%S",ty_res)
        lbl = Label(win, text=res)
        lbl.grid(column = 1, row = 2, sticky = 'w', padx = 7, pady = 3)
        title = video.title
        lbl = Label(win, text=title)
        lbl.grid(column = 1, row = 3, sticky = 'w', padx = 7, pady = 3)
        author = video.author
        lbl = Label(win, text=author)
        lbl.grid(column = 1, row = 4, sticky = 'w', padx = 7, pady = 3)
        category = video.category
        lbl = Label(win, text=category)
        lbl.grid(column = 1, row = 5, sticky = 'w', padx = 7, pady = 3)
        best = video.getbest() 
        res = best.resolution
        lbl = Label(win, text=res)
        lbl.grid(column = 1, row = 6 , sticky = 'w', padx = 7, pady = 3)
        playurl = best.url 
        Media = Instance.media_new(playurl) 
        Media.get_mrl() 
        player.set_media(Media) 
        player.play()
    def streamaudio():
    
        url = txt.get() 
        audio = pafy.new(url)
        best_quality_audio = audio.getbestaudio()
        siz = (str((best_quality_audio.get_filesize()) / 1024000) + "  MB" )
        lbl = Label(win, text=siz)
        lbl.grid(column = 1, row = 7, sticky = 'w', padx = 7, pady = 3)
        value = audio.length
        ty_res = time.gmtime(value) 
        res = time.strftime("%H:%M:%S",ty_res)
        lbl = Label(win, text=res)
        lbl.grid(column = 1, row = 2, sticky = 'w', padx = 7, pady = 3)
        title = audio.title
        lbl = Label(win, text=title)
        lbl.grid(column = 1, row = 3, sticky = 'w', padx = 7, pady = 3)
        best = audio.getbestaudio() 
        author = audio.author
        lbl = Label(win, text=author)
        lbl.grid(column = 1, row = 4, sticky = 'w', padx = 7, pady = 3)
        category = audio.category
        lbl = Label(win, text=category)
        lbl.grid(column = 1, row = 5, sticky = 'w', padx = 7, pady = 3)
        bitrate = best.bitrate
        lbl = Label(win, text=bitrate)
        lbl.grid(column = 1, row = 6, sticky = 'w', padx = 7, pady = 3)
        playurl = best.url 
        Media = Instance.media_new(playurl) 
        Media.get_mrl() 
        player.set_media(Media) 
        player.play() 
    def audio_download():
        messagebox.showinfo("Please Wait ...", "download in progress...") 
        url = txt.get()
        audio = pafy.new(url)
        value = audio.length
        ty_res = time.gmtime(value) 
        res = time.strftime("%H:%M:%S",ty_res)
        lbl = Label(win, text=res)
        lbl.grid(column = 1, row = 2, sticky = 'w', padx = 7, pady = 3)
        title = audio.title
        lbl = Label(win, text=title)
        lbl.grid(column = 1, row = 3, sticky = 'w', padx = 7, pady = 3)
        best = audio.getbestaudio() 
        author = audio.author
        lbl = Label(win, text=author)
        lbl.grid(column = 1, row = 4, sticky = 'w', padx = 7, pady = 3)
        category = audio.category
        lbl = Label(win, text=category)
        lbl.grid(column = 1, row = 5, sticky = 'w', padx = 7, pady = 3)
        bitrate = best.bitrate
        lbl = Label(win, text=bitrate)
        lbl.grid(column = 1, row = 6, sticky = 'w', padx = 7, pady = 3)
        best_quality_audio = audio.getbestaudio()
        siz = (str((best_quality_audio.get_filesize()) / 1024000) + "  MB" )
        lbl = Label(win, text=siz)
        lbl.grid(column = 1, row = 7, sticky = 'w', padx = 7, pady = 3)
        best_quality_audio.download(SAVE_PATH)
        os.startfile("downloads")
    def video_download():
   
        messagebox.showinfo("Please Wait ...", "download in progress...") 
        url = txt.get()
        video = pafy.new(url)
        value = video.length
        ty_res = time.gmtime(value) 
        res = time.strftime("%H:%M:%S",ty_res)
        lbl = Label(win, text=res)
        lbl.grid(column = 1, row = 2, sticky = 'w', padx = 7, pady = 3)
        title = video.title
        lbl = Label(win, text=title)
        lbl.grid(column = 1, row = 3, sticky = 'w', padx = 7, pady = 3)
        author = video.author
        lbl = Label(win, text=author)
        lbl.grid(column = 1, row = 4, sticky = 'w', padx = 7, pady = 3)
        category = video.category
        lbl = Label(win, text=category)
        lbl.grid(column = 1, row = 5, sticky = 'w', padx = 7, pady = 3)
        best = video.getbest() 
        res = best.resolution
        lbl = Label(win, text=res)
        lbl.grid(column = 1, row = 6 , sticky = 'w', padx = 7, pady = 3)
        best_quality_video = video.getbestvideo()
        siz = (str((best_quality_video.get_filesize()) / 1024000) + "  MB" )
        lbl = Label(win, text=siz)
        lbl.grid(column = 1, row = 8, sticky = 'w', padx = 7, pady = 3)
        best_quality_video.download(SAVE_PATH)
        os.startfile("downloads")
    def play():
        player.play()
    def pause():
        player.pause() 
    def stop():
        player.stop()  
    

    
    lbl = Label(win, text = "Enter Link :")
    lbl.grid(column = 0, row = 0 , sticky = 'w', padx= 7, pady = 3)
    
    btn = Button(win, text="Search", command = Search)
    btn.grid(column = 2, row = 0, sticky = 'w', padx = 7, pady = 10)
    
        
    
    btn = Button(win, text="stream video", command = streamvideo)
    btn.grid(column = 2, row = 1, sticky = 'w', padx = 7, pady = 10)
    #Add Entry
    btn = Button(win, text="stream audio", command = streamaudio)
    btn.grid(column = 3, row = 1, sticky = 'w', padx = 7, pady = 10)
    txt = Entry(win, width=50)
    txt.grid(column = 1, row = 0, sticky = 'w', padx = 7 , pady = 10)
    btn = Button(win, text="stop streaming", command = stop)
    btn.grid(column = 1, row = 1, sticky = 'w', padx = 7 , pady = 3)
    
    btn = Button(win, text="pause", command = pause)
    btn.grid(column = 2, row = 2, sticky = 'w', padx = 7 , pady = 3)
    
    btn = Button(win, text="play", command = play)
    btn.grid(column = 3, row = 2, sticky = 'w', padx = 7 , pady = 3)
    
    lbl = Label(win, text = "duration :")
    lbl.grid(column = 0, row = 2 , sticky = 'w', padx= 7, pady = 3)
    
    lbl = Label(win, text = "title :")
    lbl.grid(column = 0, row = 3 , sticky ='w', padx = 7, pady = 3)
    
    lbl = Label(win, text = "author :")
    lbl.grid(column = 0, row = 4 , sticky='w', padx = 7, pady = 3)
    
    lbl = Label(win, text = "quality :")
    lbl.grid(column = 0, row = 6, sticky ='w', padx = 7, pady = 3)
    
    
    lbl = Label(win, text = "category:")
    lbl.grid(column = 0, row = 5, sticky='w', padx = 7, pady = 3)

    btn = Button(win, text="download audio", command = audio_download) 
    btn.grid(column = 2, row = 9, sticky = 'n', padx = 7, pady = 10)
    
    btn = Button(win, text="download video", command = video_download) 
    btn.grid(column = 3, row = 9, sticky = 'n', padx = 7, pady = 10)
    
    lbl = Label(win, text = "total (audio) (mb) :")
    lbl.grid(column = 0, row = 7, sticky = 'w', padx = 7, pady = 5)
    
    lbl = Label(win, text = "total (video) (mb) :")
    lbl.grid(column = 0, row = 8, sticky = 'w', padx = 7, pady = 5)
    win.mainloop()
    
    
    win.mainloop()
    
except Exception as e:
    print(e)