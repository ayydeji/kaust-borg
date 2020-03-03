import pandas as pd
import random
import os
import csv
import ntpath as nt


def make_kb():
    # update with the location of your training file, with all your relationships as triples in .tsv format.
    with open('../FB15k-237/data/fb15k_trn.tsv') as infile:
        reader = pd.read_csv(infile, sep='\t', header=None)

        for index, row in reader.iterrows():
            if any(c.isupper() for c in row[0]):
                row[0] = '{}'.format(row[0])
            if any(c.isupper() for c in row[2]):
                row[2] = '{}'.format(row[2])

        relations = reader[1].unique()
        # here you can update how many relations you want to work with, they will be randomly selected.
        relations = random_select(5, relations)

        for val in relations:
            print("working on {}".format(val))
            pairs = set([])
            entities = set([])

            subdata = reader[1] == val
            subdata = reader[subdata]

            path = '../FB15k-237/tilde/{}'.format(val)
            try:
                os.makedirs(path)
            except OSError:
                print("failed making directory")

            for index, row in subdata.iterrows():
                pairs.add((row[0], row[2]))
                entities.add(row[0])
                entities.add(row[2])

            negs = get_negatives(pairs, entities)

            with open('../FB15k-237/tilde/{}/fb15k.kb'.format(val), 'w') as kb_file:
                background_data = reader[1] != val
                background_data = reader[background_data]
                background_data = background_data.sort_values([1], ascending=True)
                for index, row in background_data.iterrows():
                    kb_file.write("{}('{}', '{}').\n".format(row[1], row[0], row[2]))
                for pos in pairs:
                    kb_file.write("{}('{}', '{}', pos).\n".format(val, pos[0], pos[1]))
                for neg in negs:
                    kb_file.write("{}('{}', '{}', neg).\n".format(val, neg[0], neg[1]))

            with open('../FB15k-237/tilde/{}/fb15k_tst.kb'.format(val), 'w') as tst_file:
                # update here with your tst file location
                tst = open('../FB15k-237/pykeen/graph/fb15k_tst.tsv')
                tst_reader = pd.read_csv(tst, header=None, sep='\t')

                for index, row in tst_reader.iterrows():
                    if any(c.isupper() for c in row[0]):
                        row[0] = '{}'.format(row[0])
                    if any(c.isupper() for c in row[2]):
                        row[2] = '{}'.format(row[2])

                tst_data = tst_reader[1] != val
                tst_data = tst_reader[tst_data]
                tst_data = tst_data.sort_values([1], ascending=True)

                for index, row in tst_data.iterrows():
                    tst_file.write("{}('{}', '{}').\n".format(row[1], row[0], row[2]))

            make_s(target=val)


def make_s(target=None):
    entity_to_type = {}
    relations_types = {}
    with open('../FB15k-237/data/entity2type.txt')as entityfile:
        reader = csv.reader(entityfile, delimiter='\t')

        for row in reader:
            if row[1] != "/common/topic" or len(row) == 2:
                entity_to_type[row[0]] = row[1]
            else:
                entity_to_type[row[0]] = row[2]

    with open('../FB15k-237/data/fb15k_trn.tsv') as train_fl:
        reader = pd.read_csv(train_fl, sep='\t', header=None)

        relations = reader[1].unique()
        for relation in relations:
            filtered_data = reader[1] == relation

            filtered_data = reader[filtered_data]
            sample = filtered_data.sample(n=1, replace=True, random_state=1)
            for index, row in sample.iterrows():
                relations_types[relation] = (entity_to_type["/m/{}".format(row[0])], entity_to_type["/m/{}".format(row[2])])

    with open('../FB15k-237/tilde/{}/fb15k.s'.format(target), 'w') as s_file:

        s_file.write("predict({}(+{}, -{})).\n".format(target, relations_types[target][0].replace('/', '_')[1:], relations_types[target][1].replace('/', '_')[1:]))
        s_file.write("typed_language(yes).\n\n")
        s_file.write("/* Add extra settings here. */\n")

        for relation in relations_types:
            if relation != target:
                s_file.write("type({}({}, {})).\n".format(relation, relations_types[relation][0].replace('/', '_')[1:], relations_types[relation][1].replace('/', '_')[1:]))
        s_file.write("\n")

        for relation2 in relations_types:
            if relation2 != target:
                s_file.write("rmode(50: {}(+{}, +-{})).\n".format(relation2, relations_types[relation2][0].replace('/', '_')[1:].title(), relations_types[relation2][1].replace('/', '_')[1:].title()))


def get_negatives(pairs, entities):

    new_pairs = []
    # for entity in entities:
    #     num_selected = 0
    #     already_picked = set()
    #     while num_selected <= n-1:
    #         co_entity = random.sample(entities, 1)[0]
    #         if (entity, co_entity) not in pairs and entity != co_entity and co_entity not in already_picked:
    #             new_pairs.append((entity, co_entity))
    #             already_picked.add(co_entity)
    #             num_selected += 1
    while (len(new_pairs) <= int(len(pairs) * 0.7)):
        p1 = random.sample(entities, 1)[0]
        p2 = random.sample(entities, 1)[0]
        if (p1, p2) not in pairs and p1 != p2 and (p1, p2) not in new_pairs:
            new_pairs.append((p1, p2))

    return new_pairs


def random_select(n, relations):
    selected = []
    subset = []
    if n > len(relations):
        print("n is greater than the length of the list given")
        return

    for i in range(0, n):
        select = random.choice(relations)
        if select not in subset:
            subset.append(select)

    return subset

