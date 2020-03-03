import csv

terms = []

with open('/home/muhammaa/ilp/maxat-test/data/all_go.obo', 'r') as file:
    data = file.read()
    terms = data.split("\n\n[Term]")

with open('/home/muhammaa/ilp/maxat-test/data/all_goslim_yeast.tsv', 'w', newline='') as tsv:
    writer = csv.writer(tsv, delimiter='\t')
    tid = ""
    for val in terms:
        val.split('\n')
        line = val.split("\n")
        for desc in line:
            if desc.startswith("id:"):
                tid = desc[3:].strip()

            if tid.startswith("GO:") != -1:
                if desc.startswith("is_a:"):
                    id2 = desc[6:16].strip()
                    writer.writerow([tid, "is_a", id2])
                if desc.startswith("relationship:"):
                    l2 = desc[14: desc.find('!')].strip()
                    rel = l2[0: l2.find(" ")+1].strip()
                    id2 = l2[l2.find(" ")+1:].strip()
                    writer.writerow([tid, rel, id2])
        # if desc.find("id:") != -1:
        #     tid = desc[3:].trim()
        #     print(tid, "-----" ,"done")
