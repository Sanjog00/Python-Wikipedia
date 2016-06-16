
from Tkinter import *
from ScrolledText import *
import Tkinter as tk
from PIL import Image, ImageTk
import threading
import ttk
import tkMessageBox
import wikipedia
import Tkinter as tkinter
import WikiData
import os


class WikiPedia:
      def Wiki_Window(self, window):
            self.window = window
            self.window.geometry("1500x1500")
            
      def Notebook(self):
            self.notebook = ttk.Notebook(self.window)
            self.framePyRat = ttk.Frame(self.notebook, width=2500, height=1000)
            self.frameAbout = ttk.Frame(self.notebook, width=2500, height=1000)
            self.notebook.add(self.framePyRat, text='PyPedia')
            self.notebook.add(self.frameAbout, text='About')
            self.notebook.grid(row=0)

      def Design(self):
              ttk.Labelframe(self.window, width=1350, height=140).grid(row=0, sticky = NW)
              Label(self.window, text="Welcome To PyPedia",font=("Helvetica",20)).grid(row=0, column=0, sticky = NW, pady=50, padx = 450)
              image = Image.open("wikilogo.png")
              photo = ImageTk.PhotoImage(image)
              label = Label(image=photo)
              label.image = photo 
              label.grid(row=0, column=0, sticky = NW, padx=1150)

      def search(self):
             global infowiki
             infowiki = StringVar()
             ttk.Labelframe(self.window, width=1350, height=600).grid(row=0, sticky = NW, pady=150, column=0)
             ttk.Labelframe(self.window, width=500, height=300).grid(row=0, sticky = NW, pady=174, column=0, padx=800)
             ttk.Labelframe(self.window, width=750, height=600).grid(row=0, sticky = NW, pady=174, column=0, padx=20)
             self.WikiInfo = ScrolledText(self.window, width=65,height=18, bd=7,font=("Helvetica",15))
             self.WikiInfo.grid(row=0, sticky = NW, pady=280, column=0, padx=20)
             self.WikiInfo.insert(END, "Please Search For Content\n")
          
 
      
                 
            
                
      
      def Content(self):
            global infowiki
            infowiki = StringVar()
            Label(self.window, text="Search:: ",font=("Helvetica",18)).grid(row=0, column=0, sticky = NW, pady=210, padx=30)
            Entry(self.window, width=30, bd=4,textvariable=infowiki, font=("Helvetica",15)).grid(row=0, column=0, sticky = NW, pady=210, padx=140, ipady=3)
            Button(self.window,text="Go", bd=5, command = self.thread).grid(row=0, column=0, sticky = NW, pady=210, padx=500, ipady=1, ipadx=20)
            self.snip = Spinbox(self.window, from_=0, to=1000, width=10)
            self.snip.grid(row=0, column=0, sticky = NW, pady=215, padx=590, ipady=1, ipadx=20)
            Label(self.window, text="Sentence::",font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=190, padx=595)
            ttk.Labelframe(self.window, width=500, height=300).grid(row=0, sticky = NW, pady=480,padx=800, column=0)
            Label(self.window, text="Information ",font=("Helvetica",18)).grid(row=0, column=0, sticky = NW, pady=500, padx=815)
            Label(self.window, text="Image  (0)(0)",font=("Helvetica",18)).grid(row=0, column=0, sticky = NW, pady=160, padx=970)
            
            

            
      def Info(self):
            
            Label(self.window, text="Title :",font=("Helvetica",15)).grid(row=0, column=0, sticky = NW, pady=540, padx=815)
            Label(self.window, text="Url :",font=("Helvetica",15)).grid(row=0, column=0, sticky = NW, pady=580, padx=815)
            Label(self.window, text="Total Image In Url :",font=("Helvetica",15)).grid(row=0, column=0, sticky = NW, pady=625, padx=815)
            Label(self.window, text="Main Image :",font=("Helvetica",15)).grid(row=0, column=0, sticky = NW, pady=670, padx=815)
            
     

            
              
      def GoSearch(self):
            
            try:
               
                text = "                                                                                                                                                                                          "
                Label(self.window, text=text,font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=540, padx=870)
                Label(self.window, text=text,font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=580, padx=860)
                Label(self.window, text=text,font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=625, padx=985)
                Label(self.window, text=text,font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=670, padx=940)
                 
                self.WikiInfo.delete(1.0, END)
                self.WikiInfo.insert(END, "Title :: "+infowiki.get())
                self.WikiInfo.insert(END, "\n")
                self.WikiInfo.insert(END, "\n")
                WikiData.wikiSearch(infowiki.get(), self.snip.get())
                self.WikiInfo.insert(END, WikiData.GivingFuck())
                self.Info()
                            
                Label(self.window, text=WikiData.title(),font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=540, padx=870)
                Label(self.window, text=WikiData.url(),font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=580, padx=860)
                Label(self.window, text=WikiData.imageAll(),font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=625, padx=985)
                Label(self.window, text=WikiData.imageFront(),font=("Helvetica",12)).grid(row=0, column=0, sticky = NW, pady=670, padx=940)

                WikiData.getImage()
                WikiData.ResizeImage()
                
                



                image = Image.open("RE_IMAGE.png")
                photo = ImageTk.PhotoImage(image)
                self.label = Label(image=photo, bd=8)
                self.label.image = photo 
                self.label.grid(row=0, column=0, sticky = NW, pady=200, padx=830 )
                os.system("del image.png")
                os.system("del RE_IMAGE.png")
                     
                    
               
      

            except :
                        global opt
                        opt = []
                        
                        self.WikiInfo.insert(END, " \n")
                        self.WikiInfo.insert(END, "Found Other insted Of  "+ infowiki.get())
                        self.WikiInfo.insert(END, "\n")
                        self.WikiInfo.insert(END, " Please Insert Underscore in space like Apple_Inc \n")
                        serc = wikipedia.search(infowiki.get(), 20)
                        self.WikiInfo.insert(END, "\n")
                        for i in serc:
                              
                                    opt.append(i)
                                    self.WikiInfo.insert(END, i," \n")
                                    self.WikiInfo.insert(END, " \n")
                                    self.WikiInfo.insert(END, "\n")
                                    
                        

                
      def  thread(self):
            proc = threading.Thread(target = self.GoSearch)
            proc.start()
            
            
            
            
        
            


PyPedia = WikiPedia()
win = Tk()
PyPedia.Wiki_Window(win)
PyPedia.Notebook()
PyPedia.Design()
PyPedia.search()
PyPedia.Content()
mainloop()

