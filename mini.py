import os
import html
import xml.etree.ElementTree as ET
import pypandoc
from datetime import datetime
import requests

# RSS 피드 가져오기
feed = requests.get('https://heesang0930.tistory.com/rss')

# 피드를 파일로 저장
with open('feed.xml', 'wb') as f:
    f.write(feed.content)

# 날짜 형식 정의
input_format = "%a, %d %b %Y %H:%M:%S %z"
output_format = "%Y-%m-%d %H:%M:%S %z"

# feed.xml 파싱
root = ET.parse('feed.xml').getroot()
items = root.findall('.//item')

for i, item in enumerate(items):
    title = html.unescape(html.unescape(item.find('title').text))
    link = item.find('link').text
    pubDate = item.find('pubDate').text
    tags = item.findall('category')
    description = item.find('description')
    body = html.unescape(html.unescape(description.text if description is not None else ""))
    body = body.replace("<br>", "\n")

    # 파일 이름 생성
    filename = ''.join(c for c in title.replace(" ", "-").replace("/", "-") if c.isalnum() or c in "-_.")

    # 날짜 파싱
    parsed_date = datetime.strptime(pubDate, input_format)
    formatted_date_string = parsed_date.strftime(output_format)

    # 내용 구성
    content = f"---\ntitle: \"{title}\"\nauthor: heesang\n"
    if "프로그래머스" in title:
        content += "platform: programmers\n"
    elif "백준" in title:
        content += "platform: baekjoon\n"
    else:
        content += "platform: \n"

    content += f"date: {formatted_date_string}\ncategories: [{', '.join(html.unescape(html.unescape(tag.text)) for tag in tags)}]\n"
    content += "tags: [" + ', '.join(f"\"{html.unescape(html.unescape(tag.text))}\"" for tag in tags) + "]\ntoc: true\ncomments: true\n---\n"

    # HTML 파일 생성 및 Markdown 변환
    html_filename = f"{i}.html"
    with open(html_filename, 'w', encoding='utf-8') as file:
        file.write(body)
    output_filename = f"temp_{i}.md"
    pypandoc.convert_file(html_filename, 'md', outputfile=output_filename)

    # Markdown 파일 내용 추가
    with open(output_filename, 'r', encoding='utf-8') as file:
        content += file.read()

    # 최종 Markdown 파일 저장
    post_filename = f"_posts/{parsed_date.strftime('%Y-%m-%d')}-{filename}.md"
    with open(post_filename, 'w', encoding='utf-8') as file:
        file.write(content)

    # 임시 파일 삭제
    os.remove(html_filename)
    os.remove(output_filename)

    print(f"File {post_filename} created successfully.\n")



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
    