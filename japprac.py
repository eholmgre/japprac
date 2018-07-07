#!/bin/python3

"""
    Japanese character quiz
    Author: Erik Holmgren
    Email: erik@erikholmgren.com
    Licence: GPL3
"""

import argparse
import random


def get_hiragana(diacritic=False, digraphs=False):
    hiragana = dict()

    hiragana['\N{HIRAGANA LETTER A}'] = ('a', [])
    hiragana['\N{HIRAGANA LETTER I}'] = ('i', [])
    hiragana['\N{HIRAGANA LETTER U}'] = ('u', [])
    hiragana['\N{HIRAGANA LETTER E}'] = ('e', [])
    hiragana['\N{HIRAGANA LETTER O}'] = ('o', [])

    hiragana['\N{HIRAGANA LETTER KA}'] = ('ka', [])
    hiragana['\N{HIRAGANA LETTER KI}'] = ('ki', [])
    hiragana['\N{HIRAGANA LETTER KU}'] = ('ku', [])
    hiragana['\N{HIRAGANA LETTER KE}'] = ('ke', [])
    hiragana['\N{HIRAGANA LETTER KO}'] = ('ko', [])

    hiragana['\N{HIRAGANA LETTER SA}'] = ('sa', [])
    hiragana['\N{HIRAGANA LETTER SI}'] = ('shi', [])
    hiragana['\N{HIRAGANA LETTER SU}'] = ('su', [])
    hiragana['\N{HIRAGANA LETTER SE}'] = ('se', [])
    hiragana['\N{HIRAGANA LETTER SO}'] = ('so', [])

    hiragana['\N{HIRAGANA LETTER TA}'] = ('ta', [])
    hiragana['\N{HIRAGANA LETTER TI}'] = ('chi', [])
    hiragana['\N{HIRAGANA LETTER TU}'] = ('tsu', [])
    hiragana['\N{HIRAGANA LETTER TE}'] = ('te', [])
    hiragana['\N{HIRAGANA LETTER TO}'] = ('to', [])

    hiragana['\N{HIRAGANA LETTER NA}'] = ('na', [])
    hiragana['\N{HIRAGANA LETTER NI}'] = ('ni', [])
    hiragana['\N{HIRAGANA LETTER NU}'] = ('nu', [])
    hiragana['\N{HIRAGANA LETTER NE}'] = ('ne', [])
    hiragana['\N{HIRAGANA LETTER NO}'] = ('no', [])

    hiragana['\N{HIRAGANA LETTER HA}'] = ('ha', [])
    hiragana['\N{HIRAGANA LETTER HI}'] = ('hi', [])
    hiragana['\N{HIRAGANA LETTER HU}'] = ('fu', [])
    hiragana['\N{HIRAGANA LETTER HE}'] = ('he', [])
    hiragana['\N{HIRAGANA LETTER HO}'] = ('ho', [])

    hiragana['\N{HIRAGANA LETTER MA}'] = ('ma', [])
    hiragana['\N{HIRAGANA LETTER MI}'] = ('mi', [])
    hiragana['\N{HIRAGANA LETTER MU}'] = ('mu', [])
    hiragana['\N{HIRAGANA LETTER ME}'] = ('me', [])
    hiragana['\N{HIRAGANA LETTER MO}'] = ('mo', [])

    hiragana['\N{HIRAGANA LETTER YA}'] = ('ya', [])
    hiragana['\N{HIRAGANA LETTER YU}'] = ('yu', [])
    hiragana['\N{HIRAGANA LETTER YO}'] = ('yo', [])

    hiragana['\N{HIRAGANA LETTER RA}'] = ('ra', [])
    hiragana['\N{HIRAGANA LETTER RI}'] = ('ri', [])
    hiragana['\N{HIRAGANA LETTER RU}'] = ('ru', [])
    hiragana['\N{HIRAGANA LETTER RE}'] = ('re', [])
    hiragana['\N{HIRAGANA LETTER RO}'] = ('ro', [])

    hiragana['\N{HIRAGANA LETTER WA}'] = ('wa', [])
    hiragana['\N{HIRAGANA LETTER WO}'] = ('wo', [])
    hiragana['\N{HIRAGANA LETTER N}'] = ('n', [])

    if diacritic:
        hiragana['\N{HIRAGANA LETTER GA}'] = ('ga', [])
        hiragana['\N{HIRAGANA LETTER GI}'] = ('gi', [])
        hiragana['\N{HIRAGANA LETTER GU}'] = ('gu', [])
        hiragana['\N{HIRAGANA LETTER GE}'] = ('ge', [])
        hiragana['\N{HIRAGANA LETTER GO}'] = ('go', [])

        hiragana['\N{HIRAGANA LETTER ZA}'] = ('za', [])
        hiragana['\N{HIRAGANA LETTER ZI}'] = ('ji', [])
        hiragana['\N{HIRAGANA LETTER ZU}'] = ('zu', [])
        hiragana['\N{HIRAGANA LETTER ZE}'] = ('ze', [])
        hiragana['\N{HIRAGANA LETTER ZO}'] = ('zo', [])
        
        hiragana['\N{HIRAGANA LETTER DA}'] = ('da', [])
        hiragana['\N{HIRAGANA LETTER DI}'] = ('ji', [])
        hiragana['\N{HIRAGANA LETTER DU}'] = ('zu', [])
        hiragana['\N{HIRAGANA LETTER DE}'] = ('de', [])
        hiragana['\N{HIRAGANA LETTER DO}'] = ('do', [])
        
        hiragana['\N{HIRAGANA LETTER BA}'] = ('ba', [])
        hiragana['\N{HIRAGANA LETTER BI}'] = ('bi', [])
        hiragana['\N{HIRAGANA LETTER BU}'] = ('bu', [])
        hiragana['\N{HIRAGANA LETTER BE}'] = ('be', [])
        hiragana['\N{HIRAGANA LETTER BO}'] = ('bo', [])

        hiragana['\N{HIRAGANA LETTER PA}'] = ('pa', [])
        hiragana['\N{HIRAGANA LETTER PI}'] = ('pi', [])
        hiragana['\N{HIRAGANA LETTER PU}'] = ('pu', [])
        hiragana['\N{HIRAGANA LETTER PE}'] = ('pe', [])
        hiragana['\N{HIRAGANA LETTER PO}'] = ('po', [])

    if digraphs:
        hiragana['\N{HIRAGANA LETTER KI}\N{HIRAGANA LETTER SMALL YA}'] = ('kya', [])
        hiragana['\N{HIRAGANA LETTER KI}\N{HIRAGANA LETTER SMALL YU}'] = ('kyu', [])
        hiragana['\N{HIRAGANA LETTER KI}\N{HIRAGANA LETTER SMALL YO}'] = ('kyo', [])

        hiragana['\N{HIRAGANA LETTER SI}\N{HIRAGANA LETTER SMALL YA}'] = ('sha', [])
        hiragana['\N{HIRAGANA LETTER SI}\N{HIRAGANA LETTER SMALL YU}'] = ('shu', [])
        hiragana['\N{HIRAGANA LETTER SI}\N{HIRAGANA LETTER SMALL YO}'] = ('sho', [])

        hiragana['\N{HIRAGANA LETTER TI}\N{HIRAGANA LETTER SMALL YA}'] = ('cha', [])
        hiragana['\N{HIRAGANA LETTER TI}\N{HIRAGANA LETTER SMALL YU}'] = ('chu', [])
        hiragana['\N{HIRAGANA LETTER TI}\N{HIRAGANA LETTER SMALL YO}'] = ('cho', [])

        hiragana['\N{HIRAGANA LETTER NI}\N{HIRAGANA LETTER SMALL YA}'] = ('nya', [])
        hiragana['\N{HIRAGANA LETTER NI}\N{HIRAGANA LETTER SMALL YU}'] = ('nyu', [])
        hiragana['\N{HIRAGANA LETTER NI}\N{HIRAGANA LETTER SMALL YO}'] = ('nyo', [])

        hiragana['\N{HIRAGANA LETTER HI}\N{HIRAGANA LETTER SMALL YA}'] = ('hya', [])
        hiragana['\N{HIRAGANA LETTER HI}\N{HIRAGANA LETTER SMALL YU}'] = ('hyu', [])
        hiragana['\N{HIRAGANA LETTER HI}\N{HIRAGANA LETTER SMALL YO}'] = ('hyo', [])

        hiragana['\N{HIRAGANA LETTER MI}\N{HIRAGANA LETTER SMALL YA}'] = ('mya', [])
        hiragana['\N{HIRAGANA LETTER MI}\N{HIRAGANA LETTER SMALL YU}'] = ('myu', [])
        hiragana['\N{HIRAGANA LETTER MI}\N{HIRAGANA LETTER SMALL YO}'] = ('myo', [])

        hiragana['\N{HIRAGANA LETTER RI}\N{HIRAGANA LETTER SMALL YA}'] = ('rya', [])
        hiragana['\N{HIRAGANA LETTER RI}\N{HIRAGANA LETTER SMALL YU}'] = ('ryu', [])
        hiragana['\N{HIRAGANA LETTER RI}\N{HIRAGANA LETTER SMALL YO}'] = ('ryo', [])

        hiragana['\N{HIRAGANA LETTER GI}\N{HIRAGANA LETTER SMALL YA}'] = ('gya', [])
        hiragana['\N{HIRAGANA LETTER GI}\N{HIRAGANA LETTER SMALL YU}'] = ('gyu', [])
        hiragana['\N{HIRAGANA LETTER GI}\N{HIRAGANA LETTER SMALL YO}'] = ('gyo', [])

        hiragana['\N{HIRAGANA LETTER ZI}\N{HIRAGANA LETTER SMALL YA}'] = ('ja', [])
        hiragana['\N{HIRAGANA LETTER ZI}\N{HIRAGANA LETTER SMALL YU}'] = ('ju', [])
        hiragana['\N{HIRAGANA LETTER ZI}\N{HIRAGANA LETTER SMALL YO}'] = ('jo', [])

        hiragana['\N{HIRAGANA LETTER BI}\N{HIRAGANA LETTER SMALL YA}'] = ('bya', [])
        hiragana['\N{HIRAGANA LETTER BI}\N{HIRAGANA LETTER SMALL YU}'] = ('byu', [])
        hiragana['\N{HIRAGANA LETTER BI}\N{HIRAGANA LETTER SMALL YO}'] = ('byo', [])

        hiragana['\N{HIRAGANA LETTER PI}\N{HIRAGANA LETTER SMALL YA}'] = ('pya', [])
        hiragana['\N{HIRAGANA LETTER PI}\N{HIRAGANA LETTER SMALL YU}'] = ('pyu', [])
        hiragana['\N{HIRAGANA LETTER PI}\N{HIRAGANA LETTER SMALL YO}'] = ('pyo', [])

    return hiragana


