from Bio import SeqIO
import csv
import pandas as pd 
import random
import os
import sys
import math

def edit_fatsa():
    # edit file path here to relevent drug-target tsv you want to generate.
    with open('/home/muhammaa/ilp/original-data/targets.csv', 'w', newline='') as targets:
        fieldnames = ['drug', 'target']
        writer = csv.DictWriter(targets, fieldnames=fieldnames)
        writer.writeheader()
        # edit file path here to the drugbank target file.
        for record in SeqIO.parse('/home/muhammaa/ilp/original-data/protein.fasta', 'fasta'):
            prot = record.id.split('|')[1]
            drugs = record .description
            drugs = drugs[drugs.find('(DB')+1: -1].split(';')

            for val in drugs:
                writer.writerow({'drug':val.strip(),'target':prot.strip()})

def edit_ppi():
    with open('/home/muhammaa/ilp/original-data/ppi.csv', 'r') as ppi:
        # edit here to file path of the STRING ppi file to edit.
        with open('/home/muhammaa/ilp/original-data/protein_protein.csv', 'w', newline='') as new_file:
            reader = csv.DictReader(ppi, delimiter=',')
            fieldnames=['prot_a', 'mode', 'prot_b']
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                prot_a = row['protein_uniprot_a'].split('|')
                prot_b = row['protein_uniprot_b'].split('|')
                for val_a in prot_a:
                    for val_b in prot_b:
                        if val_a == 'NA' or val_b == 'NA':
                            continue
                        writer.writerow({'prot_a':val_a,'mode':row['mode'],'prot_b':val_b})
# method for replaceing the ids used in the disgenet data with uniprot.
def edit_gene_disease():
    vocab = pd.read_csv('/home/muhammaa/ilp/original-data/gene_mapping.tsv', encoding='utf-8', delimiter='\t')
    vocab_dict = dict(zip(vocab['GENEID'], vocab['UniProtKB']))
    
    
    with open('/home/muhammaa/ilp/original-data/curated_gene_disease_associations.tsv', 'r') as ppi:
        # path to file with the converted genes.
        with open('/home/muhammaa/ilp/original-data/gene_disease.csv', 'w', newline='') as new_file:
            reader = csv.DictReader(ppi, delimiter='\t')
            fieldnames=['geneId', 'diseaseId']
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                if row['diseaseType'] == 'disease':
                    print(row['geneId'].strip())
                    if row['geneId'].strip() in vocab_dict:
                        writer.writerow({'geneId':vocab_dict[row['geneId']],'diseaseId':row['diseaseId']})

def pykeen_csv():
    # path to where you want the final file to be sent to.
    with open('/home/muhammaa/ilp/graph/connected/final.csv', 'w', newline='') as final:
        writer = csv.writer(final, delimiter=',')

        drug_disease = open('/home/muhammaa/ilp/indevidual-graphs/drug_disease.csv', 'r')
        dd_reader = csv.reader(drug_disease)

        drug_gene = open('/home/muhammaa/ilp/indevidual-graphs/drug_gene.csv', 'r')
        dg_reader = csv.reader(drug_gene)

        gene_disease = open('/home/muhammaa/ilp/indevidual-graphs/gene_disease.csv', 'r')
        gd_reader = csv.reader(gene_disease)

        gene_gene = open('/home/muhammaa/ilp/indevidual-graphs/gene_gene.csv', 'r')
        gg_reader = csv.reader(gene_gene)

        for row in dd_reader:
            writer.writerow([row[0], 'has_disease', row[1]])
        
        for row in dg_reader:
            writer.writerow([row[0], 'has_target', row[1]])

        for row in gd_reader:
            writer.writerow([row[0], 'has_side_effect', row[1]])

        for row in gg_reader:
            writer.writerow([row[0], 'interacts_with', row[1]])

# when you have the pykeen finla file with all relations you can run this function to convert it to .kb.
# outputfile= output dir to where you want the kb to be saved.
# inputfile= input file of the tsv holding all your relationships.
def make_kb(outputfile, inputfile, diseaseset=None, drugset=None):
    if drugset == None:
        drugset = set()

    if diseaseset == None:
        diseaseset = set()

    with open(outputfile, 'w') as kb:
        # final = open(inputfile, 'r')
        final_reader = pd.read_csv(inputfile, header=None, sep='\t')
        final_reader = final_reader.sort_values(by=[1], ascending=False)
        # edit here to where your negatives file is.
        negatives = open('/home/muhammaa/ilp/original-data/new/negatives.csv', 'r')
        neg_reader = csv.reader(negatives)

        for index, row in final_reader.iterrows():
            # change the target to the relation you are trying to predict.
            if str(row[1]).find('has_disease') != -1:
                kb.write("{}('{}', '{}', pos).\n".format(row[1], row[0], row[2]))
                if row[0] not in drugset:
                    drugset.add(row[0])
                if row[2] not in diseaseset:
                    diseaseset.add(row[2])
            else:
                kb.write("{}('{}', '{}').\n".format(row[1], row[0], row[2]))
        for row in neg_reader:
            if row[0] in drugset and row[2] in diseaseset:
                kb.write("has_disease('{}', '{}', neg).\n".format(row[0], row[2]))

