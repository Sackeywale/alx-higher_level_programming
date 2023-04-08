#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
         return ("None")
    else:
        len_of_sentence = len(sentence)
        first_word = sentence[0]
        return (len_of_sentence, first_word)
