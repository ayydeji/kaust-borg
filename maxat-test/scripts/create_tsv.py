import csv
import sys

# in the command line specify the annotation file as the first argument and the link file as the second.
assoc_file = sys.argv[1]
link_file = sys.argv[2]

# path to where you wnat to save the fie.
with open('/home/muhammaa/ilp/maxat-test/pykeen/graph/all_train_human_go.tsv', 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter='\t')
    
    if assoc_file != "None":
        assoc = open(assoc_file, 'r')
        assoc_reader = csv.reader(assoc, delimiter='\t')
    
        for row in assoc_reader:
            writer.writerow([row[0], 'has_annotation', row[1]])

    link = open(link_file, 'r')
    link_reader = csv.reader(link, delimiter='\t')

    for row in link_reader:
        writer.writerow([row[0], 'links_with', row[1]])
    # path to go annotations.
    go_file = open('/home/muhammaa/ilp/maxat-test/data/all_goslim_yeast.tsv', 'r')
    go_reader = csv.reader(go_file, delimiter='\t')

    for row in go_reader:
        writer.writerow(row)


