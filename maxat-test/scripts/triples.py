import csv

with open('/home/muhammaa/ilp/maxat-test/pykeen/predictions/1.01/triples.tsv', 'w', newline='') as triples:
    writer = csv.writer(triples, delimiter='\t')

    train_file = open('/home/muhammaa/ilp/maxat-test/data/train/4932.protein.links.v11.0.txt')
    reader = csv.reader(train_file, delimiter='\t')

    for row in reader:
        writer.writerow([row[0], 'links_with', row[1]])
