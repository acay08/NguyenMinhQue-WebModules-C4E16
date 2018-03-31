from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi2/<int:weight>/<int:height>')
def bmi(weight, height):
    bmi = weight/(height/100)**2
    return render_template('index.html', weight = weight, height = height, bmi = bmi)

if __name__ == '__main__':
  app.run(debug=True)
