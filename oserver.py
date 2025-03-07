
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'database_name',
    'password': 'titus',
    'database': 'database_name'
}

# Function to connect to the MySQL database
def connect_db():
    return mysql.connecter(**db_config)    
# Serve the registration page
@app.route('/register-page')
def register_page():
    return render_template('registration.html')

# Handle user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password)
        )
        conn.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Serve the login page
@app.route('/login-page')
def login_page():
    return render_template('login.html')

# Handle user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    try:
        # Query to find the user by email
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()  # Fetch the result of the query

        # If the user exists and the password is correct
        if user and check_password_hash(user['password'], password):
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'error': 'Invalid credentials!'}), 401
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/marketplace')
def marketplace():
    return render_template('market.html')  

if __name__ == '__main__':
    app.run(debug=True)
