#COdeD By Sanjog

import re
import wikipedia

def  imageFront():
      global URL_LIST
      URL_LIST = []
      Img_list = []

      comp  = re.compile("https://(.+?).png")
      comp2  = re.compile("[(.+?)]")
      
      wiki =  wikipedia.page("Nepal")
      img = wiki.images
      
      
     
      for i in img:
            Img_list.append(re.findall(comp, str(i)))

      lenDatacount = Img_list.count([])
      
      print lenDatacount

      for ii in range(lenDatacount):
            Img_list.remove([])
            
      for ie in Img_list:
            URL_LIST.append(ie[0])
            
            
      print URL_LIST[:2]
      
      
      return URL_LIST[1]

      
   
      

imageFront()

#COdeD By Sanjog
