from flask import Flask,jsonify,render_template,json
app=Flask(__name__)
app.register_blueprint
with open('data.json') as json_file:
    data = json.load(json_file)


@app.route('/customers')
def get_customers():
    customers = data['customers']
    if len(customers)==0:
        return ({'error': 'Order not found'})
    return render_template("customers.html", customers=customers)

@app.route('/customers/<int:id>')
def getcustomer(id):
    customer=[customer for customer in data['customers'] if customer['id']==id]
    if len(customer)==0:
        return ({'error': 'Order not found'})
    return render_template("customer.html",customer=customer)

@app.route('/customers/<int:id>/orders')
def get_orders(id):
    customer_orders = [order for order in data['orders'] if order['customer_id'] == id]
    if len(customer_orders)==0:
        return ({'error': 'Order not found'})
    return render_template("orders.html",customer_orders=customer_orders)

@app.route('/customers/<int:customer_id>/orders/<int:order_id>')
def get_order(customer_id, order_id):
    order = [order for order in data['orders'] if order['customer_id'] == customer_id and order['id'] == order_id]
    if len(order)==0:
        return ({'error': 'Order not found'})
    return render_template("order.html",customer_order=order)




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)
