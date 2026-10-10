inventory = {
    "Diamond": 3,
    "Stone": 10,
    "Wood": 5,
    "Apple": 2
}


def show_inventory():
    print("\n=== Minecraft Inventory ===")

    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

    print(f"Added {quantity} {item}(s)!")

def show_inventory_summary():
    total_types = len(inventory)
    total_quantity = sum(inventory.values())

    print("\n=== Inventory Summary ===")
    print(f"Number of item types: {total_types}")
    print(f"Total item quantity: {total_quantity}")
