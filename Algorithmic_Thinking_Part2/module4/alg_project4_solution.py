"""
Project for examine Dynamic programming
"""

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Return scoring matrix that define each alphabets score include dash.

    :param alphabet: List of alphabets used in sequences of DNA
    :param diag_score: Score of same character
    :param off_diag_score: Score of off-diagonal characters
    :param dash_score: Score of dashes
    :return: Matrix of scoring matrix.
    """

    dic = {}
    alphabet_list = list(alphabet)
    alphabet_list += '-'
    for elem in alphabet_list:
        dic[elem] = {}

    for char_x in alphabet_list:
        for char_y in alphabet_list:
            if char_x == '-':
                dic['-'][char_y] = dash_score
            elif char_y == '-':
                dic[char_x]['-'] = dash_score
            elif char_x == char_y:
                dic[char_x][char_y] = diag_score
            else:
                dic[char_x][char_y] = off_diag_score

    return dic


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Compute the score of two sequences, seq_x, seq_y.

    :param seq_x: Sequence x
    :param seq_y: Sequence y
    :param scoring_matrix:
    :param global_flag:
    :return:
    """

    len_seq_x = len(seq_x)
    len_seq_y = len(seq_y)

    dp_table = []
    for loop_x in range(len_seq_x + 1):
        dp_table.append([])
        for loop_y in range(len_seq_y + 1):
            dp_table[loop_x].append(loop_y & 0)

    dp_table[0][0] = 0

    for loop_count in range(1, len_seq_x + 1):
        result = dp_table[loop_count - 1][0] + scoring_matrix[seq_x[loop_count - 1]]['-']
        if not global_flag and result < 0:
            result = 0
        dp_table[loop_count][0] = result

    for loop_count in range(1, len_seq_y + 1):
        result = dp_table[0][loop_count - 1] + scoring_matrix['-'][seq_y[loop_count - 1]]
        if not global_flag and result < 0:
            result = 0
        dp_table[0][loop_count] = result

    for x_count in range(1, len_seq_x + 1):
        for y_count in range(1, len_seq_y + 1):
            result = max(
                dp_table[x_count - 1][y_count - 1] + scoring_matrix[seq_x[x_count - 1]][seq_y[y_count - 1]],
                dp_table[x_count - 1][y_count] + scoring_matrix[seq_x[x_count - 1]]['-'],
                dp_table[x_count][y_count - 1] + scoring_matrix['-'][seq_y[y_count - 1]])
            if not global_flag and result < 0:
                result = 0
            dp_table[x_count][y_count] = result

    return dp_table


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """

    :param seq_x:
    :param seq_y:
    :param scoring_matrix:
    :param alignment_matrix:
    :return: Tuple of score, sequence x, sequence y
    """
    index_x = len(seq_x)
    index_y = len(seq_y)

    res_x = ""
    res_y = ""

    scores = 0

    while index_x != 0 and index_y != 0:
        if alignment_matrix[index_x][index_y] == (alignment_matrix[index_x - 1][index_y - 1] + scoring_matrix[seq_x[index_x - 1]][seq_y[index_y - 1]]):
            scores += scoring_matrix[seq_x[index_x - 1]][seq_y[index_y - 1]]
            res_x = seq_x[index_x - 1] + res_x
            res_y = seq_y[index_y - 1] + res_y
            index_x -= 1
            index_y -= 1
        else:
            if alignment_matrix[index_x][index_y] == (alignment_matrix[index_x - 1][index_y] + scoring_matrix[seq_x[index_x - 1]]['-']):
                scores += scoring_matrix[seq_x[index_x - 1]]['-']
                res_x = seq_x[index_x - 1] + res_x
                res_y = '-' + res_y
                index_x -= 1
            else:
                scores += scoring_matrix['-'][seq_y[index_y - 1]]
                res_x = '-' + res_x
                res_y = seq_y[index_y - 1] + res_y
                index_y -= 1

    while index_x != 0:
        scores += scoring_matrix[seq_x[index_x - 1]]['-']
        res_x = seq_x[index_x - 1] + res_x
        res_y = '-' + res_y
        index_x -= 1

    while index_y != 0:
        scores += scoring_matrix['-'][seq_y[index_y - 1]]
        res_x = '-' + res_x
        res_y = seq_y[index_y - 1] + res_y
        index_y -= 1

    return tuple([scores, res_x, res_y])


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """

    :param seq_x:
    :param seq_y:
    :param scoring_matrix:
    :param alignment_matrix:
    :return:
    """
    index_x = 0
    index_y = 0
    max_value = alignment_matrix[index_x][index_y]

    for loop_x in range(len(seq_x)+1):
        for loop_y in range(len(seq_y)+1):
            if max_value <= alignment_matrix[loop_x][loop_y]:
                max_value = alignment_matrix[loop_x][loop_y]
                index_x = loop_x
                index_y = loop_y

    res_x = ""
    res_y = ""

    scores = 0

    while index_x != 0 and index_y != 0:
        if alignment_matrix[index_x][index_y] == (alignment_matrix[index_x - 1][index_y - 1] + scoring_matrix[seq_x[index_x - 1]][seq_y[index_y - 1]]):
            scores += scoring_matrix[seq_x[index_x - 1]][seq_y[index_y - 1]]
            res_x = seq_x[index_x - 1] + res_x
            res_y = seq_y[index_y - 1] + res_y
            index_x -= 1
            index_y -= 1
        else:
            if alignment_matrix[index_x][index_y] == (alignment_matrix[index_x - 1][index_y] + scoring_matrix[seq_x[index_x - 1]]['-']):
                scores += scoring_matrix[seq_x[index_x - 1]]['-']
                res_x = seq_x[index_x - 1] + res_x
                res_y = '-' + res_y
                index_x -= 1
            else:
                scores += scoring_matrix['-'][seq_y[index_y - 1]]
                res_x = '-' + res_x
                res_y = seq_y[index_y - 1] + res_y
                index_y -= 1

        if alignment_matrix[index_x][index_y] == 0:
            break

    return tuple([scores, res_x, res_y])