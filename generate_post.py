import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_news():
    url = 'https://aws.amazon.com/new/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []

    # Find all news articles
    articles = soup.find_all('li', class_='m-card m-list-card')
    for article in articles:
        title_element = article.find('div', class_='m-card-title')
        if title_element:
            title = title_element.find('a').text.strip()
            link = title_element.find('a')['href']
            news_items.append((title, link))

    return news_items

def create_post(news_items):
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    for i, (title, link) in enumerate(news_items, start=1):
        filename = f'content/posts/{date}-{i}-{title.replace(" ", "-").lower()}.md'
        with open(filename, 'w') as file:
            file.write('+++\n')
            file.write(f'title = "{title}"\n')
            file.write(f'date = {date}\n')
            file.write('draft = false\n')
            file.write(f'description = "{title}"\n')
            file.write('keywords = ""\n')
            file.write('image = ""\n')
            file.write('imageBig = ""\n')
            file.write('categories = ["AWS"]\n')
            file.write('authors = ["Reese Gerjekian"]\n')
            file.write('avatar = "/images/reg-avatar.png"\n')
            file.write('twitter = "https://twitter.com/reg_blog"\n')
            file.write('linkedin = "https://www.linkedin.com/in/rgerjeki/"\n')
            file.write('github = "https://github.com/rgerjeki"\n')
            file.write('instagram = "https://www.instagram.com/rgerjeki/"\n')
            file.write('letterboxd = "https://boxd.it/971m9"\n')
            file.write('facebook = "https://www.facebook.com/rgerjekian/"\n')
            file.write('+++\n\n')
            file.write(f'Read more: [here]({link})')

if __name__ == '__main__':
    news_items = fetch_news()
    create_post(news_items)
