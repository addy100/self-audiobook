#!/usr/bin/env python
# coding: utf-8

# In[1]:
##Self Audiobook
import pyttsx3


# In[2]:
speaker = pyttsx3.init()
speaker.say('Hey! I like you')
speaker.runAndWait()


# In[3]:
## read content from a foreign file (pdf, docx)
import PyPDF2


# In[4]:
book = open('C:\Users\RISING-PEGASUS 007\Desktop\skull candy Warranty Claim Form,pdf', rb)
reader = PyPDF2.PdfFileReaader(book)

pages = pdfReader.numPages
print(pages)

##To get any random page num
pg = pdfReader.getPage()

## To
text = pg.extractext()
