def scrape_news_site():
    scraper = WebScraper(base_url="https://www.theguardian.com/technology/2012/aug/04/50-best-apps-chidren-smartphones-tablets")
    
    # Селекторы для новостного сайта
    selectors = {
        'headline': 'h1.article-headline',
        'author': '.author-name',
        'date': '.article-date',
        'content': '.article-content p',
        'tags': '.tags a'
    }
    
    # Собираем данные с главной страницы
    html = scraper.fetch_page("https://www.theguardian.com/technology/2012/aug/04/50-best-apps-chidren-smartphones-tablets")
    soup = BeautifulSoup(html, 'html.parser')
    
    # Находим ссылки на статьи
    article_links = []
    for article in soup.select('.article-preview a'):
        link = urljoin("https://www.theguardian.com/technology/2012/aug/04/50-best-apps-chidren-smartphones-tablets", article['href'])
        article_links.append(link)
    
    # Собираем данные со статей
    all_articles = []
    for link in article_links[:5]:  # Ограничиваем 5 статьями для примера
        article_data = scraper.scrape_page(link, selectors)
        article_data['article_url'] = link
        all_articles.append(article_data)
        print(f"Собрана статья: {article_data.get('headline', [''])[0]}")
    
    return all_articles
