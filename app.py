from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['PERMANENT_SESSION_LIFETIME'] = 30 * 24 * 60 * 60  # 30 days



# Database configuration
database_url = os.environ.get('DATABASE_URL', 'sqlite:///ngl.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient_handle = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)



@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['handle'] = user.handle
            session.permanent = True
            flash('Logged in successfully! Welcome back.', 'success')
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid email or password.')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        handle = request.form.get('handle', '').strip().lower()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        
        if not handle or not email or not password:
            return render_template('register.html', error='Please fill all fields.')
        
        if User.query.filter_by(handle=handle).first():
            return render_template('register.html', error='Handle already taken.')
        
        if User.query.filter_by(email=email).first():
            return render_template('register.html', error='Email already registered.')
        
        hashed_password = generate_password_hash(password)
        user = User(handle=handle, email=email, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        session['handle'] = user.handle
        session.permanent = True
        flash('Account created successfully! Welcome to Ghost NGL.', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('landing'))
    
    handle = session['handle']
    user_messages = Message.query.filter_by(recipient_handle=handle).order_by(Message.timestamp.desc()).all()
    
    # Mark all messages as read
    for message in user_messages:
        if not message.is_read:
            message.is_read = True
    db.session.commit()
    
    return render_template('dashboard.html', handle=handle, messages=user_messages)

@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user_id' not in session:
        return redirect(url_for('landing'))
    
    handle = session['handle']
    # Delete messages and user
    Message.query.filter_by(recipient_handle=handle).delete()
    User.query.filter_by(handle=handle).delete()
    db.session.commit()
    
    session.clear()
    return redirect(url_for('landing'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get('password', '')
        if password == os.environ.get('ADMIN_PASSWORD', 'admin123'):  # Change in production
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('admin.html', error='Invalid password.')
    
    if not session.get('admin'):
        return render_template('admin.html')
    
    total_users = User.query.count()
    users_list = User.query.all()
    return render_template('admin.html', total_users=total_users, users=users_list, logged_in=True)



@app.route('/message-sent')
def message_sent():
    return render_template('message_sent.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing'))

@app.route('/api/unread-count')
def unread_count():
    if 'user_id' not in session:
        return {'count': 0}, 401
    user = User.query.get(session['user_id'])
    count = Message.query.filter_by(recipient_handle=user.handle, is_read=False).count()
    return {'count': count}

@app.route('/health')
def health():
    return {'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()}, 200

@app.route('/message/<int:message_id>')
def view_message(message_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    message = Message.query.filter_by(id=message_id, recipient_handle=user.handle).first()
    if not message:
        return redirect(url_for('dashboard'))
    
    # Mark as read
    message.is_read = True
    db.session.commit()
    
    return render_template('view_message.html', message=message, handle=user.handle)

@app.route('/u/<username>', methods=['GET', 'POST'])
def send_page(username):
    username = username.lower()
    user = User.query.filter_by(handle=username).first()
    if not user:
        return render_template('send_page.html', error='User not found.', username=username)
    
    if request.method == 'POST':
        content = request.form.get('message', '').strip()
        if not content:
            return render_template('send_page.html', error='Please enter a message.', username=username)
        
        # Save message without any sender data
        message = Message(recipient_handle=username, content=content)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('message_sent'))
    
    return render_template('send_page.html', username=username)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)