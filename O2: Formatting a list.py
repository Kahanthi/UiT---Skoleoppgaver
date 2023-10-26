items = []
while True:
    item = input("Enter an item (blank to quit): ")
    if not item:
        break
    items.append(item)

if items:
    formatted_items = ", ".join(items[:-1]) + " and " + items[-1]
    print("The items are " + formatted_items + ".")
else:
    print("No items entered.")