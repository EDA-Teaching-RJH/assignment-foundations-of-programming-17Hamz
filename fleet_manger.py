def main():
    names, ranks, divisions, id = init_database()
    


def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Geordi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    division = ["Command", "Command", "Operations", "Security", "Engineering"]
    id = [1, 2, 3, 4, 5]
    return names, ranks, division, id

if __name__ == "__main__":
    main()

def display_menu():
    student_name = input("what is your name")
    print("Fleet Management System")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    print(student_name + " is logged into the system")
    user_choice = input("Enter an option number")
    return user_choice

