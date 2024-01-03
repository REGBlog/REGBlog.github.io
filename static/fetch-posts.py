# update_readme.py
import feedparser

# Fetch the RSS feed
feed = feedparser.parse('https://www.reg-blog.com/index.xml')

# Extract the desired data (e.g., the latest 5 posts)
posts = feed.entries[:5]

# Format the posts into Markdown
markdown_content = '\n'.join([f"- [{post.title}]({post.link})" for post in posts])

# Read the existing README
with open('README.md', 'r') as file:
    readme_contents = file.read()

# Replace the blog posts section
updated_readme = re.sub(r'<!-- BLOG-POST-LIST:START -->(.*?)<!-- BLOG-POST-LIST:END -->', 
                        f'<!-- BLOG-POST-LIST:START -->\n{markdown_content}\n<!-- BLOG-POST-LIST:END -->', 
                        readme_contents, 
                        flags=re.DOTALL)

# Write back the updated README
with open('README.md', 'w') as file:
    file.write(updated_readme)
