

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Geordi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    division = ["Command", "Command", "Operations", "Security", "Engineering"]
    id = [1, 2, 3, 4, 5]
    return names, ranks, division, id

def display_menu():
    student_name = input("what is your name ")
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
    user_choice = input("Enter an option number ")
    return user_choice

def add_member(names, ranks, divs, ids):
    """
    Adds a new crew member. Checks that the id is unique and the rank is valid.
    """
    new_name = input("what is the name of the member you want to add ")
    new_division = input ("What is the divsion you want to add ")
    new_rank = input("What is the rank of the member ").strip()
    new_id = int(input("What is the id of the new member ").strip())
    valid_rank = False
    if new_rank in ranks:
        valid_rank = True
    valid_id = True
    if new_id in ids:
        valid_id = False
    if valid_id and valid_rank:
        names.append(new_name)
        divs.append(new_division)
        ranks.append(new_rank)
        ids.append(new_id)
    elif valid_rank == False:
        print("Invalid Rank, please use a valid TNG rank")
    else:
        print("ID already in use, please use another ID")
    return names, ranks, divs, ids   


def remove_member(names, ranks, divs, ids):
    """
    Remove a member using their ID
    """
    id_to_remove = input("Enter member ID to remove: ")
    if id_to_remove in ids:
        index_to_remove = ids.index(id_to_remove)
        names.pop(index_to_remove)
        ranks.pop(index_to_remove)
        divs.pop(index_to_remove)
        ids.pop(index_to_remove)
        print("Member has been removed")
    else:
        print ("Id not found")
    return names, ranks, divs, ids

def update_rank(names, ranks, ids):
    id_to_update = input("Enter Id to update rank ")
    if id_to_update in ids:
        new_rank = input("Enter updated rank ")
        index_to_update = ids.index(id_to_update)
        ranks[index_to_update] = new_rank
    else:    
        print("Error inavlid id")
    return names, ranks, ids    

def display_roster(names, ranks, divs, ids):
    print("Table of crew members")
    print("Name | Rank | Division | ID")
    print("______________________________")
    for index in range(len(names)):
        print(names[index]+ " | "  + ranks[index] + " | " + divs[index] + " | " + str(ids[index]))
        print("______________________________")


def search_crew(names, ranks, divs, ids):
    search_term = input ("Enter a search term ")
    for name in names:
        if search_term in name:
            print(name)

def filter_by_division(names, divs):
    user_chosen_divison = input ("Choose between Command, Operations, or Sciences ").strip()
    if user_chosen_divison == "Command" or user_chosen_divison == "Operations" or user_chosen_divison == "Sciences":
        for index in range(len(names)):
            if divs[index] == user_chosen_divison: 
                print (names[index])
    else:
        print("No members in that divison")   

def calculate_payroll(ranks):
    total_cost = 0 
    for rank in ranks:
        if rank == "Captain":
            total_cost = total_cost + 1000
        elif rank == "Commander":
            total_cost = total_cost + 800
        elif rank == "Lt. Commander":
            total_cost = total_cost + 600 
        else:
            total_cost = total_cost + 400
    return total_cost



                                 

def main():
    names, ranks, divisions, id = init_database()
    user_choice = display_menu()
    

if __name__ == "__main__":
    main()



    

