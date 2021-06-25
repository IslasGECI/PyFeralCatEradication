from feral_cat_eradication import calculate_max_lambda
import pandas as pd

leslie_matrix = pd.read_csv("feral_cat_eradication/data/leslie_matrix.csv")


def test_calculate_max_lambda():
    obtained_max_lambda = calculate_max_lambda(leslie_matrix)
    expected_max_lambda = 1.2492719194750208
    assert obtained_max_lambda == expected_max_lambda
