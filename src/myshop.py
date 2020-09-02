from store import Store
from category import Category
from data_for_store import cats

my_store = Store("Bobs Emporium", [cats["legs"], cats["fruit"], cats["special"], cats["bats"]])

print(my_store)

selection = 0
while selection != len(my_store.categories) + 1:

    selection = input("Please select the number of a department. ")

    try:

        selection = int(selection)
        if selection == len(my_store.categories) + 1:
            print(f"Thanks for shopping at {my_store.name}")
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection - 1])
        else:
            print("Please select a valid number")

    except ValueError:
        print("Please enter your choice as a number.")