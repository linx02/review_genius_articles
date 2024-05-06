import os

files = os.listdir('reviews')
ids = [file[:-4] for file in files]
urls = [f'https://amazon.com/dp/{id}\n' for id in ids]

with open('links.txt', 'w') as f:
	f.writelines(urls)
