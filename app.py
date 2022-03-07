from flask import Flask, redirect, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/calculateTax', methods=['GET', 'POST'])
def calculateTax():
    if request.method == 'GET':
        return render_template('calculateTax.html')
    else:
        response = {}
        data = request.get_json()
        if data.get('value0') and data.get('value1', 'value2') and data.get('value3', 'value4') and data.get('value5', 'value6'):
            value0 = data['value0']
            value1 = int(data['value1'])
            value2 = int(data['value2'])
            value3 = int(data['value3'])
            value4 = data['value4']
            value5 = int(data['value5'])
            value6 = data['value6']

            if value1 >= 0 and value2 >= 0 and value3 >= 0:
                gross_income = value1 + value2 + value3
                annual_gross_income = gross_income * 12

            if annual_gross_income:
                if (annual_gross_income * 0.05 > 6000000):
                    positional_fee = 6000000

                else:
                    positional_fee = annual_gross_income * 0.05

            if value4 and value5 >= 0:
                if value4 == 'NM':
                    ptkp = 54000000 + value5 * 4500000

                elif value4 == 'M':
                    ptkp = 58500000 + value5 * 4500000

            regulated_subtractor = positional_fee + ptkp

            taxable_income = annual_gross_income - regulated_subtractor

            num1 = 60000000
            num2 = 250000000
            num3 = 500000000
            num4 = 5000000000

            if taxable_income < 0:
                taxable_income = 0
                annual_tax = 0

            else:
                if taxable_income >= 0 and taxable_income <= num1:
                    annual_tax = taxable_income * 0.05

                elif taxable_income > num1 and taxable_income <= num2:
                    annual_tax = num1 * 0.05 + (taxable_income - num1) * 0.150

                elif taxable_income > num2 and taxable_income <= num3:
                    annual_tax = num1 * 0.05 + (num2 - num1) * 0.15 + (taxable_income - num2) * 0.25

                elif taxable_income > num3 and taxable_income <= num4:
                    annual_tax = num1 * 0.05 + (num2 - num1) * 0.15 + (num3 - num2) * 0.25 + (taxable_income - num3) * 0.3

                elif taxable_income > num4:
                    annual_tax = num1 * 0.05 + (num2 - num1) * 0.15 + (num3 - num2) * 0.25 + (num4 - num3) * 0.3 + (taxable_income - num4) * 0.35
            
            monthly_tax = annual_tax / 12

            if value6:
                if value6 == 'Y':
                    monthly_tax = monthly_tax
                
                elif value6 == 'N':
                    monthly_tax = monthly_tax + monthly_tax * 0.2

            result1 = gross_income
            result2 = annual_gross_income
            result3 = positional_fee
            result4 = ptkp
            result5 = taxable_income
            result6 = annual_tax
            result7 = monthly_tax

            response = {'status': 200, 'result0': value0, 'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4, 'result5': result5, 'result6': result6, 'result7': result7}
        else:
            response = {'status': 500, 'result': 'Error'}
        return jsonify(response)
