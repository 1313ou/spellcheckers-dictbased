#!/usr/bin/python3

import re
import io
from io import BytesIO
import tokenize
import token

import _pyspell
import _symspell
import _hunspell
import _textblob


def tokenize_text(input_text):
    text_stream = BytesIO(input_text.encode())
    try:
        tokens = list(tokenize.tokenize(text_stream.readline))
        return tokens
    except tokenize.TokenError:
        return None


def text_to_words(input_text):
    tokens = tokenize_text(input_text)
    return [t.string for t in tokens if t.type == token.NAME] if tokens else None


def split_text(input_text):
    return tokens.split(" \t+()`'\"")


def check_pyspell(input_text):
    return _pyspell.spell_check(input_text)


def check_word_pyspell(input_word):
    return _pyspell.spell_check_word(input_word)


def check_symspell(input_text):
    return _symspell.spell_check(input_text)


def check_hunspell(input_text):
    return _hunspell.spell_check(input_text)


def check_textblob(input_text):
    return _textblob.spell_check(input_text)


def check_all(input_text):
    ps = _pyspell.spell_check(input_text)
    sp = _symspell.spell_check(input_text)
    tb = _textblob.spell_check(input_text)
    return ps + sp + tb


def check_for_unknown(input_text):
    words = text_to_words(input_text)
    if words:
        words = [w for w in words if not w[0].isupper()]
        checked = [w for w in words if check_word_pyspell(w)]
        return checked


collected = set()


def collect_unknown(input_text):
    line_unknowns = check_for_unknown(input_text)
    if line_unknowns:
        # print(line_unknowns)
        collected.update(line_unknowns)
    return None


def default_process(input_text):
    return True


if __name__ == '__main__':
    my_word = "Pyhton"
    my_sentence = f"I love to code in {word}."
    p = check_word_pyspell(my_word)
    print(p)
    my_words = text_to_words(my_sentence)
    print(my_words)
    r = default_process(my_sentence)
    print(r)
