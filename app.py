import requests
from bs4 import BeautifulSoup

def scrape_article_links(urls):
    """Scrapes a list of urls to find article links."""
    article_links = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links on the page
        links = [link.get('href') for link in soup.find_all('a')]
        
        # Filter out links that don't belong to articles
        for link in links:
            # Check if the link has a certain keyword in it (e.g. "article")
            if "article" in link:
                article_links.append(link)

    return article_links

def main():
    urls = ["https://www.example.com/landing1", "https://www.example.com/landing2"]
    article_links = scrape_article_links(urls)

    # Store the results in a text file
    with open("article_links.txt", "w") as f:
        for link in article_links:
            f.write(link + "\n")

if __name__ == "__main__":
    main()
