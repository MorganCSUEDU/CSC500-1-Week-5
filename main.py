import matplotlib.pyplot as plt

def calculate_rainfall_average():
    #get the number of years
    years = int(input("Enter the number of years: "))

    #initialize variables
    total_months = 0
    total_rainfall = 0
    rainfall_data = []

    #outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        
        #inner loop for each month
        for month in range(1, 13):
            rainfall = float(input(f"Enter rainfall for month {month} (inches): "))
            total_rainfall += rainfall
            total_months += 1
            rainfall_data.append(rainfall)

    #average rainfall
    average_rainfall = total_rainfall / total_months

    #results
    print("\nResults:")
    print(f"Total months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

    #rainfall chart
    months = [f"Month {i+1}" for i in range(total_months)]
    plt.figure(figsize=(10, 6))
    plt.bar(months, rainfall_data)
    plt.xlabel("Month")
    plt.ylabel("Rainfall (inches)")
    plt.title("Monthly Rainfall Chart")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

calculate_rainfall_average()

def calculate_points():
    #get the number of books purchased
    books_purchased = int(input("Enter the number of books purchased this month: "))

    #determine the points awarded based on the number of books purchased
    if books_purchased < 2:
        points_awarded = 0
    elif books_purchased < 4:
        points_awarded = 5
    elif books_purchased < 6:
        points_awarded = 15
    elif books_purchased < 8:
        points_awarded = 30
    else:
        points_awarded = 60

    # display the points awarded
    print(f"You have earned {points_awarded} points this month.")

calculate_points()
