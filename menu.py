import os
from flask import Flask, request, flash, jsonify, render_template, redirect
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField, FloatField
from datetime import datetime , date 
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'

mysql = MySQL(app)
# login apis
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == 'useradmin@gmail.com' and password == '1234':
        # Login successful
        return redirect('/dashboard')
    else:
        # Login failed
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    # Render the dashboard page after successful login
    return render_template('dashboard.html')

# menuu apis

class MenuForm(Form):
    item_name = StringField('item_name', [validators.InputRequired()])
    price = FloatField('price', [validators.InputRequired()])
    description = StringField('description', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)


@app.route('/add_menu', methods=['POST'])
def add_menu():
    form = MenuForm(request.form)
    if form.validate():
        item_name = form.item_name.data
        price = form.price.data
        description = form.description.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO menu(item_name, price, description, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)", (item_name, price, description, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return render_template('dashboard.html')
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/menu/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM menu WHERE id=%s", (menu_id,))
    menu = cur.fetchone()
    cur.close()
    if menu:
        response = {'code': '200', 'status': 'true', 'data': menu}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'menu not found'}
        return jsonify(response)


@app.route('/menu', methods=['GET'])
def get_all_menus():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM menu")
    menus = cur.fetchall()
    cur.close()
    response = { "data" : menus }
    return jsonify(response)
    # return render_template('dashboard.html', menu = menus)



@app.route('/del_menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    cur = mysql.connection.cursor()
    menu = cur.execute(f"DELETE FROM menu WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if menu > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'menu found', 'data': menu}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'menu not found', 'data': menu}
        return jsonify(final_response)


@app.route('/upd_menu/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    form = MenuForm(request.form)
    if form.validate():
        item_name = form.item_name.data
        price = form.price.data
        description = form.description.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM menu WHERE id=%s", (menu_id,))
        menu = cur.fetchone()
        if not menu:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'menu not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE menu SET item_name=%s, price=%s, description=%s, updated_at=%s WHERE id=%s", (item_name, price, description, updated_at, menu_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'menu updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


# User APIS

class UserForm(Form):
    name = StringField('Name', [validators.InputRequired()])
    role = StringField('Role', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)
    
@app.route('/add_user', methods=['POST'])
def add_user():
    form = UserForm(request.form)
    if form.validate():
        name = form.name.data
        role = form.role.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(name, role, created_at, updated_at) VALUES(%s, %s, %s, %s)", (name, role, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return render_template('dashboard.html')
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE id=%s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        response = {'code': '200', 'status': 'true', 'data': user}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'user not found'}
        return jsonify(response)

@app.route('/user', methods=['GET'])
def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': users}
    return jsonify(response)

@app.route('/del_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    user = cur.execute(f"DELETE FROM user WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if user > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'user found', 'data': user}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'user not found', 'data': user}
        return jsonify(final_response)


@app.route('/upd_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    form = UserForm(request.form)
    if form.validate():
        name = form.name.data
        role = form.role.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE id=%s", (user_id,))
        user = cur.fetchone()
        if not user:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'user not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE user SET name=%s, role=%s, updated_at=%s WHERE id=%s", (name, role, updated_at, user_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'user updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)

# Customer Apis
class CustomerForm(Form):
    user_id = IntegerField('Name', [validators.InputRequired()])
    phone = IntegerField('Role', [validators.InputRequired()])
    address = StringField('address', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)
    
@app.route('/add_customer', methods=['POST'])
def add_customer():
    form = CustomerForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        phone = form.phone.data
        address = form.address.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer(user_id, phone, address, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)", (user_id, phone, address, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return render_template('dashboard.html')
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer WHERE id=%s", (customer_id,))
    customer = cur.fetchone()
    cur.close()
    if customer:
        response = {'code': '200', 'status': 'true', 'data': customer}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'customer not found'}
        return jsonify(response)

@app.route('/customer', methods=['GET'])
def get_all_customers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer")
    customers = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': customers}
    return jsonify(response)

@app.route('/del_customer/<int:user_id>', methods=['DELETE'])
def delete_customer(user_id):
    cur = mysql.connection.cursor()
    customer = cur.execute(f"DELETE FROM customer WHERE user_id={user_id}")
    mysql.connection.commit()
    cur.close()
    if customer > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'customer found', 'data': customer}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'customer not found', 'data': customer}
        return jsonify(final_response)


@app.route('/upd_customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    form = CustomerForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        phone = form.phone.data
        address = form.address.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM customer WHERE id=%s", (customer_id,))
        customer = cur.fetchone()
        if not customer:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'customer not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE customer SET  user_id=%s, phone=%s, address=%s, updated_at=%s WHERE id=%s", (user_id, phone, address, updated_at, customer_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'customer updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
