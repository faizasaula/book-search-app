import scrapy
import json

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        books = response.css('article.product_pod')
        data = []

        for book in books:
            title = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            availability = book.css('p.instock.availability::text').re_first('\S+')
            rating = book.css('p.star-rating::attr(class)').re_first('star-rating (\w+)')
            link = book.css('h3 a::attr(href)').get()
            full_link = response.urljoin(link)

            data.append({
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating,
                'link': full_link
            })

        # Simpan hasil scraping ke file JSON
        with open('data/books.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
