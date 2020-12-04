# Every 3rd word of a text file will be displayed
# Concealment_1.txt is used to test


def readWords(fName):
    try:
        with open(fName) as f:
            all = f.read()
            words = all.split()
            print(all, "\n")
            count = -1
            list_len = len(words)
            for x in words:
                count += 3
                if count < list_len:
                    print(words[count])
    except FileNotFoundError:
        all = None


while True:
    name = input("Enter name of file: ")
    readWords(name)
    choice = input("\t\t\nEnter n to quit or Y to read another file ")
    if choice == "n" or choice == "N":
        break
