# pip install hunspell

import hunspell

hunspeller = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')


def spell_check(sentence):
    correct = hunspeller.spell(sentence)
    if not correct:
        suggested = hunspeller.suggest(sentence)
        return suggested if suggested else False


def print_spell_check(input_text, textid):
    r = spell_check(input_text)
    if r:
        print(f"{textid}\t{input_text}\t▶\t{r}")


if __name__ == '__main__':
    print_spell_check("misspeld", 0)
    print_spell_check("I love to code in Pyhton.", 0)
    print_spell_check("Ths sentence has some misspeld words.", 0)
    print_spell_check("Screw you kuys, I am going home.", 1)
    print_spell_check("on one side of the island was a hugh rock, almost detached", 11595)
    print_spell_check("The glass was opacified more greater privacy", 11682)
    print_spell_check("in collee she minored in mathematics", 12111)
    print_spell_check("The scientists had to accommodate the new results with the existing theories", 10184)
