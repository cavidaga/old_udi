#!/usr/bin/env python3

import argparse

MAPPING_PATH = "caucasian-albanian.txt"

# Made TABLE by running make_table() just once,
# then copy pasting that dict into data.py
from data import TABLE_T_TO_A, TABLE_A_TO_T, TEST_T_TO_A, TEST_A_TO_T

# Note that make_table, reverse_map, test_mappings aren't run,
# only were used to generate the tables


def make_table():
    with open(MAPPING_PATH, "r") as f:
        content = dict(
            map(
                lambda pair: [pair[0].strip(), pair[1].strip()],
                map(lambda line: line.split("-"), f.readlines()),
            )
        )
        return content


def reverse_map():
    t = make_table()
    return dict(map(lambda pair: [pair[1], pair[0]], t.items()))


def test_mappings():
    for albanian, turkish in TEST_A_TO_T:
        translit = "".join(
            map(lambda letter: TABLE_A_TO_T.get(letter, letter), albanian)
        )
        print(translit)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--infile", type=argparse.FileType("r", encoding="UTF-8"), required=True
    )
    parser.add_argument("--udi-to-albanian", action="store_true")
    args = parser.parse_args()
    payload = args.infile.read()
    args.infile.close()
    table = TABLE_A_TO_T if args.udi_to_albanian else TABLE_T_TO_A
    translit = "".join(map(lambda letter: table.get(letter, letter), payload))
    print(translit)
