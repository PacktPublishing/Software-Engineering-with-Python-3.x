from source.expense import Expense
from source.user import User
from source.group import UserGroup


def initialize_data():
    """This function initialized users, groups and expenses."""
    
    user1 = User('Bob', 'bob@gmail.com')
    user2 = User('Roy', 'roy@gmail.com')
    user3 = User('Jessica', 'jessica@gmail.com')
    user4 = User('Michelle', 'michel@yahoo.com')

    group1 = UserGroup('Home', [user1, user3])
    group2 = UserGroup('College', [user2, user3, user4])

    expense1 = Expense(user1, 100, lendee=user4)
    expense2 = Expense(user2, 50, lendee=[user1, user3])
    expense3 = Expense(user1, 100, group=group2)

    users_list = [user1, user2, user3, user4]
    groups_list = [group1, group2]
    expense_list = [expense1, expense2, expense3]

    return users_list, groups_list, expense_list


def print_menu():
    print("What do you want to do ?")
    print("1. Add User")
    print("2. Add Group")
    print("3. Add Expense")
    print("4. Show All Expenses")
    print("5. Show User Expenses")
    print("6. Enter Anything else to Exit")


def print_users(users_list):
    user_id = 1
    for user in users_list:
        print(f"{user_id}. {user.name}")
        user_id += 1


def print_expenses(expense_list):
    expense_id = 1
    for expense in expense_list:
        lender_name = expense.lender.name
        if expense.group is not None:
            print(f"{expense_id}. {lender_name} loaned {expense.group.group_name} {expense.amount} $")
            expense_id += 1
        else:
            if expense.transaction_type=='single':
                print(f"{expense_id}. {lender_name} loaned {expense.lendee.name} {expense.amount} $")
                expense_id += 1
            else:
                lendee_names = []
                for lendee in expense.lendee:
                    lendee_names.append(lendee.name)

                lendee_names_str = ",".join(lendee_names)
                # Get index of last comma
                index_comma = str.rfind(lendee_names_str, ',')
                lendee_names_str = lendee_names_str[:index_comma] + ' and ' + lendee_names_str[index_comma+1:]
                print(f"{expense_id}. {lender_name} loaned {lendee_names_str} {expense.amount} $")
                expense_id += 1


def get_user_id(users_list):
    print("Enter the User details")
    while True:
        print("Now select the user id from the following users")
        print_users(users_list)
        user_id = input()
        if len(user_id) == 0:
            print("User ID cannot be None")
        else:
            break
    return int(user_id)-1