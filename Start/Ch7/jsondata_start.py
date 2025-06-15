# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json

# Open the URL and read the data
url_json = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print("Response code: ", url_json.getcode())

# Read the JSON data from the source
data = url_json.read()
print("Data retrieved from the web:")
# print(data)

# Print the content of the 'text' field
json_data = json.loads(data)
print(json_data["text"])
