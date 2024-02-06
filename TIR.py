#TIR mean Thailand Inflation Rate
def getCalender():
    dataC = {
        0 : {
            "Calendar" : "2024-01-05",
            "GMT" : "04:00 AM",
            "Reference" : "Dec",
            "Actual" : "-0.83%",
            "Previous" : "0.44%",
            "Consensus" : "-0.3%",
            "TEForecast" : "-0.3%"},
        1 : {
            "Calendar" : "2024-02-05",
            "GMT" : "04:00 AM",
            "Reference" : "Jan",
            "Actual" : "-0.83%",
            "Previous" : "0.44%",
            "Consensus" : "-0.3%",
            "TEForecast" : "-0.3%"},
        2 : {
            "Calendar" : "2024-03-05",
            "GMT" : "04:00 AM",
            "Reference" : "Feb",
            "Actual" : "-0.83%",
            "Previous" : "0.44%",
            "Consensus" : "-0.3%",
            "TEForecast" : "-0.3%"
        }
    }
    key_list = list(dataC.keys())
    col_list = list(dataC[0].keys())
    col_len = [12, 10, 11, 8, 10, 11, 12]
    line_len = sum(col_len) + 9
    

def getRelated():
    print("print test")

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
        printChoise()
        choise = input("input your choise [1-4]: ")
        while choise not in ["1", "2", "3", "4"]:
            print("")
            print("your input out of choise\nplease input again")
            printChoise()
            choise = input("input your choise [1-4]: ")
        print("-"*75)
        if choise == "1":
            getCalender()
        elif choise == "2":
            getRelated()
        elif choise == "3":
            tpl = getSource()
            print(f"{tpl[0]}: {tpl[1]}")
        else:
            break
        print("-"*75)
        print("")

main()