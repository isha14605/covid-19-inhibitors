import pandas as pd
import glob

# Created by Isha Sharma (iGEM Toronto Dry Lab Researcher)

# create two dictionaries with pdb_ids as keys and values as a list of
# lists of either chainA or chainB
dict_chainA = {}
dict_chainB = {}

# the file_path specifies which files to look at (in this case, .txt files)
file_path = ".../*.txt"

# a list of all the file names with the file_path
list_file_names = glob.glob(file_path)

# the loop goes through all the files in list_file_names
for f in list_file_names:
    # pdb_id stores the pdb_id of the file, f
    pdb_id = f[51:55]

    # these two lists represent the values of the dictionaries, with f_chainA
    # corresponding to dict_chainA and f_chainB corresponding to dict_chainB
    f_chainA = []
    f_chainB = []

    # open the file and read all the lines, which are stored in list_of_lines
    file = open(f, 'r')
    list_of_lines = file.readlines()

    # this loop goes through all of the lines in the file and strips them of the
    # newline character and additional spaces
    # these stripped lines are stored in a new list, cleaned_list
    cleaned_list = []
    for line in list_of_lines:
        stripped = line.rstrip()
        cleaned_list.append(stripped)

    # this loop checks for '>PDB|' in each line stored in cleaned_list and
    # stores the index of each occurrence in a new list, pdb_index
    pdb_index = []
    for j in range(len(cleaned_list)):
        if '>PDB|' in cleaned_list[j]:
            pdb_index.append(j)

    # the if/elif statements check for the length of pdb_index and append chains
    # to the list of chains, using the second occurrence of '>PDB|B' as the
    # breakpoint between chains A and B
    if len(pdb_index) == 1:
        chainA = cleaned_list[pdb_index[0]:]
        f_chainA.append(chainA)
    elif len(pdb_index) > 1:
        chainA = cleaned_list[pdb_index[0]:pdb_index[1]]
        chainB = cleaned_list[pdb_index[1]:]
        f_chainA.append(chainA)
        f_chainB.append(chainB)

    # create the key-value pairs for the dictionaries
    dict_chainA[pdb_id] = f_chainA
    dict_chainB[pdb_id] = f_chainB

# create dataFrame objects from the dictionaries
df_A = pd.DataFrame(dict_chainA.items(), columns=['pdb_id', 'chainA'])
df_B = pd.DataFrame(dict_chainB.items(), columns=['pdb_id', 'chainB'])

# export the dataFrames as .csv files
df_A.to_csv(r'Batch8-10A.csv', index=False, header=True)
df_B.to_csv(r'Batch8-10B.csv', index=False, header=True)

