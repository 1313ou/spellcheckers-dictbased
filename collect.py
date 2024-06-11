#!/usr/bin/python3

import read_all_withids
import read_samples_withids
import process

if __name__ == '__main__':
    read_samples_withids.main()
    for u in sorted(process.collected):
        print(u)
