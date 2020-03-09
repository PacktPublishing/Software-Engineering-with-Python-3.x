from source.expense import Expense
from source.user import User
from source.group import UserGroup
from source.utilities import initialize_data, print_menu, print_users, print_expenses, get_user_id


if __name__ == "__main__":

    # Initialize Dummy data
    users_list, groups_list, expense_list = initialize_data()
    
    while True:
        # Print the Menu options
        print_menu()

        # Get the User Choice
        next_choice = input()
        print(f"Choice selected is {next_choice}")

        if next_choice=='1':
            # Get User Details

            print("Enter New User Details Below")

            # Get User Name
            while True:
                user_name = input("Enter Name : ")
                if len(user_name) == 0:
                    print("User Name cannot be left blank")
                else:
                    break

            # Get User Email
            user_email = input("Enter Email (default: None):")
            
            # Create a new user
            new_user = User(user_name, user_email)

            # Add the user to the users_list
            users_list.append(new_user)

            print(f"New user {user_name} added successfully.")

        elif next_choice=='2':
            # Get Group Details
            print("Enter Group Details")
            
            # Get Group Name
            while True:
                group_name = input("Enter Name : ")
                if len(group_name) == 0:
                    print("User Name cannot be left blank")
                else:
                    break

            # Add the users to the Group
            while True:
                print("Now select the members to add to this group")
                print_users(users_list)
                print("Enters the user no.(s), seperated by a comma.")
                print("Please enter at least 2 users ")
                group_users = input()
                if len(group_users.split(',')) < 2:
                    print("Please enter at least 2 users ")
                else:
                    break
            # Map the user id to user_list
            # group_users = "1,2,3"
            # group.split(',') = ["1", "2", "3"]
            users_info = list(map(lambda x: users_list[int(x)-1], group_users.split(',')))

            # users_info = []
            # for user_id in group_users.split(','):
            #     users_info.append(user_list[int(user_id)-1])
            
            # Create a new Group
            new_group = UserGroup(group_name, users_info)

            # Add the group to groups_list
            groups_list.append(new_group)

            print(f"New Group {group_name} added successfully!")

        elif next_choice == '3':
            # Get the Expense Details

            group_name = None
            print("Enter Expense Details")
            
            print("Enter the Lender ID")
            # Get the Lender ID
            lender_id = get_user_id(users_list)
            
            # Get the amount
            print("Enter the amount lent :")
            amount_lent = int(input())

            # Check for Group Expense
            print("Is this a Group Expense [y/n]?")
            group_flag = input()
            if 'y' in group_flag or 'Y' in group_flag:
                # Select the Group
                while True:
                    gid = 1
                    for group in groups_list:
                        print(f"{gid}. {group.group_name}")
                        gid += 1
                    selected_group = input()
                    if len(selected_group) == 0:
                        print("Group cannot be None")
                    else:
                        # TODO: Check if the index is valid
                        group_name = groups_list[int(selected_group)-1]
                        break
                # Create new Expense
                new_expense = Expense(users_list[int(lender_id)],
                                      amount_lent,
                                      group=group_name)

                # Add the expense to the Expense list
                expense_list.append(new_expense)
            else:
                print("Enter how many lendee(s) are there for this expense ?")
                print(f"Note: There are total {len(users_list)} users only!")
                lendee_count = int(input("Enter lendee(s) count"))
                lendees_list = []
                while lendee_count > 0:
                    print("Select lendee from this list")
                    lendee_id = get_user_id(users_list)
                    lendees_list.append(users_list[lendee_id])
                    lendee_count -= 1

                # If Lendess_list = ["BOB"] ==> "BOB"
                # i.e. we flatten the list, so this changes the type 
                # from list to User Class
                if len(lendees_list)==1:
                    lendees_list = lendees_list[0]

                # Create a new Expense
                new_expense = Expense(users_list[int(lender_id)],
                                      amount_lent,
                                      lendee=lendees_list)
                # Add the expense to the list of expenses
                expense_list.append(new_expense)
        elif next_choice == '4':
            print_expenses(expense_list)
        elif next_choice == '5':
            curr_user_id = get_user_id(users_list)
            users_list[int(curr_user_id)].get_report()
        else:
            break









