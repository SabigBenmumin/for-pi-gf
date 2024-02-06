print("welcome to Economic news bro!!")
link_source = "https://www.bnnbloomberg.ca/bank-of-canada-measures-suggest-it-s-more-hawkish-than-market-thinks-scotiabank-says-1.2030943"
article_dict = {
    "source" : "BNN Bloomberg",
    "link" : link_source,
    "Bank_of_cannada_Decision" : "Reintroduced cash management tools not used for several years",
    "economist_view" : "Derek Holt does not expect an imminent easing of monetary policy",
    "quantitative_tightening_start" : "April 2022",
    "cash_management" : "Stopped buing Canadian government bons and allowed balance sheet to shrink as existing bonds matured",
    "market_stress_indicator" : "Increase in the Canadian Overnigght Repo Rate Average (Corra)",
    "current_policy_rate" : "5%",
    "QT_program_end_prediction" : "End of 2024 or early next year",
}
article_key = list(article_dict.keys()) #1

def main(): #2
    on = True
    while on: #3
        print("what you want man!!")
        print("choice for infomation")
        for i in range(1,len(article_dict)+1): #4
            print(f"[{i}] {article_key[i-1]}") #5
        print("[10] stop application")
        command = int(input("input your choise: ")) 
        if command == 10: #6
            on = False 
        elif command > 10: #7
            print("your input out of choise!!")
            print("choose again please")
        else: #8
            try: #9
                index_key = command-1 #10 cuz this line for calculate
                print(article_dict[article_key[index_key]])
            except: #11
                print("",end="")
        print("")
            
main() #12