# Setup
import pandas as pd
import numpy as np
import pickle

# Call pickle files
columns = pickle.load(open('columns.pkl', 'rb'))
logit = pickle.load(open('logit.sav', 'rb'))

# Define relevant variables
schools = [i.strip('school_') for i in list(columns) if 'school_' in i]
years = [i for i in list(columns) if 'year_' in i]

# Define predict function
def predict(a, b, c, d, e, f, g):
    user = pd.DataFrame(
        np.array(
            [a, b, c, d, e, f]
            + [1 if i=='year_2023' else 0 for i in years]
            + [1 if i==g else 0 for i in schools]
        ).reshape(1, -1), 
        columns=columns[1:]
    )
    prediction = int(100 * logit.predict_proba(user).flatten()[1])
    return prediction