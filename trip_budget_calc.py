# Trip Budget Calculator for a Family of Four

def get_positive_number(prompt):
    """Function to ensure user input is a valid positive number"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_trip_budget():
    print("\n🏖️ Welcome to the Family Trip Budget Calculator! 🏖️\n")

    # Collect user input
    airfare_per_person = get_positive_number("Enter airfare cost per person: $")
    daily_food_budget = get_positive_number("Enter daily food budget per person: $")
    trip_days = get_positive_number("Enter number of days for the trip: ")
    excursions = get_positive_number("Enter total excursion costs: $")
    souvenirs = get_positive_number("Enter total souvenir budget: $")

    # Calculate total costs
    total_airfare = airfare_per_person * 4
    total_food = daily_food_budget * 4 * trip_days
    total_cost = total_airfare + total_food + excursions + souvenirs

    # Display results
    print("\n💰 Trip Budget Summary 💰")
    print(f"Airfare: ${total_airfare:.2f}")
    print(f"Food: ${total_food:.2f} ({trip_days} days)")
    print(f"Excursions: ${excursions:.2f}")
    print(f"Souvenirs: ${souvenirs:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

    # Budget check
    budget_limit = 6000
    if total_cost > budget_limit:
        print("\n🚨 Budget Alert: Your trip cost exceeds the $6000 budget! 🚨")
        over_budget = total_cost - budget_limit
        print(f"You need to reduce costs by ${over_budget:.2f} to stay within budget.")
    else:
        remaining_budget = budget_limit - total_cost
        print("\n✅ Your trip is within budget!")
        print(f"You have ${remaining_budget:.2f} remaining for extra expenses!")

# Run the program
if __name__ == "__main__":
    calculate_trip_budget()