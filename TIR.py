#TIR mean Thailand Inflation Rate

def getCalender():
    print("print test")
    print("")

def getRelated():
    print("print test")
    print("")

def getSource():
    Source =  "TREADING ECONOMICS"
    Link = "https://tradingeconomics.com/thailand/inflation-cpi"
    return Source,Link

def getChoises():
    choises = ["choose your choise", "1. get Calender table",
                    "2. get Related table", "3. get Source and link",
                    "4. stop application"]
    return choises

def printChoise():
    for line in getChoises():
        print(line)
    

def main():
    while True:
        print("-"*50)
        printChoise()
        choise = input("input your choise [1-4]: ")
        while choise not in ["1", "2", "3", "4"]:
            print("")
            print("your input out of choise\nplease input again")
            printChoise()
            choise = input("input your choise [1-4]: ")
        if choise == "1":
            getCalender()
        elif choise == "2":
            getRelated()
        elif choise == "3":
            tpl = getSource()
            print(f"{tpl[0]}: {tpl[1]}")
        else:
            break
        print("")

main()