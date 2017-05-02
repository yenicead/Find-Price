from bs4 import BeautifulSoup
import requests, re

# Taking the URL from User
URL = input('Enter an URL : ')
URLIndex = requests.get(URL)

# Using bs4 library, we pull the content of the url.
soup = BeautifulSoup(URLIndex.content, "html.parser")

# This method is used to find the price of the product with related parameters.
priceFinder = lambda tag: (getattr(tag, 'name', None) == 'span' and 'content' in tag.attrs and '' 
                          in tag.get_text().lower())

# After taking the span tags, we first convert it to str then split every words.
abc = str(soup.find(priceFinder)).split(" ")

# The third [2] information includes the price of the product. We also need to split the price and content tags. 
b = str(abc[2]).split("=", 2)

# Finally, we split the price of the product and showing to user.
c = b[1]
print('The price : ', c, 'TL')