import os
import sys

arr = os.listdir('sample_data')

master_map = {}
for i in arr:
    x = i.split('_')
    sample_num = x[2]
    run_num = x[4]
    if (sample_num,run_num) in master_map:
        master_map[(sample_num,run_num)].append(i)
    else:
        master_map[(sample_num,run_num)] = []
        master_map[(sample_num,run_num)].append(i)

for x in master_map:
    master_map[x].sort()

print(master_map)

