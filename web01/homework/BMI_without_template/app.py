from flask import Flask
app = Flask(__name__)

@app.route('/bmi1/<int:weight>/<int:height>')
def bmi(weight, height):
    bmi = weight/(height/100)**2
    if bmi < 16:
        condition = "BMI < 16 : Severely underweight"
    elif bmi <18.5:
        condition = "16 <= BMI < 18.5 : Underweight"
    elif bmi < 25:
        condition = "18.5 <= BMI < 25 : Normal"
    elif bmi < 30:
        condition = "25 <= BMI < 30 : Overweight"
    else:
        condition = "BMI > 30 : Obese"

    return condition


if __name__ == '__main__':
  app.run(debug=True)
