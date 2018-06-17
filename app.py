from flask import *
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "#$%^&*lakw"

mlab.connect()

class Tree(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()
class Buyer(Document):
    name = StringField()
    number = IntField()
    seed = StringField()
    address = StringField()


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        data = Tree.objects()
        return render_template('index.html', items = data)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        number = form['number']
        seed = form['seed']
        address = form['address']
        new_buyer = Buyer(name = name, number = number, seed = seed, address = address)
        new_buyer.save()
        return render_template('complete.html')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']
        new_tree = Tree(title = title, image = image, description = description, price = price)
        new_tree.save()
        # return render_template('add.html')
        return "ok"

if __name__ == '__main__':
  app.run(debug=True)
