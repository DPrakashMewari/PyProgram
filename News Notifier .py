#!/usr/bin/env python
# coding: utf-8

# In[3]:


import feedparser
import pynotifier
from pynotifier import Notification
import time


# In[4]:


f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")


# In[ ]:


def parsenews():
    for val in f['items']:
        Notification(title="News",description=val['title'],duration=1,urgency="low").send()
        Notification(title="News Summary",description=val['summary'],duration=1,urgency='low').send()
    time.sleep(1200)
    
if __name__ == "__main__":
    parsenews()


# In[20]:


h = feedparser.parse("https://zeenews.india.com/hindi/india.xml")


# In[ ]:


def zeenews():
    for val in h['items']:
        Notification(title="Zee News",description=val['title'],urgency="low",duration=2).send()
    time.sleep(1300)
if __name__ == "__main__":
    zeenews()

