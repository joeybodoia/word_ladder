#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',\
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',\
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    word1_counter = {}
    word2_counter = {}
    for i in range(len(word1)):
        if word1[i] in word1_counter:
            word1_counter[word1[i]] += 1
        else:
            word1_counter[word1[i]] = 1
    for i in range(len(word2)):
        if word2[i] in word2_counter:
            word2_counter[word2[i]] += 1
        else:
            word2_counter[word2[i]] = 1
    differ_counter = 0
    for key in word1_counter:
        # print("word1_counter[key]", word1_counter[key])
        # print("word2_counter[key]", word2_counter[key])
        if key not in word2_counter:
            differ_counter += 1
        elif word1_counter[key] != word2_counter[key]:
            differ_counter += abs(word1_counter[key]-word2_counter[key])
    if differ_counter <= 1:
        return True
    else:
        return False
