from flask import request

from manage import app
users = []

orders = []


class User:
    def __init__(self,user_id,user_name,user_email,user_password,user_address,confirm_password):
        self.user_id =user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_address = user_address
        self.confirm_password = confirm_password

class Order:
    def __init__(self,parcel_name,parcel_weight,parcel_description,parcel_price,pickup,destination,status):
        self.order_id = len(orders)+1
        self.parcel_name = parcel_name
        self.parcel_weight = parcel_weight
        self.parcel_description = parcel_description
        self.parcel_price = parcel_price
        self.pickup = pickup
        self.destination = destination
        self.status = status


