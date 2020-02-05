#!/usr/bin/python3
import easygui as g

def enterbox(msg,title):
    msg = g.enterbox(msg, title, default='',strip = False,image=None)
    print(msg)

enterbox(msg = 'content',title = 'title')