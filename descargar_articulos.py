import pandas as pd
import feedparser
import webbrowser
import html
import pprint

# Parser del Diario libre

canales = ['mundo', 'actualidad','revista','planeta','economia','deportes']

posts = []


for canal in canales:

    url = 'https://www.diariolibre.com/feed/' + canal + '.xml'
    feed = feedparser.parse(url)
    if not (feed.entries):
        continue
    feed_title = feed['href']
    feed_entries = feed.entries
    for entry in feed.entries:
        article_title = entry.title
        article_link = entry.link
        article_description = ''
        article_published_at = entry.published 
        summary = html.unescape(entry.summary)
        content = html.unescape(entry.description)
        posts.append((feed_title,article_title, article_link, canal, article_description, article_published_at,summary,content))
        
df = pd.DataFrame(posts, columns=['feed','titulo', 'link', 'seccion', 'descripcion', 'fecha', 'resumen', 'cuerpo']) # pass data to init

df.to_csv('articulos.csv', encoding='utf-8', mode='w')


