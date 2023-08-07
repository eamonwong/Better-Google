import webbrowser
import sys

url = 'http://www.google.com/search?q='

valid_websites = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange',
    'medium.com'
]

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

def create_filter():
    filter = '('
    for index, website in enumerate(valid_websites):
        filter += 'site:' + website
        if index == len(valid_websites) - 1:
            filter += ')'
        else:
            filter += ' OR '
    return filter

def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_url():
    if len(sys.argv[1:]) == 0:
        print("Error: Please enter a valid search query.")
    else:
        final_url = url + create_query() + create_filter()
        webbrowser.get(chrome_path).open(final_url)

create_url()
