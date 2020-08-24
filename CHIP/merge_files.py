import os
import sys

directories = sys.argv[1:len(sys.argv)- 1]
merged_files_path = sys.argv[len(sys.argv)-1]
master_map = {}

for d in directories:
    # list of files in directory
    arr = os.listdir(d)

    # make dictionary matching P# and R#
    for i in arr:
        # if i.endswith(".fastq.gz"):
        if i.endswith(".txt"):
            x = i.split('_')
            sample_num = x[1]
            run_num = x[4]
            if (sample_num,run_num) in master_map:
                master_map[(sample_num,run_num)].append(os.path.join(d, i))
            else:
                master_map[(sample_num,run_num)] = []
                master_map[(sample_num,run_num)].append(os.path.join(d, i))


# open new text file
file = open('commands.txt', 'w')        

# create cat commands and write commands to .txt file
for x in master_map:
    # don't create command if only one file matches
    if len(master_map[x]) == 1:
        continue
    master_map[x].sort()
    # start and assemble string
    string = "cat "
    for i in master_map[x]:
        string = string + i + " "
    string = f"{string}> CHIP_{x[0]}_{x[1]}_merged.fastq.gz"
    # write command to .txt file
    file.write(string + "\n")

file.close()
