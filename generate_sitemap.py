import os

files = os.listdir('reviews')

with open('sitemap.xml', 'w') as file:
    file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    file.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for f in files:
        file.write(f'<url>\n')
        file.write(f'<loc>https://reviewer-guru.com/review/{f[:-4]}</loc>\n')
        file.write(f'<changefreq>monthly</changefreq>\n')
        file.write(f'<priority>0.7</priority>\n')
        file.write(f'</url>\n')

    file.write('</urlset>')