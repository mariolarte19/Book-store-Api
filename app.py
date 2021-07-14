  
from flask import Flask, jsonify, request

app = Flask(__name__)

from books import books

# Get Books

@app.route('/books',methods=['GET'])
def getBooks():
    return jsonify({'books': books})



@app.route('/books/<string:book_name>')
def getBook(book_name):
    booksFound = [
        book for book in books if book['name'] == book_name.lower()]
    if (len(booksFound) > 0):
        return jsonify({'book': booksFound[0]})
    return jsonify({'message': 'Book Not found'})

# Add Book 

@app.route('/books', methods=['POST'])
def addBook():
    new_book = {
        'name': request.json['name'],
        'price': request.json['price'],
        'autor': request.json['autor'],
    }
    books.append(new_book)
    return jsonify({'books': books})

#Delete Book

@app.route('/books/<string:book_name>', methods=['DELETE'])
def deleteBook(book_name):
    booksFound = [book for book in books if book['name'] == book_name]
    if len(booksFound) > 0:
        books.remove(booksFound[0])
        return jsonify({
            'message': 'Book Deleted',
            'books': books
        })


# Update Book

@app.route('/books/<string:book_name>', methods=['PUT'])
def editBook(book_name):
    booksFound = [book for book in books if book['name'] == book_name]
    if (len(booksFound) > 0):
        booksFound[0]['name'] = request.json['name']
        booksFound[0]['price'] = request.json['price']
        booksFound[0]['autor'] = request.json['autor']
        return jsonify({
            'message': 'Book Updated',
            'book': booksFound[0]
        })
    return jsonify({'message': 'book Not found'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)

