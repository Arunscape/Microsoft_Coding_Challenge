#!/usr/bin/env python3
import csv

with open('file.csv') as f:
    data = list(csv.reader(f))
    outfile= open('output.txt','w')
    for line in f:
        print(line)
        numbers_in_line = [f for f in line]
        print(numbers_in_line)
        bitmask = numbers_in_line[0] & numbers_in_line[1]
        counter=0
        for char in bitmask:
            if char == 1:
                counter += 1
        print(counter)
        outfile.write(counter)
    outfile.close()
    f.close()
