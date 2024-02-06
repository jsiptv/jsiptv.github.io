import requests

def get_document(url):
    response = requests.get(url)
    return response.text

def merge_documents(urls, output_file):
    with open(output_file, 'w') as file:
        for url in urls:
            document = get_document(url)
            file.write(document + '\n')

# 指定要获取的文档地址列表
document_urls = [
    'https://example.com/document1.txt',
    'https://example.com/document2.txt',
    'https://example.com/document3.txt'
]

# 合并文档并保存为'all.txt'
output_file = 'all.txt'
merge_documents(document_urls, output_file)

print("Merge completed. The merged document is saved as 'all.txt'.")
