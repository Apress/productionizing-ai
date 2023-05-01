#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ONE OFF INSTALL - Chinese text segmentation
# %pip install jieba


# In[ ]:


# Libraries
from wordcloud import WordCloud

import PIL.Image as image

import numpy as np

import jieba


# In[ ]:


# function to parse Chinese characters and prepare text for Word Cloud

def trans_CN(text):

    word_list = jieba.cut(text)

    result = " ".join(word_list) # add spaces between Chinese characters

    return result


# Below data source taken from China Daily main headline https://cn.chinadaily.com.cn/

# In[ ]:


with open('china-daily.txt',encoding='UTF-8') as fp:

    text = fp.read()

text = trans_CN(text) # call the function above to segment words

mask = np.array(image.open('zhu.jpg')) # use an image "template" - the word cloud will be in this shape


# In[ ]:


text # check data for encoding for word cloud


# In[ ]:


mask # check numpy array format for word cloud


# In[ ]:


# Generate Word Cloud

wordcloud = WordCloud(background_color='white', # or #FFFFFF
                      mask=mask, # Add mask layer 
                      font_path="C:\Windows\Fonts\msyh.ttc" # Generate fonts for Chinese characters
                      ).generate(text)

image_produce = wordcloud.to_image()

image_produce.show()

wordcloud.to_file('wc-zw-final.jpg') # the final image


# Exercises:
# 
# -- run the code using instead the English data example (pasta recipe)
# 
# -- replace the pig image template with a different Chinese zodiac image (use images from e.g. https://www.astrosage.com/chinese-zodiac/)
# 
# -- update the code to generate the word cloud based on the current Chinese Year (tiger, rabbit, dragon etc.) 

# In[ ]:





# Source Reference: https://pythonmana.com/2021/04/20210413162743483e.html (with some adaptions)
