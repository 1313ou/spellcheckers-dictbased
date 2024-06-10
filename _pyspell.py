from spellchecker import SpellChecker
import re

# pip install pyspellchecker

spell = SpellChecker(language='en')  # English dictionary, change to other language if you prefer
separators = r"[,.;:!?\-\(\) ]+"


def spell_check(sentence):
    words = filter(lambda w: w != "", re.split(separators, sentence))
    unknown = spell.unknown(words)
    if len(unknown) > 0:
        corrected = [spell.correction(word) for word in unknown]
        return corrected
    return None


def spell_check_word(word):
    unknown = spell.unknown(word)
    if len(unknown) > 0:
        corrected = [spell.correction(word) for word in unknown]
        return corrected
    return None


def print_spell_check(input_text, textid):
    r = spell_check(input_text)
    if r:
        print(f"{textid}\t{input_text}\t▶\t{r}")


if __name__ == '__main__':
    print_spell_check("I love to code in Pyhton.", 0)
    print_spell_check("Ths sentence has some misspeld words.", 0)
    print_spell_check("Screw you kuys, I am going home.", 1)
    print_spell_check("on one side of the island was a hugh rock, almost detached", 11595)
    print_spell_check("The glass was opacified more greater privacy", 11682)
    print_spell_check("in collee she minored in mathematics", 12111)
    print_spell_check("The scientists had to accommodate the new results with the existing theories", 10184)
