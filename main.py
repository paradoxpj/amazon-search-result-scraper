from bs4 import BeautifulSoup
import requests

from constants import URL


def search(soup):
    '''Function to get list of items on search results page on Amazon'''
    # A counter to maintain count of items scraped
    counter=1
    for item in soup.find_all('div', attrs={'class': 's-result-item'}):
        # Getting various fields using respective html tag classes
        name = item.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
        rating = item.find('span', attrs={'class': 'a-icon-alt'})
        rating_count = item.find('span', attrs={'class': 'a-size-base'})
        price_symbol = item.find('span', attrs={'class': 'a-price-symbol'})
        price = item.find('span', attrs={'class': 'a-price-whole'})
        if (name is None) or (rating is None) or (rating_count is None) or (price_symbol is None) or (price is None):
            # Condition to check if any field is None.
            # If any of the field is none, then the item is not a search result as Amazon uses same classes for other elements as well.
            continue
        else:
            print(counter, ":")
            print("Name-", name.get_text())
            print("Rating-", rating.get_text(), "("+rating_count.get_text()+")")
            print("Price-", price_symbol.get_text(), price.get_text())
            counter+=1


if __name__ == '__main__':

    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    search(soup)
