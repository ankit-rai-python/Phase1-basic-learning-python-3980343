# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML

import xml.dom.minidom as minidom

# Load and parse the XML file
doc = minidom.parse("sample.xml")

# Print basic document info
print("Document node:", doc.nodeName)
print("First child tag:", doc.firstChild.nodeName)

# Get a list of all <title> tags
titles = doc.getElementsByTagName("title")
for tag in titles:
    print("Tag name:", tag.nodeName)
    print("Tag value:", tag.firstChild.nodeValue)

print("First title tag value:", titles[0].firstChild.nodeValue)
print("Number of title tags:", len(titles))
print("Title node list:", titles)

# Get the root <library> element (assuming root element is <library>)
library = doc.getElementsByTagName("library")[0]

# Create a new <book> element
new_book = doc.createElement("book")
new_book.setAttribute("id", "b4")

# Create and append <title>
title = doc.createElement("title")
title_text = doc.createTextNode("Automate the Boring Stuff")
title.appendChild(title_text)
new_book.appendChild(title)

# <author>
author = doc.createElement("author")
author_text = doc.createTextNode("Al Sweigart")
author.appendChild(author_text)
new_book.appendChild(author)

# <year>
year = doc.createElement("year")
year_text = doc.createTextNode("2023")
year.appendChild(year_text)
new_book.appendChild(year)

# <price>
price = doc.createElement("price")
price_text = doc.createTextNode("35.00")
price.appendChild(price_text)
new_book.appendChild(price)

# Append the new <book> to the <library>
library.appendChild(new_book)

# Output the updated XML
print(doc.toprettyxml())