def get_katakana(diacritic=False, digraphs=False):
    katakana = dict()
    katakana['\N{KATAKANA LETTER A}'] = ('a', [])
    katakana['\N{KATAKANA LETTER I}'] = ('i', [])
    katakana['\N{KATAKANA LETTER U}'] = ('u', [])
    katakana['\N{KATAKANA LETTER E}'] = ('e', [])
    katakana['\N{KATAKANA LETTER O}'] = ('o', [])

    katakana['\N{KATAKANA LETTER KA}'] = ('ka', [])
    katakana['\N{KATAKANA LETTER KI}'] = ('ki', [])
    katakana['\N{KATAKANA LETTER KU}'] = ('ku', [])
    katakana['\N{KATAKANA LETTER KE}'] = ('ke', [])
    katakana['\N{KATAKANA LETTER KO}'] = ('ko', [])

    katakana['\N{KATAKANA LETTER SA}'] = ('sa', [])
    katakana['\N{KATAKANA LETTER SI}'] = ('shi', [])
    katakana['\N{KATAKANA LETTER SU}'] = ('su', [])
    katakana['\N{KATAKANA LETTER SE}'] = ('se', [])
    katakana['\N{KATAKANA LETTER SO}'] = ('so', [])

    katakana['\N{KATAKANA LETTER TA}'] = ('ta', [])
    katakana['\N{KATAKANA LETTER TI}'] = ('chi', [])
    katakana['\N{KATAKANA LETTER TU}'] = ('tsu', [])
    katakana['\N{KATAKANA LETTER TE}'] = ('te', [])
    katakana['\N{KATAKANA LETTER TO}'] = ('to', [])

    katakana['\N{KATAKANA LETTER NA}'] = ('na', [])
    katakana['\N{KATAKANA LETTER NI}'] = ('ni', [])
    katakana['\N{KATAKANA LETTER NU}'] = ('nu', [])
    katakana['\N{KATAKANA LETTER NE}'] = ('ne', [])
    katakana['\N{KATAKANA LETTER NO}'] = ('no', [])

    katakana['\N{KATAKANA LETTER HA}'] = ('ha', [])
    katakana['\N{KATAKANA LETTER HI}'] = ('hi', [])
    katakana['\N{KATAKANA LETTER HU}'] = ('fu', [])
    katakana['\N{KATAKANA LETTER HE}'] = ('he', [])
    katakana['\N{KATAKANA LETTER HO}'] = ('ho', [])

    katakana['\N{KATAKANA LETTER MA}'] = ('ma', [])
    katakana['\N{KATAKANA LETTER MI}'] = ('mi', [])
    katakana['\N{KATAKANA LETTER MU}'] = ('mu', [])
    katakana['\N{KATAKANA LETTER ME}'] = ('me', [])
    katakana['\N{KATAKANA LETTER MO}'] = ('mo', [])

    katakana['\N{KATAKANA LETTER YA}'] = ('ya', [])
    katakana['\N{KATAKANA LETTER YU}'] = ('yu', [])
    katakana['\N{KATAKANA LETTER YO}'] = ('yo', [])

    katakana['\N{KATAKANA LETTER RA}'] = ('ra', [])
    katakana['\N{KATAKANA LETTER RI}'] = ('ri', [])
    katakana['\N{KATAKANA LETTER RU}'] = ('ru', [])
    katakana['\N{KATAKANA LETTER RE}'] = ('re', [])
    katakana['\N{KATAKANA LETTER RO}'] = ('ro', [])

    katakana['\N{KATAKANA LETTER WA}'] = ('wa', [])
    katakana['\N{KATAKANA LETTER WO}'] = ('wo', [])
    katakana['\N{KATAKANA LETTER N}'] = ('n', [])

    if diacritic:
        katakana['\N{KATAKANA LETTER GA}'] = ('ga', [])
        katakana['\N{KATAKANA LETTER GI}'] = ('gi', [])
        katakana['\N{KATAKANA LETTER GU}'] = ('gu', [])
        katakana['\N{KATAKANA LETTER GE}'] = ('ge', [])
        katakana['\N{KATAKANA LETTER GO}'] = ('go', [])

        katakana['\N{KATAKANA LETTER ZA}'] = ('za', [])
        katakana['\N{KATAKANA LETTER ZI}'] = ('ji', [])
        katakana['\N{KATAKANA LETTER ZU}'] = ('zu', [])
        katakana['\N{KATAKANA LETTER ZE}'] = ('ze', [])
        katakana['\N{KATAKANA LETTER ZO}'] = ('zo', [])

        katakana['\N{KATAKANA LETTER DA}'] = ('da', [])
        katakana['\N{KATAKANA LETTER DI}'] = ('ji', [])
        katakana['\N{KATAKANA LETTER DU}'] = ('zu', [])
        katakana['\N{KATAKANA LETTER DE}'] = ('de', [])
        katakana['\N{KATAKANA LETTER DO}'] = ('do', [])

        katakana['\N{KATAKANA LETTER BA}'] = ('ba', [])
        katakana['\N{KATAKANA LETTER BI}'] = ('bi', [])
        katakana['\N{KATAKANA LETTER BU}'] = ('bu', [])
        katakana['\N{KATAKANA LETTER BE}'] = ('be', [])
        katakana['\N{KATAKANA LETTER BO}'] = ('bo', [])

        katakana['\N{KATAKANA LETTER PA}'] = ('pa', [])
        katakana['\N{KATAKANA LETTER PI}'] = ('pi', [])
        katakana['\N{KATAKANA LETTER PU}'] = ('pu', [])
        katakana['\N{KATAKANA LETTER PE}'] = ('pe', [])
        katakana['\N{KATAKANA LETTER PO}'] = ('po', [])

    if digraphs:
        katakana['\N{KATAKANA LETTER KI}\N{KATAKANA LETTER SMALL YA}'] = ('kya', [])
        katakana['\N{KATAKANA LETTER KI}\N{KATAKANA LETTER SMALL YU}'] = ('kyu', [])
        katakana['\N{KATAKANA LETTER KI}\N{KATAKANA LETTER SMALL YO}'] = ('kyo', [])

        katakana['\N{KATAKANA LETTER SI}\N{KATAKANA LETTER SMALL YA}'] = ('sha', [])
        katakana['\N{KATAKANA LETTER SI}\N{KATAKANA LETTER SMALL YU}'] = ('shu', [])
        katakana['\N{KATAKANA LETTER SI}\N{KATAKANA LETTER SMALL E}'] = ('she', [])
        katakana['\N{KATAKANA LETTER SI}\N{KATAKANA LETTER SMALL YO}'] = ('sho', [])

        katakana['\N{KATAKANA LETTER TI}\N{KATAKANA LETTER SMALL YA}'] = ('cha', [])
        katakana['\N{KATAKANA LETTER TI}\N{KATAKANA LETTER SMALL YU}'] = ('chu', [])
        katakana['\N{KATAKANA LETTER TI}\N{KATAKANA LETTER SMALL E}'] = ('che', [])
        katakana['\N{KATAKANA LETTER TI}\N{KATAKANA LETTER SMALL YO}'] = ('cho', [])

        katakana['\N{KATAKANA LETTER NI}\N{KATAKANA LETTER SMALL YA}'] = ('nya', [])
        katakana['\N{KATAKANA LETTER NI}\N{KATAKANA LETTER SMALL YU}'] = ('nyu', [])
        katakana['\N{KATAKANA LETTER NI}\N{KATAKANA LETTER SMALL YO}'] = ('nyo', [])

        katakana['\N{KATAKANA LETTER HI}\N{KATAKANA LETTER SMALL YA}'] = ('hya', [])
        katakana['\N{KATAKANA LETTER HI}\N{KATAKANA LETTER SMALL YU}'] = ('hyu', [])
        katakana['\N{KATAKANA LETTER HI}\N{KATAKANA LETTER SMALL YO}'] = ('hyo', [])

        katakana['\N{KATAKANA LETTER MI}\N{KATAKANA LETTER SMALL YA}'] = ('mya', [])
        katakana['\N{KATAKANA LETTER MI}\N{KATAKANA LETTER SMALL YU}'] = ('myu', [])
        katakana['\N{KATAKANA LETTER MI}\N{KATAKANA LETTER SMALL YO}'] = ('myo', [])

        katakana['\N{KATAKANA LETTER RI}\N{KATAKANA LETTER SMALL YA}'] = ('rya', [])
        katakana['\N{KATAKANA LETTER RI}\N{KATAKANA LETTER SMALL YU}'] = ('ryu', [])
        katakana['\N{KATAKANA LETTER RI}\N{KATAKANA LETTER SMALL YO}'] = ('ryo', [])

        katakana['\N{KATAKANA LETTER GI}\N{KATAKANA LETTER SMALL YA}'] = ('gya', [])
        katakana['\N{KATAKANA LETTER GI}\N{KATAKANA LETTER SMALL YU}'] = ('gyu', [])
        katakana['\N{KATAKANA LETTER GI}\N{KATAKANA LETTER SMALL YO}'] = ('gyo', [])

        katakana['\N{KATAKANA LETTER ZI}\N{KATAKANA LETTER SMALL YA}'] = ('ja', [])
        katakana['\N{KATAKANA LETTER ZI}\N{KATAKANA LETTER SMALL YU}'] = ('ju', [])
        katakana['\N{KATAKANA LETTER ZI}\N{KATAKANA LETTER SMALL E}'] = ('je', [])
        katakana['\N{KATAKANA LETTER ZI}\N{KATAKANA LETTER SMALL YO}'] = ('jo', [])

        katakana['\N{KATAKANA LETTER BI}\N{KATAKANA LETTER SMALL YA}'] = ('bya', [])
        katakana['\N{KATAKANA LETTER BI}\N{KATAKANA LETTER SMALL YU}'] = ('byu', [])
        katakana['\N{KATAKANA LETTER BI}\N{KATAKANA LETTER SMALL YO}'] = ('byo', [])

        katakana['\N{KATAKANA LETTER PI}\N{KATAKANA LETTER SMALL YA}'] = ('pya', [])
        katakana['\N{KATAKANA LETTER PI}\N{KATAKANA LETTER SMALL YU}'] = ('pyu', [])
        katakana['\N{KATAKANA LETTER PI}\N{KATAKANA LETTER SMALL YO}'] = ('pyo', [])

        katakana['\N{KATAKANA LETTER U}\N{KATAKANA LETTER SMALL I}'] = ('wi', [])
        katakana['\N{KATAKANA LETTER U}\N{KATAKANA LETTER SMALL E}'] = ('we', [])
        katakana['\N{KATAKANA LETTER U}\N{KATAKANA LETTER SMALL O}'] = ('wo', [])

        katakana['\N{KATAKANA LETTER TU}\N{KATAKANA LETTER SMALL A}'] = ('tsa', [])
        katakana['\N{KATAKANA LETTER TU}\N{KATAKANA LETTER SMALL I}'] = ('tsi', [])
        katakana['\N{KATAKANA LETTER TU}\N{KATAKANA LETTER SMALL E}'] = ('tse', [])
        katakana['\N{KATAKANA LETTER TU}\N{KATAKANA LETTER SMALL O}'] = ('tso', [])

        katakana['\N{KATAKANA LETTER TE}\N{KATAKANA LETTER SMALL I}'] = ('ti', [])

        katakana['\N{KATAKANA LETTER HU}\N{KATAKANA LETTER SMALL A}'] = ('fa', [])
        katakana['\N{KATAKANA LETTER HU}\N{KATAKANA LETTER SMALL I}'] = ('fi', [])
        katakana['\N{KATAKANA LETTER HU}\N{KATAKANA LETTER SMALL U}'] = ('fyu', [])
        katakana['\N{KATAKANA LETTER HU}\N{KATAKANA LETTER SMALL E}'] = ('fe', [])
        katakana['\N{KATAKANA LETTER HU}\N{KATAKANA LETTER SMALL O}'] = ('fo', [])

        katakana['\N{KATAKANA LETTER DE}\N{KATAKANA LETTER SMALL I}'] = ('di', [])
        katakana['\N{KATAKANA LETTER DE}\N{KATAKANA LETTER SMALL U}'] = ('dyu', [])

        katakana['\N{KATAKANA LETTER VU}\N{KATAKANA LETTER SMALL A}'] = ('va', [])
        katakana['\N{KATAKANA LETTER VU}\N{KATAKANA LETTER SMALL I}'] = ('vi', [])
        katakana['\N{KATAKANA LETTER VU}'] = ('vu', [])
        katakana['\N{KATAKANA LETTER VU}\N{KATAKANA LETTER SMALL E}'] = ('ve', [])
        katakana['\N{KATAKANA LETTER VU}\N{KATAKANA LETTER SMALL O}'] = ('vo', [])

    return katakana


