#!/bin/python3

from collections import deque
from copy import deepcopy


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
    word_stack = []
    word_stack.append(start_word)
    if start_word == end_word:
        return word_stack
    word_queue = deque([])
    word_queue.append(word_stack)
    with open('words5.dict') as f:
        words = f.readlines()
        words = list([word.strip() for word in words])
    while len(word_queue) != 0:
        word_stack = word_queue.popleft()
        for word in words:
            if _adjacent(word_stack[-1], word):
                if word == end_word:
                    word_stack.append(word)
                    return word_stack
                copy_stack = deepcopy(word_stack)
                copy_stack.append(word)
                word_queue.append(copy_stack)
                words.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    for i in range(len(ladder)-1):
        if not _adjacent(ladder[i], ladder[i+1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    differ_counter = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            differ_counter += 1
    return differ_counter == 1
