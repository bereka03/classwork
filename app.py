from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Lecture14'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f'Book title:{self.title}; Author: {self.author}; Price: {self.price}'


# b1 = Books.query.first()
# print(b1)
# all_books = Books.query.all()
# print(all_books)
# for each in all_books:
#     print(each)
# all_books = Books.query.filter_by(author='William Shakespeare').all()
# for each in all_books:
#     print(each)
# b1 = Books(title='ლექსების კრებული', author='ლადო ასათიანი', price=10)
# db.session.add(b1)
# db.session.commit()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('login.html')



@app.route('/user')
def user():
    subjects = ['Python', 'Calculus', 'DB']
    return render_template('user.html',  subjects=subjects)


@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method=='POST':
        t = request.form['title']
        a = request.form['author']
        p = request.form['price']
        b1 = Books(title=t, author=a, price=float(p))
        db.session.add(b1)
        db.session.commit()
        return 'მონაცემები დამატებულია'

    return render_template('books.html')


if __name__ == "__main__":
    app.run(debug=True)