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
while page <= page_end:
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

# Close the WebDriver session
driver.quit()

# Save the content to an HTML file
html_content = "<html>\n<head>\n<meta charset='UTF-8'>\n<title>Web Scraped Content</title>\n</head>\n<body>\n"
html_content += "\n".join(content)
html_content += "\n</body>\n</html>"

# Create a table of contents and style
with open(input_file, "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

style_tag = soup.new_tag("style")
style_tag.string = '''
      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
          Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
        line-height: 1.6;
        padding: 20px;
        max-width: 800px;
        margin: auto;
      }

      h1 {
        font-size: 2em;
        font-weight: bold;
        margin-top: 20px;
      }

      p {
        margin-top: 10px;
        font-size: 1.5em;
        text-align: justify;
      }

      h1:first-of-type {
        margin-top: 0;
      }
'''

soup.head.append(style_tag)

toc_div = soup.new_tag("div", id="table-of-contents")
toc_div.append(soup.new_tag("h2"))
toc_div.h2.string = "Table of Contents"
toc_list = soup.new_tag("ul")

for index, h1 in enumerate(soup.find_all("h1"), start=1):
    h1_id = f"section-{index}"
    h1['id'] = h1_id
    toc_item = soup.new_tag("li")
    toc_link = soup.new_tag("a", href=f"#{h1_id}")
    toc_link.string = h1.get_text()
    toc_item.append(toc_link)
    toc_list.append(toc_item)

toc_div.append(toc_list)

soup.body.insert(0, toc_div)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(str(soup))

print("Table of Contents has been added and saved.")
