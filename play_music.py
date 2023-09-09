from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
music=Tk()
music.title("music")
music.geometry("500x440")
pygame.mixer.init()
import os

def next():
    next_one=box.curselection()
    next_one=next_one[0]+1
    song=box.get(next_one)
    songe=fr"c:\Users\hp pc\OneDrive\Bureau\songs\{song}"
    pygame.mixer.music.load(songe)
    pygame.mixer.music.play()
    box.select_clear(0,END)
    #box.activate(next_one)
    box.select_set(next_one,last=None)
    my_slider.config(value=0)

def previous():
    prev_one=box.curselection()
    prev_one=prev_one[0]-1
    song=box.get(prev_one)
    songe=fr"c:\Users\hp pc\OneDrive\Bureau\songs\{song}"
    pygame.mixer.music.load(songe)
    pygame.mixer.music.play()
    box.select_clear(0,END)
    #box.activate(next_one)
    box.select_set(prev_one,last=None)
    my_slider.config(value=0)
def add_many():
    song_files = filedialog.askopenfilenames(
        initialdir=r"c:\Users\hp pc\OneDrive\Bureau\songs",
        title="Choose songs",
        filetypes=(("mp3 files", "*.mp3"),)
    )
    
    
    for song_path in song_files:
        song_name = os.path.basename(song_path)
        box.insert(END, song_name)
        print(song_name)

def add():
    song_file = filedialog.askopenfilename(
        initialdir=r"c:\Users\hp pc\OneDrive\Bureau\songs",
        title="Choose one",
        filetypes=(("mp3 file", "*.mp3"),)
    )
    
    
     ### .name return the complete file path
    song_name = os.path.basename(song_file)
    
   

    box.insert(END, song_name)
    print(song_name)
    
def play_time():
    global lenght,curr_time
    curr_time=pygame.mixer.music.get_pos()/1000
    conv_time=time.strftime("%M:%S",time.gmtime(curr_time))
    conv_slider=time.strftime("%M:%S",time.gmtime(my_slider.get()))
    #curr_time=box.curselection()
    song=box.get(ACTIVE)
    songe=fr"c:\Users\hp pc\OneDrive\Bureau\songs\{song}"
    muta=MP3(songe)
    lenght=muta.info.length
    lenght_time=time.strftime("%M:%S",time.gmtime(lenght))
    statu_bar.config(text=f' time : {conv_time} / {lenght_time} ')
    slider_label.config(text=f' {conv_slider} / {lenght_time}')
    curr_time+=1
    if conv_slider==lenght_time:
        slider_label.config(text=f' time : {lenght_time} / {lenght_time}')

    
    elif conv_slider == conv_time:
        slider_position=int(lenght)
        my_slider.config(to=slider_position,value=curr_time)
    
    else:
        slider_position=int(lenght)
        my_slider.config(to=slider_position,value=my_slider.get())
        conv_slider=time.strftime("%M:%S",time.gmtime(my_slider.get()))
        statu_bar.config(text=f' time : {conv_slider} / {lenght_time}')
        next_time=int(my_slider.get())+1
        my_slider.config(value=next_time)
       

   # statu_bar.config(text=f' time : {conv_time} / {lenght_time} ')
    #my_slider.config(value=curr_time)
    
    #statu_bar.config(text=conv_time)
    statu_bar.after(1000,play_time)
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    curr_volume=pygame.mixer.music.get_volume()
    volume_label.config(text=int(curr_volume*100))
    
def slide(x):
    #slider_label.config(text=f"{int(my_slider.get())}/{int(lenght)}")
    song = box.get(ACTIVE)
    song_path = f"c:\\Users\\hp pc\\OneDrive\\Bureau\\songs\\{song}"
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0,start=my_slider.get())
def plaay():
    
    song = box.get(ACTIVE)
    song_path = f"c:\\Users\\hp pc\\OneDrive\\Bureau\\songs\\{song}"
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)
    play_time()
    curr_volume=pygame.mixer.music.get_volume()
    volume_label.config(text=int(curr_volume*100))
    
    

stoped=FALSE
def sttop():
    statu_bar.config(text="")
                   
    my_slider.config(value=0)

    pygame.mixer.music.stop()
    box.select_clear(ACTIVE)
    #statu_bar.config(text="")
    #my_slider.config(value=0)
    global stoped
    stoped=TRUE
def delete_one():
    box.delete(ANCHOR)
    pygame.mixer.music.stop()
def delete_all():
    box.delete(0,END)
    pygame.mixer.music.stop()

master_frame=Frame(music)
master_frame.pack(pady=20)


box=Listbox(master_frame,width=60,foreground='green',bg="black")
box.grid(row=0,column=1)
#a=Image.open(r"c:\Users\hp pc\OneDrive\Bureau\music\button-24836_960_720.webp")
forward=PhotoImage(file=(r"c:\Users\hp pc\OneDrive\Bureau\music\R (4).png"))
play=PhotoImage(file=(r"c:\Users\hp pc\OneDrive\Bureau\music\Button-Play-icon.png"))
stop=PhotoImage(file=(r"c:\Users\hp pc\OneDrive\Bureau\music\Button-Stop-icon.png"))
back=PhotoImage(file=(r"c:\Users\hp pc\OneDrive\Bureau\music\R (5).png"))
#forward=ImageTk.PhotoImage(Image.open(r"c:\Users\hp pc\OneDrive\Bureau\music\R 23.png"))
framee=Frame(master_frame)
framee.grid(row=1,column=1)
forward_btn=Button(framee,image=forward,borderwidth=0,command=next)
play_btn=Button(framee,image=play,borderwidth=0,command=plaay)
stop_btn=Button(framee,image=stop,borderwidth=0,command=sttop)
back_btn=Button(framee,image=back,borderwidth=0,command=previous)
forward_btn=Button(framee,image=forward,borderwidth=0,command=next)

forward_btn.grid(row=0,column=3,padx=10)
play_btn.grid(row=0,column=0,padx=10)
stop_btn.grid(row=0,column=1,padx=10)
back_btn.grid(row=0,column=2,padx=10)
#create menu
my_menu=Menu(music)
music.config(menu=my_menu)
#add songs
add_songs=Menu(my_menu)
my_menu.add_cascade(label="add",menu=add_songs)
add_songs.add_command(label="add song",command=add)
add_songs.add_command(label="add many song",command=add_many)
delete=Menu(my_menu)
my_menu.add_cascade(label="delet",menu=delete)
delete.add_command(label="delet one song",command=delete_one)
delete.add_command(label="delet all songs",command=delete_all)

## staut bar
statu_bar=Label(music,text='',bd=1,relief=GROOVE,anchor=E)
statu_bar.pack(fill=X,ipady=3,side=BOTTOM)
### create a slider
my_slider=ttk.Scale(master_frame,orient=HORIZONTAL,from_=0,to=100,length=200,command=slide,value=0)
my_slider.grid(row=3,column=1,pady=20)
slider_label=Label(music,text='0')
slider_label.pack(pady=5)
volume_frame=LabelFrame(master_frame,font=("Arial",10),borderwidth=1,text='Volume')
volume_frame.grid(row=0,column=2,padx=20)
volume_label=Label(volume_frame,text='0')
volume_label.pack(pady=10)

volume_slider=ttk.Scale(volume_frame,orient=VERTICAL,from_=0,to=1,length=150,value=1,command=volume)
volume_slider.pack(padx=10)
music.mainloop()