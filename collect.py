#!/usr/bin/python3

import read_all_withids
import read_samples_withids
import process

if __name__ == '__main__':
    read_all_withids.main()
    # for w in sorted(process.collected):
    #    print(w)
    sorted_dict = dict(sorted(process.frequency.items(), key=lambda x: x[1], reverse=False))
    for w in sorted_dict:
        print(f"{w} {sorted_dict[w]}")
