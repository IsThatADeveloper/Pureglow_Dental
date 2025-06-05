from main import app
import os

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    


# Decryption:
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt()
# bcrypt.generate_password_hash('test')
# bcrypt.generate_password_hash('test').decode('utf-8')
# hashed_pw = bcrypt.generate_password_hash('test').decode('utf-8')
# bcrypt.check_password_hash(hashed_pw, 'password')  #(Result FALSE)
# bcrypt.check_password_hash(hashed_pw, 'test')  #(Result TRUE)