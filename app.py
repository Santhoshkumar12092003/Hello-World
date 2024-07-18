# from flask import Flask

# #constructor
# app = Flask(__name__)

# #routing,#Methods
# @app.route('/')
# def hello_world():
#     return "Hello World!!!"

# #routing2,#Methods2
# @app.route('/hello')
# def hello():
#     return "Hello Welcome to the Training!!!"

# #routing3,#Methods3 with value
# @app.route('/login/<username>')
# def login_username(username):
#     return f'The username is {username}'
                                                                                                                                                                                                                    
 
# #routing4,#Methods4 with value ID
# @app.route('/login/<int:id>')
# def login():
#     return f' The username is {username}'


# #run
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)