import json
import os

with open('data.json', 'r') as file:
    data = json.load(file)

with open('links.txt', 'r') as file:
    links = file.readlines()

ids = [link.replace('https://amazon.com/dp/', '') for link in links]
ids = [link.replace('\n', '') for link in ids]
files = [link + '.txt' for link in ids]

for i, f in enumerate(files):

    print(f)

    img_tag = f'<img src="{data[i]["product_image_url"]}" alt="Product image" />'

    with open(f'reviews/{f}', 'r') as file:
        content = file.read()
    
    content = img_tag + content

    with open(f'reviews/{f}', 'w') as file:
        file.write(content)
    
    print(f'Inserted image in {f}')