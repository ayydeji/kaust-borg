# gilps file that can be used with any tilde file to convert to gilps format.
import csv
import sys
# start program with the path to where you want the file to be saved as the first argument, the .kb file as the second argument.
def main():
    with open(sys.argv[1], 'w') as prolog:
        origin = open(sys.argv[2], 'r')
        lines = origin.readlines()
        # swap with the relevent relations from your dataset. modeh point to the target and modeb to the background information.
        prolog.write("\n"
                     ":- modeh(1, links_with(+protein, -protein)).\n"
                     ":- modeb(*, has_annotation(+protein, -annotation)).\n")
        for line in lines:
            # update with correct prediction target.
            if line.find('links_with') != -1:
                if line.find('pos') != -1:
                    prolog.write('example({}), 1).\n'.format(line[:-8].strip()))
                elif line.find('neg') != -1:
                    prolog.write('example({}), -1).\n'.format(line[:-8].strip()))
            else:
                prolog.write(line)

        examples = open('/home/muhammaa/ilp/gilps/examples.kb', 'r')
        # for line in examples.readlines():
        #     if line.find('pos') != -1:
        #         prolog.write('example({}), 1).\n'.format(line[:-7].strip()))
        #     elif line.find('neg') != -1:
        #         prolog.write('example({}), -1).\n'.format(line[:-7].strip()))

if __name__ == "__main__":
    main()
