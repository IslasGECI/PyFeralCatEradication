import numpy as np


def calculate_max_lambda(leslie_matrix):
    return np.max(np.linalg.eigvals(leslie_matrix).real)


def calculate_stable_stage(leslie_matrix):
    _, eigenvectors = np.linalg.eig(leslie_matrix)
    proyection = np.matmul(leslie_matrix, eigenvectors.real)
    return proyection / np.sum(proyection)


def calculate_reproductive_value(leslie_matrix, max_age=7):
    transition = leslie_matrix.copy()
    transition.loc[0] = 0
    fertility = leslie_matrix.copy()
    fertility.loc[1:] = 0
    identity = np.identity(max_age)
    N_fund = np.linalg.pinv(identity - transition.to_numpy())
    reproductive_matrix = np.matmul(fertility.to_numpy(), N_fund)
    return calculate_max_lambda(reproductive_matrix)


def calculate_generation_function(leslie_matrix):
    reproductive_values = np.log(calculate_reproductive_value(leslie_matrix))
    max_lambda_log = np.log(calculate_max_lambda(leslie_matrix))
    return reproductive_values / max_lambda_log
