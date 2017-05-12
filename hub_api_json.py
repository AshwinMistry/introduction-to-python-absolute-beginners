import json
import urllib.request

# open the url
url = "http://hub.nature.com/api/v1/articles?page=1&pageSize=10&publicationDate=2017-01-01%2F2017-01-07&domain=nature&client=xmldev"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib.request.urlopen(url))

# json response from hub api contains both query and articles.
# mapping articles part of response to articles variable
articles = data["articles"]

#print(articles)
for article in articles:
    print(article["id"], ' - ', article["title"])
#    print(article["title"])