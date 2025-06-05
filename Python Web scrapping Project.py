#!/usr/bin/env python
# coding: utf-8
# 1.Python Web scrapping Project
# In[5]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[40]:


print(webpage.text)


# In[45]:


current_page = 1


# In[58]:


data = []


# In[65]:


proceed = True
while(proceed):
    print("currently scraping page:"+str(current_page))
    url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"
    
    webpage = requests.get(url)
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    
    if soup.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        
        for book in all_books:
            item = {}
            
            item['Title'] = book.find("img").attrs["alt"]
            
            item['link'] = book.find("a").attrs["href"]
            
            item['Price'] = book.find("p", class_="price_color").text[2:]
            
            item['Stock'] = book.find("p", class_="instock availability").text.strip()
            
            data.append(item)
    
    current_page += 1
df = pd.DataFrame(data)
df.to_excel("books.xlsx")
df.to_csv("books.csv")


# In[ ]:




