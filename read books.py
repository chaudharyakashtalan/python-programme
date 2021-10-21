#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#we are going to create an audio book


# In[ ]:


# module 1: pyttsx3
# module 2: PyPDF2


# In[1]:

import pyttsx3
import PyPDF2
boook = open("bppd.pdf","rb")
pdfReader = PyPDF2.PdffileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
page=pdfReader.getPage(24)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()


# In[ ]:




