import csv
import pandas as pd
import ntpath as nt

protein_set = set()
with open('/home/muhammaa/ilp/knowledge_embeddings/WN18RR/test.kb', 'w') as kb_file:

    final = open('/home/muhammaa/datasets_knowledge_embedding/WN18RR/original/test.txt')
    final_reader = pd.read_csv(final, header=None, sep='\t')
    final_reader = final_reader.sort_values(by=[1], ascending=False)

    for index, row in final_reader.iterrows():
        # if row[1] == "has_annotation":
        #     kb_file.write("{}({}, '{}').\n".format(row[1], str(row[0])[5:].lower(), row[2]))
        #     protein_set.add(row[0])
        #     protein_set.add(row[2])
        # elif row[1] == "links_with":
        #     kb_file.write("{}({}, {}).\n".format(row[1], str(row[0])[5:].lower(), row[2][5:].lower()))
        #     protein_set.add(row[0])
        #     protein_set.add(row[2])
        # kb_file.write("{}({}, {}).\n".format(nt.basename(row[1]), nt.basename(row[0]), nt.basename(row[2])))
        kb_file.write("{}({}, {}).\n".format(row[1], row[0], row[2]))

# with open('/home/muhammaa/ilp/maxat-test/ilp/tilde/yeast/new_data/yeast.bg', 'w') as bg_file:
#
#     go_info = open('/home/muhammaa/ilp/maxat-test/data/goslim_yeast.tsv')
#     go_reader = pd.read_csv(go_info, delimiter='\t', header=None)
#     go_reader = go_reader.sort_values(by=[1], ascending=False)
#
#     for index, row in go_reader.iterrows():
#         if row[0] in protein_set and row[2] in protein_set:
#             bg_file.write("{}('{}', '{}').\n".format(row[1], row[0], row[2]))


# with open('/home/muhammaa/ilp/maxat-test/ilp/tilde/yeast/new_data/yeast.s', 'w') as s_file:
#     s_file.write("""
# predict(has_link(+protein, -protein)).\n
# typed_language(yes).\n
# type(has_annotation(protein, annotation)).
# type(is_a(annotation, annotation)).
# type(part_of(annotation, annotation)).
# type(has_part(annotation, annotation)).
# type(occurs_in(annotation, annotation)).
# type(regulates(annotation, annotation)).\n
#
# rmode(5: has_annotation(+Protein, +-Annotation)).
# rmode(5: is_a(+Annotation, +-Annotation)).
# rmode(5: part_of(+Annotation, +-Annotation)).
# rmode(5: has_part(+Annotation, +-Annotation)).
# rmode(5: occurs_in(+Annotation, +-Annotation)).
# rmode(5: regulates(+Annotation, +-Annotation)).
#     """)