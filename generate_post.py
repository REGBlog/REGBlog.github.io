import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_news():
    # URL of the news source
    url = 'https://aws.amazon.com/new/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first news article (you can modify this to fetch more)
    first_article = soup.find('div', {'class': 'lb-txt'})
    title = first_article.find('h3').text.strip()
    description = first_article.find('p').text.strip()

    return title, description

def create_post(title, description):
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    filename = f'content/posts/{date}-{title.replace(" ", "-").lower()}.md'

    with open(filename, 'w') as file:
        file.write('+++\n')
        file.write(f'title = "{title}"\n')
        file.write(f'date = {date}\n')
        file.write('draft = false\n')
        file.write(f'description = "{description}"\n')
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
        file.write(description)  # You can expand this with more content

if __name__ == '__main__':
    title, description = fetch_news()
    create_post(title, description)
