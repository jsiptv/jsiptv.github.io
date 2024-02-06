import requests
from github import Github

# 定义要获取的文档地址列表
document_urls = [
    'https://git.iptv-cn.tk/https://raw.githubusercontent.com/jsiptv/jsiptv.github.io/main/TV/v6.txt',
    'https://git.iptv-cn.tk/https://raw.githubusercontent.com/jsiptv/tv/main/itvlist.txt'
]

# 创建一个空字符串，用于保存所有文档内容
all_document_content = ''

# 循环遍历文档地址列表，逐个获取文档内容并拼接到 all_document_content 中
for url in document_urls:
    response = requests.get(url)
    if response.status_code == 200:
        document_content = response.text
        all_document_content += document_content + '\n'

# 将合并后的文档内容写入到 all.txt 文件中
with open('all.txt', 'w') as file:
    file.write(all_document_content)

# 使用 PyGithub 库将 all.txt 文件提交到 GitHub 主分支
g = Github("<YOUR_GITHUB_ACCESS_TOKEN>")
repo = g.get_repo("jsiptv/jsiptv.github.io")
repo.create_file("all.txt", "commit message", all_document_content, branch="main")




