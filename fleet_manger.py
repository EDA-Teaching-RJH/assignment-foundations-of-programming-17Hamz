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