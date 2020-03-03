import csv 

prots = set()
# open the test csv file.
with open('/home/muhammaa/ilp/maxat-test/data/test/4932.protein.links.v11.0.txt') as infile:
    reader = csv.reader(infile, delimiter='\t')
# add all the proteins to the set.
    for row in reader:
        prots.add(row[1])
        prots.add(row[0])

# convert the set to a 1 column tsv file.
with open('/home/muhammaa/ilp/maxat-test/data/test/entities.tsv', 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='\t')

    for val in prots:
        writer.writerow([val])
