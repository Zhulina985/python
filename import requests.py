import requests
import re

url = 'https://blog.csdn.net/qq_17275369/article/details/147990855?ops_request_misc=&request_id=&biz_id=102&utm_term=python%E6%80%8E%E4%B9%88%E5%AF%BC%E5%8C%85&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~sobaiduweb~default-0-147990855.nonecase&spm=1018.2226.3001.4450'  # 替换为你要爬取的页面地址

response = requests.get(url)
html = response.text

# 使用正则表达式提取所有数字
numbers = re.findall(r'\d+', html)

print(numbers)