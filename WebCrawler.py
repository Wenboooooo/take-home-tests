import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website
URL = 'https://www.bbc.com/news'

# Send a request to fetch the content of the page
response = requests.get(URL)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the article elements using the appropriate HTML structure
articles = soup.find_all('div', {'data-testid': 'card-text-wrapper'})  # locate info based on the structure of div

# Create lists to hold the scraped data
titles = []
descriptions = []
last_updated_times = []
tags = []

# Scrape the title, description, last updated time, and tag for each article
for article in articles:
    # Extract the title
    title_tag = article.find('h2', {'data-testid': 'card-headline'})
    title = title_tag.text.strip() if title_tag else 'N/A'

    # Extract the description
    description_tag = article.find('p', {'data-testid': 'card-description'})
    description = description_tag.text.strip() if description_tag else 'N/A'

    # Extract the last updated time
    last_updated_tag = article.find('span', {'data-testid': 'card-metadata-lastupdated'})
    last_updated = last_updated_tag.text.strip() if last_updated_tag else 'N/A'

    # Extract the tag (e.g., US & Canada)
    tag_tag = article.find('span', {'data-testid': 'card-metadata-tag'})
    tag = tag_tag.text.strip() if tag_tag else 'N/A'

    # Append the scraped data to the respective lists
    titles.append(title)
    descriptions.append(description)
    last_updated_times.append(last_updated)
    tags.append(tag)

    # Stop after collecting 100 articles (or fewer if available)
    if len(titles) >= 100:
        break

# Create a DataFrame to store the data
data = pd.DataFrame({
    'Title': titles,
    'Description': descriptions,
    'Last Updated': last_updated_times,
    'Tag': tags
})

# Save the data to a CSV file
csv_filename = 'scraped_articles.csv'
data.to_csv(csv_filename, index=False)

print(f'Data scraped successfully and saved to {csv_filename}')