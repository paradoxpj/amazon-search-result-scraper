import requests

from bs4 import BeautifulSoup
from openpyxl import Workbook

from constants import URL


def scrape():
    '''Function to scrape data from Amazon search results page and put it into an xls sheet'''
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")
    # Calling search function thaat scrapes items and returns them in a list
    items = search(soup)
    # Calling the function to extract items into an xls sheet
    extract_in_xls(items)

def search(soup):
    '''Function to get list of items on search results page on Amazon'''
    # A list to store details of the items
    items = []
    for item in soup.find_all('div', attrs={'class': 's-result-item'}):
        # Getting various fields using respective html tag classes
        name = item.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
        rating = item.find('span', attrs={'class': 'a-icon-alt'})
        rating_count = item.find('span', attrs={'class': 'a-size-base'})
        price_symbol = item.find('span', attrs={'class': 'a-price-symbol'})
        price = item.find('span', attrs={'class': 'a-price-whole'})
        if None in (name, rating, rating_count, price_symbol, price):
            # Condition to check if any field is None.
            # If any of the field is none, then the item is not a search result as Amazon uses same classes for other elements as well.
            continue
        else:
            # Extracting text from bs4 tag elements and appending a list of the fields into the items list
            items.append(
                [ name.get_text(),
                float(rating.get_text().split()[0]),
                int(rating_count.get_text().replace(",", "")),
                price_symbol.get_text(),
                int(price.get_text().replace(",", "")) ]
            )
    return items

def extract_in_xls(items):
    ''' A function to extract items in the items list into an xls sheet'''
    wb = Workbook()
    ws = wb.active
    # Assigning names to Column
    ws['A1'] = 'Title'
    ws['B1'] = 'Ratings'
    ws['C1'] = 'Rated By'
    ws['D1'] = 'Price Symbol'
    ws['E1'] = 'Price'
    # Appending rows into xls sheet
    for item in items:
        ws.append(item)
    # Saving the worksheet into a local xls sheet
    wb.save("result.xlsx")

if __name__ == '__main__':
    '''main function'''
    scrape()
