def readWords(fName):
    f = open(fName)
    all = f.read()
    words = all.split()
    print(all, "\n")
    count = 0
    for x in words:
        count = count + 3
        print(count)
        print(len(words))

    f.close()


while True:
    name = input("Enter name of file: ")
    readWords(name)
    choice = input("\t\t\nEnter n to quit or Y to read another file ")
    if choice == "n" or choice == "N":
        break
