# Flask_Api
Run the following commands

docker build -t flask-app .    
docker run -p 5001:5001 flask-app

#Get methods

http://127.0.0.1:5001/customers - displays all  the customers details

http://127.0.0.1:5001/customers/1 -displays the customer with id=1

http://127.0.0.1:5001/customers/1/orders - displays all orders with the customer id=1

http://127.0.0.1:5001/customers/1/orders/1  - display the customer with id=1 and order id=1

