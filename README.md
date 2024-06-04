# TECHIN510_lab4

## Book Scraper

### Overview

This app scrapes book data from "https://books.toscrape.com/" and stores it in a PostgreSQL database. The data is displayed in a Streamlit web app, allowing users to search, filter, and sort the books.

### Features
- **Web Scraping**: Extracts book information (title, price, rating, description) from all 50 pages.
- **Database Storage**: Stores the scraped data in a PostgreSQL database.
- **Search Functionality**: Allows users to search books by title or description.
- **Filtering**: Filter books based on price range and rating.
- **Sorting**: Sort books by price in ascending order.
- **Scraping Control**: Prevents unnecessary scraping by checking if data already exists in the database.

### Reflections
- **Learning**: Gained insights into HTML structure analysis and element selection with BeautifulSoup.
- **Data Management**: Highlighted the importance of cleaning and transforming data for integrity.
- **Database Integration**: Demonstrated the integration with PostgreSQL for data storage and retrieval.
- **User Experience**: Enhanced with search, filtering, and sorting functionalities using dynamic SQL queries.
- **Resource Efficiency**: Emphasized efficient resource use and UI design to minimize unnecessary scraping.

## Weather App

### Overview

This app provides real-time weather information and a 3-day forecast based on the location entered by the user.

### Features
- **Real-time Weather Data**: Fetches current temperature and weather conditions using Meteomatics API.
- **3-Day Forecast**: Provides temperature ranges and weather conditions for the next three days.
- **Geocoding**: Converts city names to geographical coordinates using Geopy.
- **User-Friendly Interface**: Interactive web application built with Streamlit.

### How to Run
1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-repo/weather-app.git
    cd weather-app
    ```

2. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**
    - Create a `.env` file in the root directory.
    - Add your Meteomatics API credentials:
      ```
      METEOMATICS_USERNAME=your_meteomatics_username
      METEOMATICS_PASSWORD=your_meteomatics_password
      ```

4. **Run the Streamlit App**
    ```bash
    streamlit run weather_app.py
    ```

5. **Open the App in Your Web Browser**
    - Navigate to `http://localhost:8501` to start using the app.

### Reflections
- **API Integration**: Learned to integrate multiple APIs for data fetching and display.
- **Error Handling**: Improved handling of invalid city names and API request failures.
- **User Interface**: Enhanced user experience with intuitive design and clear weather information.
- **Data Presentation**: Presented real-time and forecasted weather data effectively using Streamlit.


