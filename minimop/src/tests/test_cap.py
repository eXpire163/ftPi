# test_cap.py
import pytest
from src.mathf import Mathf


def capital_case(mixcase):
    return mixcase.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_mathf():
        assert Mathf.clamp(10, 0, 1) == 1
        assert Mathf.clamp(0.53, 0, 1) == 0.53
        assert Mathf.smoothstep(0, 1, 0.5) == 0.5
        assert Mathf.smoothstep(0, 1, 0.2) == 0.104