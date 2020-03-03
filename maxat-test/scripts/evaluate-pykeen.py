import csv
import pandas as pd
import sys

links = {}
links=set()
hts10 = []
hts100 = []
meanrnk = []

with open('/home/muhammaa/ilp/maxat-test/data/test/4932.protein.links.v11.0.txt') as test_file:
    tst_reader = pd.read_csv(test_file, delimiter='\t', header=None)

    for index, row in tst_reader.iterrows():
        links.add((row[0], row[1]))
    
    with open('/home/muhammaa/ilp/maxat-test/pykeen/predictions/1.01/predictions.tsv' ) as predictions:
        reader = pd.read_csv(predictions, sep=' ', header=None)
        reader = reader.sort_values(by=[3], ascending=False)
        
        hits_count = 0
        row_count=1
        for index, row in reader.iterrows():
            if (row[0], row[2]) in links:
                print("({},{})".format(row[0], row[2]))
                print(row_count)
                hits_count = hits_count+1
                meanrnk.append(row_count)
                links.discard((row[0], row[2]))
                if len(links) == 0:
                    break

            if index == 10:
                hts10.append((hits_count/index) * 100)
            if index == 100:
                hts10.append((hits_count/index) * 100)

            row_count = row_count+1


    print(hts10/100, hts100/100, meanrnk/100)


