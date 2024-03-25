#Student ID:
#Date:

studentlist = []
progresscounter = 0
trailercounter = 0
excludecounter = 0
retrievercounter = 0
y_or_q = None

def printlist():
    print("Part 2:")
    for x in range(len(studentlist)):
        print(studentlist[x][0], "- ", end='')
        print(studentlist[x][1], studentlist[x][2], studentlist[x][3], sep=", ")

def printfile():
    print("Part 3:")
    file = open("myfile.txt", "r")
    x=file.read()
    print(x)
    file.close()

file = open("myfile.txt", "w")
while True:
    if y_or_q == "q":
        break
    try:
        current_list = []
        credits_at_pass = int(input("Please enter your credits at pass: "))
        if credits_at_pass % 20 == 0 and credits_at_pass >= 0 and credits_at_pass <= 120:
            defer = int(input("Please enter your credit at defer: "))
            if defer % 20 == 0 and defer >= 0 and defer <= 120:
                fail = int(input("Please enter your credit at fail: "))
                if fail % 20 == 0 and fail >= 0 and fail <= 120:
                    if credits_at_pass + defer + fail == 120:
                        if credits_at_pass == 120:
                            progression = "Progress"
                            progresscounter += 1
                        elif credits_at_pass == 100:
                            progression = "Progress(module trailer)"
                            trailercounter += 1
                        elif fail >= 80:
                            progression = "Exclude"
                            excludecounter += 1
                        else:
                            progression = "Module retriever"
                            retrievercounter += 1
                        print(progression)
                        file.write(progression + " - " + str(credits_at_pass) + ", " + str(defer) + ", " + str(fail))
                        current_list = [progression, credits_at_pass, defer, fail]
                        studentlist.append(current_list)
                    else:
                        print("Total incorrect.")
                        continue
                else:
                    print("Out of range.")
                    continue
            else:
                print("Out of range.")
                continue
        else:
            print("Out of range.")
            continue
    except ValueError:
        print("Integer required")
        continue    
    while True:
        print("\nWould you like to enter another set of data?")
        y_or_q = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        print()
        if y_or_q == "y":
            break
        elif y_or_q == "q":
            print("---------------------------------------------------------------")
            print("Histogram")
            print("Progress ", progresscounter, " : ", progresscounter * "*")
            print("Tralier ", trailercounter, "  : ", trailercounter * "*")
            print("Retriever ", retrievercounter, ": ", retrievercounter * "*")
            print("Excluded", excludecounter, "  : ", excludecounter * "*\n")
            outcomes = progresscounter + trailercounter + retrievercounter + excludecounter
            if outcomes == 1:
                print("\n 1 outcome in total.")
            elif outcomes == 0:
                print("\n No outcomes.")
            else:
                print(outcomes, "outcomes in total.")
            print("---------------------------------------------------------------\n")
            printlist()
            printfile()
            break
        else:
            continue

