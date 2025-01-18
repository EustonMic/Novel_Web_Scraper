from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Initialize WebDriver and parameter
driver = webdriver.Chrome()
content = []

# Setup parameters
page = 10691
page_end = 10713
scroll_time_setting = 3
input_file = "scraped_content.html"
output_file = "scraped_output.html"

# Unwanted texts to filter
unwanted_texts = ["翻上頁", "呼出功能", "翻下頁", "上一頁", "目錄", "書頁", "下一頁", "背景", "字體", "章評", "插圖"]

# Loop through pages
while True:
    # Open the URL of the webpage
    url = f"https://tw.linovelib.com/novel/73/{page}.html"
    driver.get(url)

    # Scroll the page
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1
    while True:
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_time_setting)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if screen_height * i > scroll_height:
            break

    # Fetch data using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    paragraphs = soup.select("p")

    # Filter out unwanted paragraphs
    filtered_paragraphs = [p for p in paragraphs if not any(text in p.get_text() for text in unwanted_texts)]

    # Save the page content
    title = soup.select_one("title").get_text()
    page_content = f"<h1>{title}</h1>\n"
    page_content += "\n".join([str(p) for p in filtered_paragraphs])

    content.append(f"<h2>{title}</h2>\n{page_content}\n<hr>")

    # Increment page number
    page += 1
    if page > page_end:
        break

# Close the WebDriver session
driver.quit()

# Save the content to an HTML file
html_content = "<html>\n<head>\n<meta charset='UTF-8'>\n<title>Web Scraped Content</title>\n</head>\n<body>\n"
html_content += "\n".join(content)
html_content += "\n</body>\n</html>"

with open(input_file, "w", encoding="utf-8") as file:
    file.write(html_content)
