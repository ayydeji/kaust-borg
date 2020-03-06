from Bio import SeqIO
import csv
import pandas as pd 
import random
import os
import sys
import math
# output file will the path to where you want the file to be saved, input file is the location of the tsv file holding all relations.
def make_kb(outputfile, inputfile, diseaseset=None, drugset=None):
    if drugset == None:
        drugset = set()

    if diseaseset == None:
        diseaseset = set()

    with open(outputfile, 'w') as kb:
        # final = open(inputfile, 'r')
        # replace with the predictive target
        target = "links_with"
        final_reader = pd.read_csv(inputfile, header=None, sep='\t')
        final_reader = final_reader.sort_values(by=[1], ascending=True)
        without = final_reader[1] != target
        without_r = final_reader[without]
        # replace with the path to the negatives file.
        negatives = open('/home/muhammaa/ilp/maxat-test/data/train/4932_neg.tsv', 'r')
        neg_reader = csv.reader(negatives, delimiter='\t')

        for index, row in without_r.iterrows():
            kb.write("{}('{}', '{}').\n".format(row[1], row[0], row[2]))

        target = final_reader[1] == target
        target_r = final_reader[target]

        for index, row in target_r.iterrows():
            kb.write("{}('{}', '{}', pos).\n".format(row[1], row[0], row[2]))
            if row[0] not in drugset:
                drugset.add(row[0])
            if row[2] not in diseaseset:
                diseaseset.add(row[2])

        for row in neg_reader:
            if row[0] in drugset and row[1] in diseaseset:
                kb.write("links_with('{}', '{}', neg).\n".format(row[0], row[1]))

