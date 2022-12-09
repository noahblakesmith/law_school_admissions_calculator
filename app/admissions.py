# Importing necessary libraries
import pandas as pd
import numpy as np
import pickle

# Call pickle files
columns = pickle.load(open('/Users/nbs/Documents/Georgetown/Semester 5/1 Courses/OPIM 244/columns.pkl', 'rb'))
logit = pickle.load(open('/Users/nbs/Documents/Georgetown/Semester 5/1 Courses/OPIM 244/logit.sav', 'rb'))

# Define relevant variables
schools = [i.strip('school_') for i in list(columns) if 'school_' in i]
years = [i for i in list(columns) if 'year_' in i]

def predict(a, b, c, d, e, f, g):

    user = pd.DataFrame(

        np.array(

            [0 if i=='NO' else 1 if i=='YES' else i for i in [a, b, c, d, e, f]]
            + [1 if i=='year_2023' else 0 for i in years]
            + [1 if i==g else 0 for i in schools]
        
        ).reshape(1, -1), 

        columns=columns[1:]
    )

    prediction = int(100 * logit.predict_proba(user).flatten()[1])
    return prediction









'''
# Importing the dataset
data = pd.read_csv('./iris.csv')

# Dictionary containing the mapping
variety_mappings = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

# Encoding the target variables to integers
data = data.replace(['Setosa', 'Versicolor' , 'Virginica'],[0, 1, 2])

X = data.iloc[:, 0:-1] # Extracting the independent variables
y = data.iloc[:, -1] # Extracting the target/dependent variable

logreg = LogisticRegression(max_iter=1000) # Initializing the Logistic Regression model
logreg.fit(X, y) # Fitting the model

pickle.dump(logreg, open('model.sav', 'wb'))
logreg = pickle.load(open('model.sav', 'rb'))

# Function for classification based on inputs
def classify(a, b, c, d):
    arr = np.array([a, b, c, d]) # Convert to numpy array
    arr = arr.astype(np.float64) # Change the data type to float
    query = arr.reshape(1, -1) # Reshape the array
    prediction = variety_mappings[logreg.predict(query)[0]] # Retrieve from dictionary
    return prediction # Return the prediction
'''