def reverse_dict(to_reverse):

    revd = dict()

    for i in to_reverse:
        revd[to_reverse[i][0]] = (i, [])

    return revd


def versus(dict1, dict2):
    vsdict = dict()

    revd2 = reverse_dict(dict2)

    for c in dict1:
        try:
            vsdict[c] = (revd2[dict1[c][0]][0], [])
        except KeyError:
            pass

    return vsdict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Learn Japanese')
    grp1 = parser.add_mutually_exclusive_group()
    grp2 = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-k', '--katakana', action='store_true', help='quiz the katakana letters, default is hiragana.')
    grp1.add_argument('-b', '--both', action='store_true', help='quiz with both hiragana and katakana.')
    parser.add_argument('-d', '--diacritic', action='store_true',
                        help='quiz with diacritic marks (for g,b,d,z,p consonants).')
    parser.add_argument('-i', '--digraphs', action='store_true', help='quiz with letter combinations')
    parser.add_argument('-c', '--corrections', action='store_true',
                        help='show corrections for wrong answers while quizzing.')
    grp1.add_argument('--htok', action='store_true', help='input katakana given hiragana.')
    grp1.add_argument('--ktoh', action='store_true', help='input hiragana given katakana.')
    grp1.add_argument('-r', '--reversed', action='store_true', help='input Japanese characters given romaji.')
    grp2.add_argument('-o', '--once', action='store_true', help='quiz each character once in order.')
    grp2.add_argument('-a', '--random', action='store_true', help='quiz each character once randomly.')
    grp2.add_argument('-n', '--num', type=int, help='length of quiz')
    args = parser.parse_args()

    user_dict = None

    if args.htok:
        user_dict = versus(get_hiragana(args.diacritic, args.digraphs),
                           get_katakana(args.diacritic, args.digraphs))

    elif args.ktoh:
        user_dict = versus(get_katakana(args.diacritic, args.digraphs),
                           get_hiragana(args.diacritic, args.digraphs))

    elif args.katakana:
        user_dict = get_katakana(args.diacritic, args.digraphs)

    elif args.both:
        user_dict = {**get_hiragana(args.diacritic, args.digraphs),
                     **get_katakana(args.diacritic, args.digraphs)}

    else:
        user_dict = get_hiragana(args.diacritic, args.digraphs)

    if args.reversed:
        user_dict = reverse_dict(user_dict)

    errors = 0
    correct = 0

    char_list = None

    if args.once:
        char_list = [c for c in user_dict]
    elif args.random:
        char_list = [c for c in user_dict]
        random.shuffle(char_list)
    else:
        char_list = list()
        for _ in range(args.num):
            char_list.append(random.choice(list(user_dict)))

    for char in char_list:
        test = input(f'{char}: ')
        if user_dict[char][0] == test:
            print('\u2713')
            correct += 1
        else:
            print(f'\u2717 {"[" + user_dict[char][0] + "]" if args.corrections else ""}')
            user_dict[char][1].append(test)
            errors += 1

    if errors:
        print('mistakes:')
    for h in user_dict:
        if len(user_dict[h][1]) > 0:
            print(f'{h} ({user_dict[h][0]}): {len(user_dict[h][1])}, {user_dict[h][1]}')

    print(f'\ncorrect: {correct}, errors: {errors}, percent: {(correct / (correct + errors)) * 100}')



