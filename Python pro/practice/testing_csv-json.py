import json, csv
books = [{'Title': 'Title1', 'Author': 'Author1', 'Pages': 15},
        {'Title': 'Title2', 'Author': 'Author2', 'Pages': 377},
        {'Title': 'Title3', 'Author': 'Author3', 'Pages': 743},
        {'Title': 'Title4', 'Author': 'Author4', 'Pages': 26732},
        {'Title': 'Title5', 'Author': 'Author5', 'Pages': 226},
]
with open('books.json', 'w') as file:
    json.dump(books, file)
big_books = []
with open('books.json', 'r') as file:
    reader = json.load(file)
    for book in reader:
        if book['Pages'] > 300:
            big_books.append(book)
            print(book)

with open('big_books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author', 'Pages'])  # Заголовок

    for book in big_books:
        writer.writerow([book['Title'], book['Author'], book['Pages']])