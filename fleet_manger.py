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

def add_member(names, ranks, divs, ids):
    new_name = input("what is the name of the member you want to add")
    new_division = input ("What is the divsion you want to add")
    new_rank = input("What is the rank of the member").strip()
    new_id = int(input("What is the id of the new member").strip())
    valid_rank = False
    for rank in ranks:
        if new_rank == rank:
            valid_rank = True
            break
    valid_id = True
    for id in ids:
        if new_id == id:
            valid_id = False
            break 
    if valid_id and valid_rank:
        names.append(new_name)
        divs.append(new_division)
        ranks.append(new_rank)
        ids.append(new_id)
    elif valid_rank == False:
        print("Invalid Rank, please use a valid TNG rank")
    else:
        print("ID already in use, please use another ID")
    return(names, ranks, divs, ids)    
    

