# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:19:51 2023

@author: DELL
"""

from tkinter import*
import random 

root = Tk()
root.title("list")
root.geometry("500x400")

list_item = Label(root)
random_no = Label(root)
list = ["bottle", "lunchbox" , "games" , "chocolate" , "napkins" , "diary" , "pen"]

list_item["text"] = "Listed items : " + str(list)

def randomlist() :
    
    number = random.sample(range(0,6),1)
    random_no["text"] = " Put item" + str(number) + " in the bag"
    
btn = Button(root , text = "Which item to put in bag ?", command = randomlist)
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
list_item.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)
random_no.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)
    

root.mainloop()

