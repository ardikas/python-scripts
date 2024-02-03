from datetime import datetime

def get_year():
    year = now.strftime("%Y")
    current_year = input("Is this for year " + year +" (Y/N)? ")

    if  current_year == "N" or current_year == "n":
        year = input("Enter the correct year: ")
        return year
    else:
        return year

def get_month():
    # This function uses datetime module. 
    # The user gives the input for the month number. 
    # datetime.strptime() is called. 
    # It takes month number and month format "%m" as arguments. 
    # Passing "%b" to strftime returns abbreviated month name, 
    # while using "%B" returns full month name.

    current_month_num = now.strftime("%m")
    datetime_object = datetime.strptime(current_month_num, "%m")
    month_name = datetime_object.strftime("%b")

    current_month = input("Is this for the month of " + month_name +" (Y/N)? ")

    if  current_month == "N" or current_month == "n":
        month_name = input("Enter the correct month (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ")
        return month_name
    else:
        return month_name

def company():

    # Use a dictionary to associate the string the user enters with the one you want to display to them later:
    print("\nPlease select the company to be billed from the following options:")
    company_options = {
        "1": "Sound Chiropractic",
        "2": "Ring Road Limo Services",
    }

    # print the options
    for c, desc in company_options.items():
        print(f"{c}. {desc}")

    choice = input("\nEnter 1, 2, etc.: ")
    while choice not in company_options:
        choice = input(f"Please choose one of following options: {', '.join(company_options)}: ")

    print(f"\nCompany: {company_options[choice]}")

    company_selected = company_options[choice]
    return company_selected

def admin_fee(company_billed):

    if company_billed == "Sound Chiropractic":
        print("Admin fee: $ 10.00\n")
        adminfee = 10.00
        return adminfee
    elif company_billed == "Ring Road Limo Services":
        print("Admin fee: $ 10.00\n")
        adminfee = 10.00
        return adminfee

def enter_month_cost(bill_month):
    # use format to ensure there are two places after the decimal point, i.e 1.00
    cost_for_the_month = float(input("Please enter the cost for the month of " + bill_month + ": "))
    return cost_for_the_month

def website_work():
    # Create an empty dictionary in python. Then input a number to loop a number of times you want to take input. 
    # Then put a for loop and input key and value and store them in the dictionary as dict[key]=value.

    # initialize empty dictionary
    work = {}

    additional_work = input("\nWas there any work done on the website during that month (Y/N)? ")
    if  additional_work == "Y" or additional_work == "y":
        n=int(input("How many additional jobs were done during that month? "))

        for i in range(n):
            job = input("\nPlease enter a short description for job #" + str(i+1) + ": ")
            
            # use format to ensure there are two places after the decimal point, i.e 1.00
            job_cost = float(input("Please enter the cost for job #" + str(i+1) + ": "))
            work[job] = job_cost

        return work
    else:
        print("No additional work done. Got it.")
        exit
        
    return work

def get_total(fee, month_cost, website_work_dict):
    total = 0
    total = fee + month_cost + sum(website_work_dict.values())
    return total

def final_message(bill_year, bill_month, company_billed, fee, month_cost, website_work_dict, final_total):
    print("\n=======COPY & PASTE THE MESSAGE BELOW=======")
    print("\n" + bill_month + " " + bill_year + " AWS Bill for " + company_billed +"\n")

    # use format to ensure there are two places after the decimal point, i.e 1.00
    print("AWS " + bill_month + " " + bill_year + " - $" + "{0:.2f}".format(month_cost))
    print("Admin fee - $", "{0:.2f}".format(fee))

    print("\nWebsite work: ")
    if len(website_work_dict) == 0:
        print("None")
    else:
        # Printing a dictionary using a loop and the items() method
        for job, cost in website_work_dict.items():
            print("*", job, "- $", "{0:.2f}".format(cost))
    
    print("\n---------------")
    print("Total: $" + str("{0:.2f}".format(final_total)))
    print("---------------\n")
    print("Venmo request sent.\n")

if __name__ == "__main__":
    now = datetime.now() # current date and time

    # Get the date
    bill_year = get_year()
    bill_month = get_month()
    
    # Get the company and the associated fee
    company_billed = company()
    fee = admin_fee(company_billed)

    # Get the costs for the month
    month_cost = enter_month_cost(bill_month)

    # Access the dictionary that is returned from the website_work() function
    # website_work() function is responsible for collecting any additional labor and the cost
    website_work_dict = website_work()

    # Calculate the total costs based on the fee + month cost + any additional work
    final_total = get_total(fee, month_cost, website_work_dict) 

    # Print the final message
    final_message(bill_year, bill_month, company_billed, fee, month_cost, website_work_dict, final_total)


