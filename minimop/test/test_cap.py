# test_cap.py

def capital_case(mixcase):
    return mixcase.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
