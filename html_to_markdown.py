import markdown
import os

reviews = os.listdir('reviews')

for review in reviews:
	with open(f'reviews/{review}', 'r') as file:
		content = file.read()

	with open(review, 'w') as file:
		htmlcontent = markdown.markdown(content)
		file.write(htmlcontent)
