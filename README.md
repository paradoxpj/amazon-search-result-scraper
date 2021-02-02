# amazon-search-result-scraper

A simple python project that scrapes out items and their details from Amazon search results web-page using _BeautifulSoup_.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies of the _amazon-search-result-scraper_.

```bash
pip install -r requirements.txt
```

## How to run

The code extracts the list of items on the provided Amazon web-page and puts it in an xlsx sheet.
To provide a search result web-page url, change the contents of constants.py file -

```python
URL = ""
```  

To run the program, enter following code in a terminal inside the project's directory -

```bash
python main.py
```

or

```bash
python3 main.py
```

Check the outcome in the _result.xlsx_ sheet.

## Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change or check the already open issues.
