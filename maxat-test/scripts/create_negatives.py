import csv

prots = set()
annots = set()

relationships = set()

with open('/home/muhammaa/ilp/maxat-test/data/train/9606_neg.tsv', 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='\t')

    annotations = open('/home/muhammaa/ilp/maxat-test/data/train/9606.protein.links.v11.0.txt', 'r')
    annot_reader = csv.reader(annotations, delimiter='\t')

    for row in annot_reader:
        prots.add(row[0])
        annots.add(row[1])

        relationships.add((row[0],row[1]))

    for prot in prots:
        counter = 0
        for annot in annots:
            if counter >= 5:
                break
            if (prot, annot) not in relationships:
                writer.writerow([prot, annot])
                counter = counter + 1
