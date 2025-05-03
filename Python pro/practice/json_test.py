import json
students = [
    {"name": "Alice", "age": 22, "city": "New York"},
    {"name": "Bob", "age": 24, "city": "San Francisco"},
    {"name": "Charlie", "age": 21, "city": "Chicago"}
]

with open('students.json', 'w') as file:
    data = json.dump(students, file)

with open('students.json', 'r') as file:
    print(json.load(file))


import csv
products = [["Product", "Price"],
        ["Banana", 130],
        ["Apple", 25],
        ["Potato", 15],
        ["Tomato", 21],
        ["Mango", 256]]

with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(products)
    
with open('products.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовок ("Product", "Price")
    for row in reader:
        product, price = row
        if int(price) > 100:
            print(product)