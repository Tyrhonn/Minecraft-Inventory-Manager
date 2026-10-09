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