""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
## Q1: Sample Paragraphs

def lines_from_file(path):
    readed_file = open(path)
    lines = readlines(readed_file)
    total = len(lines)
    i = 0
    while i < total:
        lines[i] = strip(lines[i])
        i += 1
    close(readed_file)
    return lines

def new_sample(path, i):
    lines = lines_from_file(path)
    return lines[i]

## Q2: Analyze

def analyze(sample_paragraph, typed_string, start_time, end_time):

    def words_per_minute(sample_paragraph, typed_string, start_time, end_time):
        characters_num = len(typed_string)
        words_num = characters_num / 5
        minutes = (end_time - start_time) / 60
        return words_num / minutes

    def accuracy_percentage(sample_paragraph, typed_string):
        sample_words = split(sample_paragraph)
        typed_words = split(typed_string)
        sample_len, typed_len = len(sample_words), len(typed_words)
        total, correct = min(sample_len, typed_len), 0
        if total == 0:
            return 0.0
        i = 0
        while i < total:
            if sample_words[i] == typed_words[i]:
                correct += 1
            i += 1
        return correct * 100 / total

    return [words_per_minute(sample_paragraph, typed_string, start_time, end_time), accuracy_percentage(sample_paragraph, typed_string)]

## Q3: Pig Latin

def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    suffixes = ['ay', 'way']
    new_word = ''
    if word[0] in vowels:
        new_word = word + suffixes[1]
    else:
        consonant_cluster = ''
        word_len = len(word)
        i = 0
        while i < word_len:
            if word[i] not in vowels:
                consonant_cluster += word[i]
            else:
                break
            i += 1
        new_word = word[i:] + consonant_cluster + suffixes[0]
    return new_word

## Q4: Autocorrect Skeleton

def autocorrect(user_input, words_list, score_function):

    def value_of_min_key(d):
        min_key = min(d.keys())
        for item in d.items():
            if item[0] == min_key:
                return item[1]

    if user_input in words_list:
        return user_input

    words_len = len(words_list)
    i = 0
    score_dict = {}
    while i < words_len:
        score = score_function(user_input, words_list[i])
        if score_dict.get(score) == None:
            score_dict[score] = i
        else:
            old_index = score_dict[score]
            min_index = min(i, old_index)
            score_dict[score] = min_index
        i += 1
    index_of_lowest = value_of_min_key(score_dict)
    return words_list[index_of_lowest]

## Q5: First Score Function

def swap_score(o, d):
    min_len = min(len(o), len(d))
    new_o, new_d = o[:min_len], d[:min_len]
    i, cnt = 0, 0
    while i < min_len:
        if new_o[i] == new_d[i]:
            cnt += 1
    return cnt

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    def dp(word1, word2, i, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if memo[i][j] != 0:
            return memo[i][j]

        if word1[i] == word2[j]:
            memo[i][j] = dp(word1, word2, i - 1, j - 1)
        else:
            a = dp(word1, word2, i, j - 1) + 1
            b = dp(word1, word2, i - 1, j) + 1
            c = dp(word1, word2, i - 1, j - 1) + 1
            memo[i][j] = min(a, b, c)
        return memo[i][j]
    memo = [[0] * len(word2) for i in range(len(word1))]
    return dp(word1, word2, len(word1) - 1, len(word2) - 1)


KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8

## Q7: Accuracy

def score_function_accurate(word1, word2):

## Q8: Efficiency

def score_function_final(word1, word2):

# END Q7-8
