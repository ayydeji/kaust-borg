import csv
import math
import sys


outputfile = sys.argv[1]

train_relations = set()
train_drugs = set()
train_genes = set()

test_relations = set()
test_drugs = set()
test_genes = set()
# open the tsv file that you will end up writing to.
with open('{}_train.tsv'.format(outputfile), 'w', newline='') as output:
    writer = csv.writer(output, delimiter='\t')
# open the medset file.
    input = open('/home/muhammaa/ilp/original-data/new/drug_gene_disease.csv', 'r')
    reader = csv.reader(input)

    ppi_input = open('/home/muhammaa/ilp/original-data/new/gene_gene.csv', 'r')
    reader02 = csv.reader(ppi_input)
# find the number of lines that are inside the file.
    row_count = sum(1 for row in reader)
    input.seek(0)
# calculate the number of lines for the training and the test set.
    train_amount = math.floor(0.8 * row_count)
    print(train_amount, row_count)
    counter = 0
# for each line take the drug_target and the target_disease associations.
    for row in reader:
        # add these relations to a set.
        # add the drugs in these relations to a set.
        if counter > train_amount:
            break
        if (row[0], row[1]) not in train_relations:
            writer.writerow([row[0], 'has_target', row[1]])
            train_relations.add((row[0], row[1]))
            if row[0] not in train_drugs:
                train_drugs.add(row[0])

        if (row[1], row[2]) not in train_relations:
            writer.writerow([row[1], 'has_side_effect', row[2]])
            train_relations.add((row[1], row[2]))
            if row[1] not in train_genes:
                train_genes.add(row[1])

        if (row[0], row[2]) not in train_relations:
            writer.writerow([row[0], 'has_disease', row[2]])
            train_relations.add((row[0], row[2]))

        counter = counter+1

    for row in reader02:
        gene_1 = row[0].split('|')[0]
        gene_2 = row[1].split('|')[0]
        if gene_1 == 'NA' or gene_2 == 'NA':
            continue
        if gene_1 in train_genes or gene_1 in train_genes:
            writer.writerow([gene_1, 'interacts_with', gene_2])




with open('{}_test.tsv'.format(outputfile), 'w', newline='') as output2:
    writer = csv.writer(output2, delimiter='\t')
    # open the medset file.
    input = open('/home/muhammaa/ilp/original-data/new/drug_gene_disease.csv', 'r')
    reader = csv.reader(input)

    ppi_input = open('/home/muhammaa/ilp/original-data/new/gene_gene.csv', 'r')
    reader02 = csv.reader(ppi_input)

    for row in reader:
        # add these relations to a set.
        # add the drugs in these relations to a set.
        if (row[0], row[1]) not in train_relations and (row[0], row[1]) not in test_relations:
            writer.writerow([row[0], 'has_target', row[1]])
            test_relations.add((row[0], row[1]))
            if row[0] not in test_drugs:
                test_drugs.add(row[0])

        if (row[1], row[2]) not in train_relations and (row[1], row[2]) not in test_relations:
            writer.writerow([row[1], 'has_side_effect', row[2]])
            test_relations.add((row[1], row[2]))
            if row[1] not in test_genes:
                test_genes.add(row[1])

        if (row[0], row[2]) not in train_relations and (row[0], row[2]) not in test_relations:
            writer.writerow([row[0], 'has_disease', row[2]])
            test_relations.add((row[0], row[2]))

    for row in reader02:
        gene_1 = row[0].split('|')[0]
        gene_2 = row[1].split('|')[0]
        if gene_1 == 'NA' or gene_2 == 'NA':
            continue
        if gene_1 in test_genes or gene_1 in test_genes:
            writer.writerow([gene_1, 'interacts_with', gene_2])