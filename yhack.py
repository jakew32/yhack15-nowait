from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('trucks/<truck_id>')
def get_truck_menu(truck_id):
    return "truck info"

@app.route('order/<item_id>')
def place_order(item_id):
    return "ordering"




if __name__ == '__main__':
    app.run()
