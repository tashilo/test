
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

key = "ocean" 
letter_case = None 

def find_articles(key, letter_case=False):
    found_articles = []
    for article in articles_dict:
        if letter_case:
            if key in article['title'] or key in article['author']:
                found_articles.append(article)
        else:
            if key.lower() in article['title'].lower() or key.lower() in article['author'].lower():
                found_articles.append(article)

# форматируем результат с помощью методом join 
    output = "\n".join([
        f"{article['title']}, {article['author']}, {article['year']}" 
        for article in found_articles
    ])
    return output




print(find_articles(key, letter_case))

