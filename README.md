# TECHIN510_lab4

## getting started 


```
python -m venv venv
source venv/bin/activate
pip install -r requirement.txt

streamlit run app.py
```
## webapp features
This lab focuses on creating a web scraper using Python and BeautifulSoup to extract book data from the website "https://books.toscrape.com/". The scraped data is then stored in a PostgreSQL database and displayed in a Streamlit web app. Users can search, filter, and sort the scraped book data based on various criteria.

## lesson learned

Learning to use BeautifulSoup for web scraping offered invaluable insights into HTML structure analysis, element selection, and adapting to varied page layouts. This project involved navigating multiple pages and extracting data such as book descriptions, highlighting the importance of understanding website navigation and pagination. Cleaning and transforming the scraped data, including price adjustments and managing missing descriptions, was crucial for data integrity.
