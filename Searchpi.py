import requests
import webbrowser
import bs4
# searchResult = "python"
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=python', 'html.parser')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.content, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))