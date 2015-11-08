from flask import Flask, request, render_template
import braintree, random
import yhackconfig

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/order/')
def place_order():
    clienttoken = braintree.ClientToken.generate()
    amount = request.args.get('amt')
    item = request.args.get('item')

    return render_template("payment.html", amount=amount, item=item, clienttoken=clienttoken)


@app.route('/trucks/3/')
def get_truck_menu3():
    return render_template("3.html")

@app.route('/trucks/5/')
def get_truck_menu3():
    return render_template("5.html")

@app.route('/trucks/6/')
def get_truck_menu3():
    return render_template("6.html")

@app.route('/checkout/', methods=['POST'])
def checkout():

    result = braintree.Transaction.sale({
        "amount": request.args.get('amount'),
        "payment_method_nonce": request.args.get("payment_method_nonce"),
        "options": {
            "submit_for_settlement": True
        }
    })

    if result.is_success:
        number = random.randrange(1, 999)
        return render_template("checkout.html", number=number)

    else:
        return "error"





if __name__ == '__main__':
    app.run('0.0.0.0')
