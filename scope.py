"""
    Return statements and scope

"""
def weekdays():

    work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekend = ("Sarturday", "Sunday")
    return work_days, weekend 
    # Local variable inside of weekdays




def main():

    days, weekend = weekdays() # scope is inside of main
    print("Work Week")
    days.append("Saturday")
    for day in days:
        print(day)
    
    print("\nWeekend")
 
    for day in weekend:
        print(day)


main()