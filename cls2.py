from flask import Flask, jsonify
app = Flask(__name__)

# app.route('/store',) is default get request if you want to change it to put request u need to change that 
#Post - receive data
#Get - send data back only
stores = [
    {
        'name' : 'My Store',
        'items' : [
            {
            'name' : 'My Item',
            'price' : 16.99
            }
        ]
    }
]
# Post /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    pass
# Get /store<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass
# Get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})
# Post /store/<string:name>/istem {name:,price:}
@app.route('/store/<string:name>/item',methods = ['POST'])
def create_items_in_store(name):
    pass
# Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass
app.run(port=5001)