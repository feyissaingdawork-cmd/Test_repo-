# # projec preparation
# """   1)	Build a program that:
# •	Displays a list of snacks and drinks with item numbers and prices. 
# •	Ask the user to choose items by number in a loop.
# •	 Keeps track of selected items and their prices.
# •	Ends when the user types "done".
# •	Finally prints a receipt showing: List of selected items with prices and total cost"""

def suq_badarate():
    bag = {
            1:{"name": "potato chips", "price": 1.99},
            2:{"name": "soda", "price": 2.25},
            3:{"name": "snackers", "price": 2.99},
            4:{"name": "bottle water", "price": "2.05"},
            5:{"name": "pretzels", "price": 1.85} 
        }
    choosen_item = []
    total_cost = 0
    print("\nWellcome to tinishua suq machine ")
    print("=" * 35)
    print("Item No. | Item name | Price ") 
    print("=" * 35)
    for number, item in bag.items():
            #{number:<8}: This takes the variable number, aligns it to the left (<), and ensures it occupies a width of exactly 8 characters.
            #print(f"{number:<8} | {item['name']:<13} | ${item['price']}:.2f" )
            print(f"{number:<8} | {item['name']:<13} | $(item['price']):<13.2f")
    print("=" * 35)
    while True:
            user_input = input("Enter an item number, or type 'done' to finish ").strip().lower()
            if user_input =="done":
                break
            try:
                item_number = int(user_input)
                #keep tracking selected item n their price 
                if item_number in bag:
                    item = bag[item_number]
                    choosen_item.append(item)
                    total_cost += item['price']
                    print(f"Added {item['name']} to your bag. " )
                    print(f"total cost: $({total_cost}.2f)")
                else:
                    print("Invalid Item number. try again")
                
            except ValueError:
                print("Invalid input. enter an item number or 'done'. ")

    print("\n" + "-" * 35)
    print(".............RECEIPT.........")
    print("=" * 35)
    if not choosen_item:
            print("No item purchased. ")
    else:
            for item in choosen_item:
                print(f"{item['name']:<20} ${item['price']:>13.2f}")
            print("=" *35)
            print("Thank you for your purchase!")
            print("Please come again")
suq_badarate()


