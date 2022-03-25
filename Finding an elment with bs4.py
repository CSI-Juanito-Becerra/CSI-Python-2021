
# import requests
# import webbrowser
# import bs4
# import sys




# # search_term = 'python'

# print('Googling...') # display text while downloading the Google page
# res = requests.get("https://www.google.com/search?q=abolicion+de+la+esclavitud" + " ".join(sys.argv[1:]))

# # Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text, 'html.parser')

# # Open a browser tab for each result.
# linkElems = soup.select('.package-snippet')
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'https://www.google.com' + linkElems[i].get('href')
#     print('Opening', urlToOpen)
#     webbrowser.open(urlToOpen)

# # import bs4
# # import sys
# # import requests
# # import webbrowser
# # print("Searching")
# # wordSearch = "python"
# # res = requests.get('http://google.com/search?q=?' + wordSearch.join(sys.argv[1:]))
# # res.raise_for_status()
# # soup = bs4.BeautifulSoup(res.text, 'html.parser')
# # linkElems = soup.select('.r a')
# # numOpen = min(5, len(linkElems))
# # for i in range(numOpen):
# #     urlToOpen = "https://www.google.com/" + linkElems[i].get("href")
# #     print("Opening", urlToOpen)
# #     webbrowser.open(urlToOpen)
# # exampleFile = open("example.html")
# # exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
# # pElems = exampleSoup.select("p")
# # type(pElems)
# # print(len(pElems))
# # print(str(pElems[0]))
# # print(pElems[0].getText())
# # print(pElems[2].getText())


#!/usr/bin/env python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4
print('Searching...')  #Display text while downloading search result page.  
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])) 
print(sys.argv[1:])
res.raise_for_status()

# Retrieve top search result links. 
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#Open a browser tab for each result, the element looks like this when search the term "boring stuff": <a class="package-snippet" href="/project/boring/">
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # join the href to the base url 
    urlToOpen = 'http://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
