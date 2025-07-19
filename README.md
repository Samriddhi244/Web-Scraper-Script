# News Headlines Scraper

A Python web scraper that extracts top headlines from news websites using requests and BeautifulSoup.

## Features

- Scrapes headlines from BBC News (primary source)
- Fallback to Reuters if BBC is unavailable
- Removes duplicate headlines
- Saves headlines to a text file with timestamp
- Displays top headlines in the console
- Handles errors gracefully with proper exception handling

## Requirements

- Python 3.6+
- requests
- beautifulsoup4
- lxml (for better parsing performance)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests beautifulsoup4 lxml
```

## Usage

### Basic Usage

Run the scraper with default settings:
```bash
python news_scraper.py
```

This will:
- Scrape headlines from BBC News
- Display the top 15 headlines in the console
- Save all headlines to `news_headlines.txt`

### Customization

You can modify the `main()` function in `news_scraper.py` to:
- Change the output filename
- Adjust the number of headlines displayed
- Add more news sources

### Example Output

The scraper will create a text file like this:

```
News Headlines - Scraped on 2025-07-19 14:30:25
==================================================

 1. Breaking: Major political development announced
 2. Technology sector sees significant growth
 3. Climate change summit reaches new agreement
 ...

Total headlines: 25
```

## Error Handling

The scraper includes robust error handling:
- Network timeouts and connection errors
- HTML parsing errors
- File writing errors
- Fallback to alternative news sources

## Notes

- The scraper uses a realistic User-Agent to avoid being blocked
- It respects website structure and doesn't overload servers
- Headlines are deduplicated to avoid repetition
- Timestamps are included in the output file

## Legal Considerations

This scraper is for educational purposes. Always:
- Respect robots.txt files
- Don't overload servers with requests
- Follow the terms of service of websites
- Consider rate limiting for production use

## Troubleshooting

If the scraper fails:
1. Check your internet connection
2. Verify that the target websites are accessible
3. The scraper includes fallback sources
4. Website structures may change - selectors might need updates
