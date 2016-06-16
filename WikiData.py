
import wikipedia
import urllib2
import urllib2 as urllib
import io
from PIL import *
import PIL
import os
import re


def  wikiSearch(name, number):
      global ReturnData
      global PageInfo
     
      PageInfo =  wikipedia.page(name)
      ReturnData  = wikipedia.summary(name, number)
      


def GivingFuck():
      return ReturnData

def  title():
      return PageInfo.title

def  url():
      return PageInfo.url


      

def  imageFront():
      global URL_LIST
      URL_LIST = []
      Img_list = []

      comp  = re.compile("https://(.+?).jpg")
      comp2  = re.compile("[(.+?)]")
      
      wiki =  PageInfo.images
      
     
      for i in wiki:
            Img_list.append(re.findall(comp, str(i)))

      lenDatacount = Img_list.count([])
      
      print lenDatacount

      for ii in range(lenDatacount):
            Img_list.remove([])
            
      for ie in Img_list:
            URL_LIST.append(ie[0])
            
      return URL_LIST[0]

def imageAll():
      return len(PageInfo.images)

def getImage():
      url = str("https://"+imageFront()+".jpg")
      print url
   
      Ima = urllib.urlopen(url)
      im_image = io.BytesIO(Ima.read())
      im = Image.open(im_image)
      im.save("image.png")

def ResizeImage():
      basewidth = 380
      img = Image.open("image.png")
      wpercent = (basewidth / float(img.size[0]))
      hsize = int((float(img.size[1]) * float(wpercent)))
      img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
      img.save("RE_IMAGE.png")




      
      
 
