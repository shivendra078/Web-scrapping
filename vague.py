import requests
from bs4 import BeautifulSoup

url = 'https://schools.org.in/uttar-pradesh/agra/acchnera/-town-area'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Finding a specific element first
    results = soup.find('div', class_='card my-3')

    # Check if the element is found before calling find_all
    if results:
        # Find all tables with class 'table table-striped'
        tables = results.find_all('table', class_='table table-striped')

        # Further processing of the tables if needed
        for table in tables:
            # Your code to extract data from each table
            print(table.text)

    else:
        print('The specified element was not found on the page.')

else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)

