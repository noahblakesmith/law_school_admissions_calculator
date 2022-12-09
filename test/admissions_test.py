import pytest
from admissions import predict

def test_predict():

    # Probability should always be between 0 and 1
    assert predict(3.75, 160, 0, 1, 0, 1, 'GEORGETOWN UNIVERSITY') > 0
    assert predict(3.75, 160, 0, 1, 0, 1, 'GEORGETOWN UNIVERSITY') < 100
    
    # Reality check 1
    assert predict(4.00, 178, 1, 0, 0, 1, 'OHIO STATE UNIVERSITY') > 50

    # Reality check 2
    assert predict(2.00, 152, 0, 1, 0, 1, 'COLUMBIA UNIVERSITY') < 50