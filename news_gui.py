import webbrowser
import io
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import  ImageTk,Image





class NewsApp:

    def __init__(self):

        #fetch data

        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=07ce6431517e45c5b04b589c36e5bed6' ).json()

        #initial GUI
        self.load_gui()

        #load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title("News App")
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        #clear the screen for the new news item
        self.clear()

        #image
        try:
            image_url = self.data['articles'][index]['urlToImage']
            raw_data=urlopen(image_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        except:
            image_url = 'data:image/png;base64,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'
            raw_data = urlopen(image_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image=photo)
        label.pack()

        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,justify='center')
        details.pack(pady=(10, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)
        if index!=0:
            prev = Button(frame,text='Prev',width=16,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=16, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj =NewsApp()