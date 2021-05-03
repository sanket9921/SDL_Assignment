fname = input("Enter the file name  (info.txt)  :")
d1 = dict()
count = 0
count1 = 0
try:
    fhand = open(fname)
    for line in fhand:
        word = line.rstrip()
        print(word)
        count += 1
    fhand.close()
    fhand = open(fname)
    for lin in fhand:
        words = lin.split()

        for word in words:
            count1 += 1
            if word in d1:
                d1[word] = d1[word] + 1
            else:
                d1[word] = 1
    print(d1)
    fhand.close()
    print("Count of a line is", count)
    print("Count of word is ", count1)
except:
    print("File is not found please try again")
