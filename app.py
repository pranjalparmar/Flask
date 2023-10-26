from flask import Flask, render_template, url_for, redirect, request, flash
import mysql.connector, re, bcrypt


app = Flask(__name__)

regex1 = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
app.secret_key = 'epJ\xb3^\xc6\xacy\xbd\xdc\xb7]{'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="abodemeals"
)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/product_detail')
def product_detail():
    return render_template('product_detail.html')


@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/result',methods=['POST','GET'])
def result():


    if request.method == "POST":
        signup = request.form
        username=signup['username']
        email=signup['email']
        password=signup['password']
        confirm=signup['confirm']

        mycursor = mydb.cursor()
        mycursor.execute("insert into signup(username,email,password) values(%s,%s,%s)",(username,email,password))
        mydb.commit()
        mycursor.close()
        flash("User Successfully Created" )
        return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)