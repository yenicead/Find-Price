from bs4 import BeautifulSoup
import requests, re

# Taking the URL from user until given URL is valid.
while True:
     try:
          URL = input('Enter an URL : ')
          URLIndex = requests.get(URL)
          break
     except ValueError:
          print('Oops!  That was no valid URL.  Try again...');

# Using bs4 library, we pull the content of the url.
soup = BeautifulSoup(URLIndex.content, "html.parser")

# This method is used to find the price of the product with related parameters.
priceFinder = lambda tag: (getattr(tag, 'name', None) == 'span' and 'content' in tag.attrs and '' 
                       in tag.get_text().lower())

# After taking the span tags, we first convert it to str then split every words.
pfString = str(soup.find(priceFinder)).split(" ")

# The third [2] information includes the price of the product. We also need to split the price and content tags. 
productInformation = str(pfString[2]).split("=", 2)

# Finally, we split the price of the product and showing to user.
productPrice = productInformation[1]
print('The price :', productPrice,  'TL');
