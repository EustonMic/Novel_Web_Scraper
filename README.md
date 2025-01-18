# Web Scraping Novel Reader

This project scrapes novel content from a website and formats it for offline reading. The scraper uses Selenium and BeautifulSoup to fetch, process, and organize the content. The result is a user-friendly HTML file that can be read on devices like the iPad Mini.

## Version 1: Initial Web Scraping Setup
This version sets up the basic web scraping functionality using Selenium WebDriver and BeautifulSoup to scrape novel content from a specified website. The program fetches novel content in chunks by scrolling through the page and then extracts `<p>` tags for processing. The content is then saved into an HTML file.

### Features:
- Initializes a Selenium WebDriver session.
- Scrapes pages incrementally, scrolling until the content is fully loaded.
- Extracts and saves paragraphs of content into an HTML file.

### Requirements:
- Install necessary libraries: `beautifulsoup4`, `selenium`.
- Chrome WebDriver should be installed and available in the system PATH.

---

## Version 2: Filtering Unwanted Content
This version improves the previous setup by filtering out unwanted content from the scraped pages. Specific unwanted phrases such as "翻上頁", "下一頁", "目錄", etc., are excluded from the content. This ensures that only the relevant paragraphs (novel content) are saved.

### Features:
- Filters out unnecessary content by checking paragraph text against a predefined list of unwanted phrases.
- Saves only the relevant novel content into the HTML file.

### Changes from Version 1:
- Added content filtering to exclude navigation, headers, and other irrelevant sections.

---

## Version 3: Multi-Page Scraping
This version adds the ability to scrape multiple pages from the website. The program loops through a specified range of pages and collects content for each page. This allows for scraping a large number of pages efficiently.

### Features:
- Loops through pages, scraping content from each one.
- Automatically increments the page number (`page`) until the end page (`page_end`).
- Saves the content of all pages into a single HTML file.

### Changes from Version 2:
- Added page looping and automatic page incrementing to scrape multiple pages.

---

## Version 4: Enhanced Scrolling for Full Content Load
This version improves the scrolling behavior to ensure the entire page content is loaded before scraping begins. The program now scrolls until the end of the page is reached, ensuring all data is loaded by the browser before scraping.

### Features:
- Scrolls down the page automatically, simulating user behavior to ensure all content is loaded.
- Scrapes content only after the entire page is loaded.

### Changes from Version 3:
- Enhanced page scrolling mechanism for better handling of dynamic content loading.

---

## Version 5: Table of Contents and Styling
This version adds a Table of Contents (ToC) to the scraped content. Each chapter or section is linked in the ToC for easier navigation. Additionally, custom CSS styling is applied to improve the readability and presentation of the content.

### Features:
- Creates a Table of Contents at the beginning of the HTML file.
- Adds anchors to each chapter heading (`<h1>`) and links them in the ToC.
- Applies custom CSS for improved styling and readability.

### Changes from Version 4:
- Added Table of Contents with anchor links for each chapter.
- Applied CSS styles for a cleaner, more readable format.

---

## Final Features:
- Scrapes novel content from multiple pages.
- Filters out unwanted content like page navigation.
- Automatically scrolls pages to load all content before scraping.
- Creates a Table of Contents with clickable links for easy navigation.
- Applies custom CSS styling for an optimized reading experience.

## Requirements:
- Python 3.x
- `beautifulsoup4`, `selenium`
- Chrome WebDriver for Selenium

## Installation:
1. Install required libraries:
   ```bash
   pip install beautifulsoup4 selenium
