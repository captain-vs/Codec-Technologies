import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from bs4 import BeautifulSoup
import requests
import re


def extract_features(url):
    features = []

    # Feature 1: Length of URL
    features.append(len(url))

    # Feature 2: Presence of IP address in URL
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    features.append(1 if re.search(ip_pattern, url) else 0)

    # Feature 3: Count of special characters in URL
    special_chars = re.compile(r'[!@#$%^&*(),?":{}|<>]')
    features.append(len(re.findall(special_chars, url)))

    # Additional features can be added here

    return features


def scrape_urls(site):
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'lxml')
    urls = [a['href'] for a in soup.find_all('a', href=True)]
    return urls


# Load dataset (Replace 'url_dataset.csv' with your dataset)
data = pd.read_csv('url_dataset.csv')

# Extract features
data['features'] = data['url'].apply(extract_features)
X = np.array(data['features'].tolist())
y = data['label']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost classifier
model = XGBClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(classification_report(y_test, y_pred))

# Example URL for testing
url = 'http://example.com'
features = extract_features(url)
print(f"Features for {url}: {features}")

# Example: Scrape URLs from example.com
scraped_urls = scrape_urls('http://example.com')
print("Scraped URLs:", scraped_urls)
