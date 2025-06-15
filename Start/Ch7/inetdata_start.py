# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#
# import the library to retrieve data from the internet
import urllib.request

web_url = urllib.request.urlopen("http://www.example.com")
print("Response code: ", web_url.getcode())

data = web_url.read()
print("Data retrieved from the web:")
print(data)
