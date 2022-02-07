#TIME COMPLEXITY: O(1)
def MonthNameTODays(MonthName):
    
    if MonthName == "February":
        return("No. of Days: 28/29 Days")
    elif MonthName in ("April", "June", "September", "November"):
        return("No. of Days: 30 Days")
    elif MonthName in ("January", "March", "May", "July", "August", "October", "December"):
        return("No. of Days: 31 Days")
    else:
        return("Wrong Month Name. Try Again!")

if __name__ == '__main__':
    print("List of Months: January, February, March, April, May, June, July, August, September, October, November, December")
    MonthName = input("Input the name of Month: ")
    reply = MonthNameTODays(MonthName)
    print(reply)