#run this to get a subset of your dataset. k is the number of drugs to take.
def subset(k=None, drugset=None, create_kb=True, split=False):
    if k is None and drugset is None:
        print("either enter a number or enter a drugset")
        sys.exit()

    if k is None:
        k=len(drugset)
    # path to drug_gene dataset.
    drug_gene = open('/home/muhammaa/ilp/indevidual-graphs/drug_gene.csv', 'r')
    df = pd.read_csv(drug_gene, header=None)
    dg_dict = {}

    for i, row in df.iterrows():
        if row[0] not in dg_dict:
            dg_dict[row[0]] = [row[1]]
        else:
            dg_dict[row[0]].append(row[1])
    
    drug_list = set(df[0].tolist())
    gene_list = set()
    disease_list = set()
    filename = k
    
    os.makedirs('/home/muhammaa/ilp/tilde/tilde/ecml06/drugdisease/{}_set'.format(k), exist_ok=True)
    if str(k).find('%') != -1:
        k = int(len(drug_list) * int(k[:-1])/100)
        
    print(k)
    tuple_ = set()
    if drugset == None:
        tuple_ = random_select(k, drug_list)
        drugs = tuple_[0]
    else:
        drugs = drugset
    with open('/home/muhammaa/ilp/tilde/tilde/ecml06/drugdisease/{}_set/kb_csv.tsv'.format(filename), 'w') as kb:
        writer = csv.writer(kb, delimiter='\t')

        for drug in drugs:
            for target in dg_dict[drug]:
                if target == 'NA':
                    continue
                if target.find('|') != -1:
                    targets = target.split('|')
                    for val in targets:
                        writer.writerow([drug, 'has_target', val])
                        gene_list.add(val)
                else:
                    writer.writerow([drug, 'has_target', target])
                    gene_list.add(target)
        # path to gene_gene set.
        gene_gene = open('/home/muhammaa/ilp/indevidual-graphs/gene_gene.csv', 'r')
        gg_reader = csv.reader(gene_gene)
        # path to gene_disease dataset.
        gene_disease = open('/home/muhammaa/ilp/indevidual-graphs/gene_disease.csv', 'r')
        gd_reader = csv.reader(gene_disease)
        # path to gene_disease dataset.
        drug_disease = open('/home/muhammaa/ilp/indevidual-graphs/drug_disease.csv', 'r')
        dd_reader = csv.reader(drug_disease)

        for row in gg_reader:
            if row[0] in gene_list or row[1] in gene_list:
                if row[0] == 'NA' or row[1] == 'NA':
                    continue
                if row[0].find('|') != -1 or row[1].find('|') != -1 :
                    row[0] = row[0].split('|')[0]
                    row[1] = row[1].split('|')[0]
                writer.writerow([row[0], 'interacts_with', row[1]])

        for row in gd_reader:
            if row[0] in gene_list:
                writer.writerow([row[0], 'has_side_effect', row[1]])
                disease_list.add(row[1])

        for row in dd_reader:
            if row[0] in drugs and row[1] in disease_list:
                writer.writerow([row[0], 'has_disease', row[1]])
        if create_kb == True:
            make_kb('/home/muhammaa/ilp/tilde/tilde/ecml06/drugdisease/{}_set/drugdisease.kb'.format(filename), '/home/muhammaa/ilp/tilde/tilde/ecml06/drugdisease/{}_set/kb_csv.tsv'.format(filename), drugs, disease_list)

        if split == True:
            return tuple_[1]

 
def random_select(k, entity_set):
    added = set()
    not_added = set()
    for i in range(0,k):
        selected = random.sample(entity_set,1)[0]
        if selected not in added:
            added.add(selected)
    for val in entity_set:
        if val not in added:
            not_added.add(val)

    return added, not_added

def train_test_split(train_split):
    inter = subset("{}".format(train_split), split=True)

    subset(drugset=inter, create_kb=False)

