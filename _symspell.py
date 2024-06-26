from symspellpy import SymSpell, Verbosity
from importlib.resources import files
import re
import sys

# pip install symspellpy

# Create a SymSpell object
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load a dictionary
dictionary_path = str(files('symspellpy').joinpath('frequency_dictionary_en_82_765.txt'))
print(dictionary_path, file=sys.stderr)
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
separators = r"[,.;:!?'\- ]+"


def spell_check(sentence):
    corrected = sym_spell.lookup_compound(sentence, max_edit_distance=2)
    if corrected:
        return list(map(lambda c: str(c.term), filter(lambda c: c.distance > 1, corrected)))
    return None


def spell_check_words(sentence):
    words = filter(lambda w: w != "", re.split(separators, sentence))
    return [spell_check_word(word) for word in words]


def spell_check_word(word):
    corrections = sym_spell.lookup(word, max_edit_distance=2, verbosity=Verbosity.CLOSEST)
    if corrections:
        return [correction.term for correction in corrections]
    return None


def print_spell_check(input_text, textid):
    r = spell_check(input_text)
    if r:
        print(f"{textid}\t{input_text}\t▶\t{r}")


def print_spell_check_words(input_text, textid):
    r = spell_check(input_text)
    if r:
        print(f"{textid}\t{input_text}\t▶\t{r}")


def print_spell_check_word(input_word, textid):
    r = spell_check(input_word)
    if r:
        print(f"{textid}\t{input_word}\t▶\t{r}")


if __name__ == '__main__':
    print_spell_check_word("misspell", 0)
    print_spell_check_word("misspeld", 0)
    print_spell_check("Ths sentence has some misspeld words.", 0)
    print_spell_check("I love to code in Pyhton.", 0)
    print_spell_check("Ths sentence has some misspeld words.", 0)
    print_spell_check("Screw you kuys, I am going home.", 1)
    print_spell_check("on one side of the island was a hugh rock, almost detached", 11595)
    print_spell_check("The glass was opacified more greater privacy", 11682)
    print_spell_check("in collee she minored in mathematics", 12111)
    print_spell_check("The scientists had to accommodate the new results with the existing theories", 10184)
    print_spell_check_words("in collee she minored in mathematics", 12111)
