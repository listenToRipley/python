import webbrowser

# webbrowser.open('http://pypi.org')

def search_on_search_engine(query, search_engine):
  search_engines = {
    'google': 'https://www.google.com/search?q={}',
    'yahoo' : 'https://search.yahoo.com/search?p={}',
    'bing' : 'https://www.bing.com/search?q={}',
  }

  if search_engine not in search_engines:
    print("Unsupported search engine ", search_engine)
    return
  search_url = search_engines[search_engine].format(query)

  webbrowser.open(search_url)

search_on_search_engine("food near me", "google")