#!/usr/bin/python3

import _pyspell
import _symspell
import _hunspell
import _textblob

def check_pyspell(input_text, id):
    if not _pyspell.spell_check(input_text, id):
        print(f"{id}\r{input_text}")


def check_symspell(input_text, id):
    if not _symspell.spell_check(input_text, id):
        print(f"{id}\r{input_text}")


def check_hunspell(input_text, id):
    if not _hunspell.spell_check(input_text, id):
        print(f"{id}\r{input_text}")


def check_textblob(input_text, id):
    if not _textblob.spell_check(input_text, id):
        print(f"{id}\r{input_text}")


def check_all(input_text, id):
    if not _pyspell.spell_check(input_text, id):
        if not _symspell.spell_check(input_text, id):
            print(f"{id}\r{input_text}")


def default_process(input_text, id):
    return False