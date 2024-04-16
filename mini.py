from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from datetime import datetime

import html
import xml.etree.ElementTree as ET

from time import sleep
import requests
#<!------------------RSS-----------------!>#
feed = requests.get('https://heesang0930.tistory.com/rss')

## feed를 html로 변환해서 저장
with open('feed.xml', 'wb') as f:
    f.write(feed.content)

# 입력 형식 정의
input_format = "%a, %d %b %Y %H:%M:%S %z"

# 출력 형식 정의
output_format = "%Y-%m-%d %H:%M:%S %z"

## feed.xml을 파싱
root = ET.parse('feed.xml')

items = root.findall('.//item')



for item in items[20:22]:
    title = item.find('title').text
    link = item.find('link').text
    pubDate = item.find('pubDate').text
    tags = item.findall('category')
    
    title = html.unescape(html.unescape(title))
    print(f"Title: {title}")
    if title.startswith("["):
        file_title = title[title.index("]")+1:]
    filename = title.replace(" ", "-").replace("/", "-")
    # 유효하지 않은 파일 이름 문자 제거
    filename = ''.join(c for c in filename if c.isalnum() or c in "-_.")
    print(f"Link: {link}")
    
    parsed_date = datetime.strptime(pubDate, input_format)
    formatted_date_string = parsed_date.strftime(output_format)
    print(f"Published Date: {formatted_date_string}")
    
    print("Tags: ")
    for tag in tags:
        print(html.unescape(html.unescape(tag)).text)
    content = "---\n"
    content += f"title: {file_title}\n"
    content += "author: heesane\n"
    if "프로그래머스" in title:
        content += "platform: programmers\n"
        content += "level: "
        temp_title = title.split()
        for i in range(len(temp_title)):
            if temp_title[i] == "Level":
                content += f"Level {temp_title[i+1]}\n"
        
    elif "백준" in title:
        content += "platform: baekjoon\n"
        content += "level: \n"
        temp_title = title.split()
        for i in range(len(temp_title)):
            if temp_title[i] == "[백준]":
                content += f"{temp_title[i+1]}\n"
        
    content += f"date: {formatted_date_string}\n"
    content += f"categories: [\n"
    content += f"\t{html.unescape(html.unescape(tags[0].text))}\n"
    content += f"]\n"
    content += "tags: [\n"
    for tag in tags:
        content += f"\t{html.unescape(html.unescape(tag.text))},\n"
    content += "]\n"
    content += "toc: true\n"
    content += "comments: true\n"
    content += "---\n"
    # 파일 쓰기
    with open(filename+".md", 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"File {title} created successfully.")



#<!------------------Selenium-----------------!>#
# chrome_options = Options()
# chrome_options.add_argument("--start-fullscreen")

# driver = webdriver.Chrome(options=chrome_options)

# driver.implicitly_wait(3)

# driver.get(url='https://markdowndown.vercel.app')
# my_blog_base_url = 'https://heesang0930.tistory.com/'
# input_area = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]/input')
# button_area = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]/button')
# for i in range(1,47):
#     input_area.clear()
#     input_area.send_keys(my_blog_base_url + str(i))
    
#     sleep(1)
    
#     button_area.click()
    
#     while button_area.text != 'Convert':
#         sleep(1)
    
#     temp_file = '/Users/heesang/Downloads/' + str(i) + '.md'
    