from alg_application4_provided import *
from alg_project4_solution import *
import matplotlib.pyplot as plt
import random
from math import *

scoring_matrix = read_scoring_matrix(PAM50_URL)
human_seq = read_protein(HUMAN_EYELESS_URL)
fruit_seq = read_protein(FRUITFLY_EYELESS_URL)
consensus_seq = read_protein(CONSENSUS_PAX_URL)
word_list = read_words(WORD_LIST_URL)

def question1():
    alignment_matrix = compute_alignment_matrix(human_seq, fruit_seq, scoring_matrix, False)
    result = compute_local_alignment(human_seq, fruit_seq, scoring_matrix, alignment_matrix)
    return result

def question2(sequence):
    question1_result = question1()

    left_string = question1_result[1].replace("-","")
    right_string = question1_result[2].replace("-","")

    left_alignment_matrix = compute_alignment_matrix(left_string, sequence, scoring_matrix, True)
    right_alignment_matrix = compute_alignment_matrix(right_string, sequence, scoring_matrix, True)
    left_result = compute_global_alignment(left_string, sequence, scoring_matrix, left_alignment_matrix)
    right_result = compute_global_alignment(right_string, sequence, scoring_matrix, right_alignment_matrix)

    left_score = 0.0
    pam_index = 0
    for char in left_result[1]:
        if char == left_result[2][pam_index]:
            left_score += 1.0
        pam_index += 1

    right_score = 0.0
    pam_index = 0
    for char in right_result[1]:
        if char == right_result[2][pam_index]:
            right_score += 1.0
        pam_index += 1

    return tuple([(left_score/len(left_result[1])) * 100, (right_score/len(right_result[1]))*100])

def question3():
    test_amino = "ACBEDGFIHKMLNQPSRTWVYXZ"
    return question2(test_amino)

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    scoring_distribution = {}
    for loop_count in range(1,num_trials+1):
        rand = list(seq_y)
        random.shuffle(rand)
        rand_y = ''.join(rand)
        alignment_matrix = compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        result = compute_local_alignment(seq_x, rand_y, scoring_matrix, alignment_matrix)

        if result[0] in scoring_distribution:
            scoring_distribution[result[0]] += 1
        else:
            scoring_distribution[result[0]] = 1

    return scoring_distribution

def question4():
    trial = 1000
    scoring_distribution = generate_null_distribution(human_seq, fruit_seq, scoring_matrix, trial)

    dist_key = []
    dist_value = []
    for key, value in scoring_distribution.iteritems():
        dist_key.append(key)
        dist_value.append(value/float(trial))

    bar_width = 0.35

    rect = plt.bar(dist_key, dist_value, bar_width,
                   color = 'b',
                   label = 'Score')

    plt.xlabel('Scores')
    plt.ylabel('Distribution')
    plt.title('Null Distribution of human sequence and fruit flies sequence')
    plt.legend()
    plt.show()

def question5():
    trial = 1000
    scoring_distribution = generate_null_distribution(human_seq, fruit_seq, scoring_matrix, trial)
    dist_score = []
    dist_value = []
    key_count = 0
    for key, value in scoring_distribution.iteritems():
        dist_score.append(key)
        dist_value.append(value)
        key_count += 1

    mean = sum(dist_score)/float(key_count)
    sum_deriv = 0
    for elem in dist_score:
        sum_deriv += pow((elem-mean), 2)
    derivation = sqrt(sum_deriv/float(key_count))
    z_score = (sum_deriv-mean)/derivation

    return tuple([mean, derivation, z_score])

def question7():
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    return build_scoring_matrix(alphabets, 2, 1, 0)

def check_spelling(checked_word, dist, word_list):
    scoring_matrix = question7()

    result = set()

    checked_length = len(checked_word)
    for word in word_list:
        alignment_matrix = compute_alignment_matrix(checked_word, word, scoring_matrix, True)
        score_result = compute_global_alignment(checked_word, word, scoring_matrix, alignment_matrix)

        edit_distance = checked_length + len(word) - score_result[0]
        if edit_distance >= 0 and edit_distance <= dist:
            result.add(word)

    return result

def question8():
    humble_result = check_spelling('humble', 1, word_list)
    firefly_result = check_spelling('firefly', 2, word_list)

    print humble_result
    print firefly_result

print question5()
