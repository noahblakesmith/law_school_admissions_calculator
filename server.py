from flask import Flask, request, render_template,jsonify # Import flask libraries
import pickle
from admissions import predict

# Call pickle files
columns = pickle.load(open('columns.pkl', 'rb'))
logit = pickle.load(open('logit.sav', 'rb'))

# Define relevant variables
schools = [i.strip('school_') for i in list(columns) if 'school_' in i]
years = [i for i in list(columns) if 'year_' in i]

# Initialize the flask class and specify the templates directory
app = Flask(__name__, template_folder="templates")

# Default route set as 'home'
@app.route('/home')
def home():
    return render_template('home.html', schools=[i.title() for i in schools]) # Render home.html




# Route 'classify' accepts GET request
@app.route('/classify',methods=['POST','GET'])
def classify_type():
    try:
        gpa = request.args.get('gpa') # Get parameters for sepal length
        lsat = request.args.get('lsat') # Get parameters for sepal width
        urm = request.args.get('urm') # Get parameters for petal length
        fee_waived = request.args.get('fee_waived') # Get parameters for petal width
        non_trad = request.args.get('non_trad')
        intl = request.args.get('intl')
        school = request.args.get('school').upper()

        # Get the output from the classification logit
        prediction = predict(gpa, lsat, urm, fee_waived, non_trad, intl, school)

        # Render the output in new HTML page
        return render_template('output.html', prediction=prediction, school=school.title())
    except:
        return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)