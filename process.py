#!/usr/bin/python3

import _pyspell
import _symspell
import _hunspell
import _textblob


def check_pyspell(input_text):
    return _pyspell.spell_check(input_text)


def check_symspell(input_text):
    return _symspell.spell_check(input_text)


def check_hunspell(input_text):
    return _hunspell.spell_check(input_text)


def check_textblob(input_text):
    return _textblob.spell_check(input_text)


def check_all(input_text):
    if not _pyspell.spell_check(input_text):
        if not _symspell.spell_check(input_text):
            return _textblob.spell_check(input_text)


def default_process(input_text):
    return True
