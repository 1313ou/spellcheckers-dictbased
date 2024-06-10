#!/usr/bin/python3

import argparse
import sys

import process
from process import *


def process_line(line, checkf):
    fields = line.split(r"\t")
    r = checkf()
    if r:
        print(f"{fields[0]} {fields[len(fields)-1]}")


def read_file(file, resume, checkf):
    with open(file) as fp:
        for line in fp:
            process_line(line.strip(), checkf)


def get_processing(name):
    return globals()[name] if name else process.default_process


def main():
    parser = argparse.ArgumentParser(description="scans the samples from sqlite file")
    parser.add_argument('text', type=str, help='text')
    parser.add_argument('--resume', type=int, help='line to resume from')
    parser.add_argument('--processing', type=str, help='processing function to apply')
    args = parser.parse_args()
    processing = get_processing(args.processing)
    if processing:
        print(processing, file=sys.stderr)
    read_file(args.text, args.resume, process_line)


if __name__ == '__main__':
    main()
