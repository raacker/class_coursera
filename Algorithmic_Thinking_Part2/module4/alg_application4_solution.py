from alg_application4_provided import *
from alg_project4_solution import *
import matplotlib.pyplot as plt

scoring_matrix = read_scoring_matrix(PAM50_URL)
human_seq = read_protein(HUMAN_EYELESS_URL)
fruit_seq = read_protein(FRUITFLY_EYELESS_URL)

def question1():
    