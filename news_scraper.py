#!/usr/bin/env python3
"""
News Headlines Scraper
Scrapes top headlines from BBC News and saves them to a text file.
Uses requests and BeautifulSoup for web scraping.
"""

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os


class NewsHeadlineScraper:
    def __init__(self):
        self.session = requests.Session()
        # Set a user agent to avoid blocking
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.headlines = []
    
    def scrape_bbc_news(self):
        """Scrape headlines from BBC News homepage"""
        url = "https://www.bbc.com/news"
        
        try:
            print(f"Fetching headlines from {url}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # BBC News uses various selectors for headlines
            headline_selectors = [
                'h2[data-testid="card-headline"]',  # Main story cards
                'h3[data-testid="card-headline"]',  # Secondary story cards
                'h2.sc-4fedabc7-3',  # Alternative selector
                'h3.sc-4fedabc7-3',  # Alternative selector
                '.media__title a',    # Media titles
                '.gs-c-promo-heading__title'  # Promo headings
            ]
            
            headlines_found = set()  # Use set to avoid duplicates
            
            for selector in headline_selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline_text = element.get_text(strip=True)
                    if headline_text and len(headline_text) > 10:  # Filter out very short text
                        headlines_found.add(headline_text)
            
            # Convert to list and sort
            self.headlines = sorted(list(headlines_found))
            
            print(f"Successfully scraped {len(self.headlines)} unique headlines")
            return True
            
        except requests.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            return False
        except Exception as e:
            print(f"Error parsing the webpage: {e}")
            return False
    
    def scrape_alternative_source(self):
        """Fallback: Scrape from Reuters as alternative source"""
        url = "https://www.reuters.com"
        
        try:
            print(f"Trying alternative source: {url}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Reuters headline selectors
            headline_selectors = [
                'h3[data-testid="Heading"]',
                '.story-title',
                'h3.text__text__1FZLe',
                'a[data-testid="Heading"]'
            ]
            
            headlines_found = set()
            
            for selector in headline_selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline_text = element.get_text(strip=True)
                    if headline_text and len(headline_text) > 10:
                        headlines_found.add(headline_text)
            
            self.headlines = sorted(list(headlines_found))
            print(f"Successfully scraped {len(self.headlines)} unique headlines from Reuters")
            return True
            
        except Exception as e:
            print(f"Error with alternative source: {e}")
            return False
    
    def save_headlines(self, filename="headlines.txt"):
        """Save headlines to a text file"""
        if not self.headlines:
            print("No headlines to save!")
            return False
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"News Headlines - Scraped on {timestamp}\n")
                file.write("=" * 50 + "\n\n")
                
                for i, headline in enumerate(self.headlines, 1):
                    file.write(f"{i:2d}. {headline}\n")
                
                file.write(f"\n\nTotal headlines: {len(self.headlines)}")
            
            print(f"Headlines saved to '{filename}'")
            return True
            
        except Exception as e:
            print(f"Error saving headlines: {e}")
            return False
    
    def display_headlines(self, limit=10):
        """Display headlines in the console"""
        if not self.headlines:
            print("No headlines available!")
            return
        
        print(f"\n📰 Top {min(limit, len(self.headlines))} Headlines:")
        print("=" * 50)
        
        for i, headline in enumerate(self.headlines[:limit], 1):
            print(f"{i:2d}. {headline}")
        
        if len(self.headlines) > limit:
            print(f"\n... and {len(self.headlines) - limit} more headlines")
    
    def run(self, output_file="headlines.txt", display_limit=10):
        """Main method to run the scraper"""
        print("🔍 Starting News Headlines Scraper...")
        print("-" * 40)
        
        # Try BBC News first
        success = self.scrape_bbc_news()
        
        # If BBC fails, try Reuters
        if not success:
            print("Trying alternative news source...")
            success = self.scrape_alternative_source()
        
        if not success:
            print("❌ Failed to scrape headlines from all sources")
            return False
        
        # Display some headlines
        self.display_headlines(display_limit)
        
        # Save to file
        if self.save_headlines(output_file):
            print(f"\n✅ Scraping completed successfully!")
            print(f"📁 Headlines saved to: {os.path.abspath(output_file)}")
            return True
        else:
            print("❌ Failed to save headlines to file")
            return False


def main():
    """Main function"""
    scraper = NewsHeadlineScraper()
    
    # You can customize the output filename here
    output_filename = "news_headlines.txt"
    
    # Run the scraper
    scraper.run(output_file=output_filename, display_limit=15)


if __name__ == "__main__":
    main()
