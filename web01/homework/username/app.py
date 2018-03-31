from flask import Flask
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    user_list = {
        "user1" : {
                    "name" : "Nguyen Van A",
                    "gender" : "Male",
                    "age" : 20,
                    },
        "user2" : {
                    "name" : "Nguyen Thi B",
                    "gender" : "Female",
                    "age" : 18,
                    },

    }

    if username in user_list:
         username = str(user_list[username])
    else:
         username = "User not found"
    return username

if __name__ == '__main__':
  app.run(debug=True)
