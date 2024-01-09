from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'epicemmence@gmail.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'uicf rdpd enff mmvt'  # Update with your password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    email = request.form.get('email')

    # Send welcome email
    msg = Message('Welcome!', sender='epicemmence@gmail.com', recipients=[email])
    msg.html = f'''
        <p>Hi {name},</p>
        <p>Welcome to our platform! Here are your details:</p>
        <ul>
            <li><strong>Name:</strong> {name}</li>
            <li><strong>Address:</strong> {address}</li>
            <li><strong>Phone:</strong> {phone}</li>
            <li><strong>Email:</strong> {email}</li>
        </ul>
        <p>Thank you for signing up!</p>
    '''
    mail.send(msg)
    
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
