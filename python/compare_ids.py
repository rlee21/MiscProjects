import sys


def compare_files(file1, file2):
    """ Read text files and converts each to a set and then checks for differences """
    with open(file1, 'r') as f:
        file1_data = f.read().splitlines()
        file1_ids = {row for row in file1_data}
    
    with open(file2, 'r') as f:
        file2_data = f.read().splitlines()
        file2_ids = {row for row in file2_data}
    
    file1_not_file2 = file1_ids.difference(file2_ids)
    file2_not_file1 = file2_ids.difference(file1_ids)
    
    if len(file1_not_file2) > 0:
           print("Records in {} but not in {}: {}".format(file1, file2, file1_not_file2))
    else:
        print("All records in {} are present in {}".format(file1, file2))

    if len(file2_not_file1) > 0:
        print("Records in {} but not in {}: {}".format(file2, file1, file2_not_file1))
    else:
        print("All records in {} are present in {}".format(file2, file1))


if __name__ == '__main__':
       file1 = sys.argv[1]
       file2 = sys.argv[2]
       compare_files(file1, file2)

