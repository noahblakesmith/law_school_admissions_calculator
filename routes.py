# Setup
from flask import Flask, request, render_template, jsonify
import pickle
from admissions import predict

app = Flask(__name__, template_folder="templates")

# Call pickle files
columns = pickle.load(open('columns.pkl', 'rb'))
logit = pickle.load(open('logit.sav', 'rb'))

# Define relevant variables
schools = [i.strip('school_') for i in list(columns) if 'school_' in i]
years = [i for i in list(columns) if 'year_' in i]

# Set default input route
@app.route('/input')
def input():
    return render_template('input.html', schools=[i.title() for i in schools])

# Define output route
@app.route('/output', methods=['POST', 'GET'])
def output():

    try:

        # Define arguments
        gpa = request.args.get('gpa')
        lsat = request.args.get('lsat')
        urm = request.args.get('urm')
        fee_waived = request.args.get('fee_waived')
        non_trad = request.args.get('non_trad')
        intl = request.args.get('intl')
        school = request.args.get('school').upper()

        # Generate prediction for user
        prediction = predict(gpa, lsat, urm, fee_waived, non_trad, intl, school)
        return render_template('output.html', prediction=prediction, school=school.title())
    
    except:

        return 'Error. Please fill in all fields on previous page.'

if(__name__=='__main__'):
    app.run(debug=True)