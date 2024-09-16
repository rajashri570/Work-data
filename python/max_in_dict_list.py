# Q. write a proram to find our the max element in each dictionary.
data = {
    "group1":[34,22,11],
    "group2":[43,99,23],
    "group3":[12,45,67]
}

for grp,values in data.items():
    # print(f"Max in {grp} is:",max(values))
    max = 0
    for num in values:
        if max < num:
            max = num
    print(grp,"max:",max)