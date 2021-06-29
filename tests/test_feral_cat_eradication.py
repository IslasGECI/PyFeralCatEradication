from feral_cat_eradication import (
    calculate_max_lambda,
    calculate_reproductive_value,
    calculate_stable_stage,
    calculate_generation_function,
)
import numpy as np
import pandas as pd
from math import isclose


leslie_matrix = pd.read_csv("feral_cat_eradication/data/leslie_matrix.csv")


def test_calculate_max_lambda():
    obtained_max_lambda = calculate_max_lambda(leslie_matrix)
    expected_max_lambda = 1.2492719194750208
    assert obtained_max_lambda == expected_max_lambda


def test_calculate_reproductive_value():
    obtained_reproductive_value = calculate_reproductive_value(leslie_matrix)
    expected_reproductive_value = 2.0419708727999995
    are_almost_equal = isclose(
        obtained_reproductive_value, expected_reproductive_value, abs_tol=1e-4
    )
    assert are_almost_equal


def test_calculate_stable_stage():
    leslie_matrix = np.array([[0.1, 0.1, 0.1], [0.2, 0, 0], [0, 0.2, 0]])
    expected_stable_stage = np.array(
        [
            [0.3397574, -0.07895071, -0.07895071],
            [0.27538551, 0.04322675, 0.04322675],
            [0.22320979, 0.11654761, 0.11654761],
        ]
    )
    obtained_stable_stage = calculate_stable_stage(leslie_matrix)
    np.testing.assert_allclose(expected_stable_stage, obtained_stable_stage)


def test_calculate_generation_function():
    obtained_generation_function = calculate_generation_function(leslie_matrix)
    expected_generation_function = 3.2077305601567505
    are_almost_equal = isclose(
        expected_generation_function, obtained_generation_function, abs_tol=1e-4
    )
    assert are_almost_equal
