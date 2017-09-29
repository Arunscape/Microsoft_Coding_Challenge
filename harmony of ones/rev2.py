#!/usr/bin/env python3
import csv

with open('file.csv') as f:
    data = list(csv.reader(f))
    data.pop(0)
    #print(data)

    for line in data:
        num1 = int(line[0])
        num2 = int(line[1])

        binary = num1 & num2

        numones= bin(binary).count("1")
        print(numones)
        numones = str(numones)

        outfile = open('outfile.txt','w')
        outfile.write(numones)
        outfile.write("\n")
        #bitmask = num1 & num2

        # counter=0
        # for char in bitmask:
        #     if char == 1:
        #         counter+=1
        # outfile = open('output.txt', 'w')
        # outfile.write(str(counter))
