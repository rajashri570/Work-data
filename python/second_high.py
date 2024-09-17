#Q.write a program to find the second highest number in a list.
l = [78,22,11,56,98]
high = 0
second_high = 0

for num in l:
    if high < num:
        second_high = high
        high = num
    elif second_high < num:
        second_high = num
    