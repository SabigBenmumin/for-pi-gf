#TIR mean Thailand Inflation Rate na ja
def printLine(l, char = "-"):
    print(char*l)

def printCols(lst, lens):
    for c in range(0,len(lst)):
        print(f"|{lst[c]:^{lens[c]}}",end="")
    print("|")

def getSummary():
    summary = f"In Thailand, the most important categories in the Consumer Price index are Food & Non-alcoholic Beverages (40% of the total weight), Housing & Furnishing (23%), Transportation & Communications (23%). Others include: Medical & Personal Care (6%); Recreation & Education (5%); Apparel & Footwear (2%); and Tobacco & Alcoholic Beverages (1%)."
    print(f"{summary:-^75}")
    print(summary)

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
    line_len = sum(col_len) + (len(col_len)+1)
    printLine(line_len)
    printCols(col_list, col_len)
    printLine(line_len)
    for recID in key_list:
        vals = list(dataC[recID].values())
        printCols(vals, col_len)
    printLine(line_len)

def getRelated():
    dataR = {
        0 : {
            "Related" : "Inflation Rate",
            "Last" : "-1.11",
            "Previous" : "-0.83",
            "Unit" : "percent",
            "Reference" : "Jan 2024"
        },
        1 : {
            "Related" : "Inflation Rate MoM",
            "Last" : "0.02",
            "Previous" : "-0.46",
            "Unit" : "percent",
            "Reference" : "Jan 2024"
        },
        2 : {
            "Related" : "Core Inflation Rate",
            "Last" : "0.52",
            "Previous" : "0.58",
            "Unit" : "percent",
            "Reference" : "Jan 2024"
        },
        3 : {
            "Related" : "Producer Prices",
            "Last" : "110.30",
            "Previous" : "110.00",
            "Unit" : "points",
            "Reference" : "Jan 2024"
        },
        4 : {
            "Related" : "Food Inflation",
            "Last" : "-1.06",
            "Previous" : "-0.63",
            "Unit" : "percent",
            "Reference" : "Jan 2024"
        },
        5 : {
            "Related" : "Producer Prices Change",
            "Last" : "0.30",
            "Previous" : "-0.81",
            "Unit" : "percent",
            "Reference" : "Jan 2024"
        },
        6 : {
            "Related" : "CPI Transportation",
            "Last" : "111.57",
            "Previous" : "108.42",
            "Unit" : "point",
            "Reference" : "Jan 2024"
        }
    }
    key_list = list(dataR.keys())
    col_list = list(dataR[0].keys())
    col_len = [22, 8, 10, 10, 12]
    line_len = sum(col_len) + (len(col_len)+1)
    printLine(line_len)
    printCols(col_list, col_len)
    printLine(line_len)
    for recID in key_list:
        vals = list(dataR[recID].values())
        printCols(vals, col_len)
    printLine(line_len)

def getSource():
    Source =  "TREADING ECONOMICS"
    Link = "https://tradingeconomics.com/thailand/inflation-cpi"
    return Source,Link

def getChoises():
    choises = ["choose your choise","1. get Thailand Inflation Rate", "2. get Calender table",
                    "3. get Related table", "4. get Source and link",
                    "5. stop application"]
    return choises

def printChoise():
    for line in getChoises():
        print(line)
    
def main():
    while True:
        printChoise()
        choise = input("input your choise [1-4]: ")
        while choise not in ["1", "2", "3", "4", "5"]:
            print("")
            print("your input out of choise\nplease input again")
            printChoise()
            choise = input("input your choise [1-5]: ")
        print("="*75)
        if choise == "1":
            getSummary()
        elif choise == "2":
            getCalender()
        elif choise == "3":
            getRelated()
        elif choise == "4":
            tpl = getSource()
            print(f"Source: {tpl[0]}\nLink: {tpl[1]}")
        else:
            break
        print("="*75)
        print("")

main()