
from inventory import show_inventory, add_item

# ===== Terminal colors =====
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
GRAY = "\033[90m"
WHITE = "\033[97m"


def line(char="═", width=48):
    print(f"{DARK_GREEN}{char * width}{RESET}")


def title():
    print()
    line("═")
<<<<<<< HEAD
    print(f"{GREEN}{BOLD}        ⛏️  MINECRAFT INVENTORY - SURVIVAL MODE{RESET}")
=======
    print(f"{GREEN}{BOLD}        ⛏️  MINECRAFT INVENTORY - DIAMOND EDITION{RESET}")
>>>>>>> d97701158eac9b91774636bf26555b1f69606a24
    print(f"{YELLOW}             BLOCK EDITION{RESET}")
    line("═")
    print(f"{GRAY}  Manage your items. Build your world.{RESET}")
    print()


def menu():
    print(f"{CYAN}{BOLD}  SELECT AN ACTION{RESET}")
    line("─")
    print(f"  {GREEN}[1]{RESET} 🎒  Show Inventory")
    print(f"  {YELLOW}[2]{RESET} 📦  Add Item")
    print(f"  {CYAN}[3]{RESET} 🔍  Search / View Coming Soon")
    print(f"  {RED}[4]{RESET} 🚪  Exit")
    line("─")


def pause():
    input(f"\n{GRAY}Press Enter to continue...{RESET}")


def main():
    while True:
        title()
        menu()

        choice = input(f"\n{YELLOW}  ➜ Choose an option: {RESET}").strip()

        if choice == "1":
            print(f"\n{GREEN}{BOLD}  🎒 YOUR INVENTORY{RESET}")
            line("─")
            show_inventory()
            line("─")
            pause()

        elif choice == "2":
            print(f"\n{YELLOW}{BOLD}  📦 ADD NEW ITEM{RESET}")
            line("─")

            name = input(f"  {CYAN}Item name: {RESET}").strip()

            if not name:
                print(f"{RED}  ✖ Item name cannot be empty.{RESET}")
                pause()
                continue

            try:
                quantity = int(input(f"  {CYAN}Quantity: {RESET}"))
            except ValueError:
                print(f"{RED}  ✖ Quantity must be a whole number.{RESET}")
                pause()
                continue

            if quantity <= 0:
                print(f"{RED}  ✖ Quantity must be greater than zero.{RESET}")
            else:
                print()
                add_item(name, quantity)
                print(f"{GREEN}  ✔ Item added successfully!{RESET}")

            pause()

        elif choice == "3":
            print(f"\n{YELLOW}  🔍 Search feature is coming soon!{RESET}")
            print(f"{GRAY}  Your teammate can implement this feature.{RESET}")
            pause()

        elif choice == "4":
            print()
            line("═")
            print(f"{GREEN}{BOLD}   👋 Thanks for playing, Miner!{RESET}")
            print(f"{YELLOW}      Keep mining. Keep building.{RESET}")
            line("═")
            print()
            break

        else:
            print(f"\n{RED}  ✖ Invalid option. Choose 1–4.{RESET}")
            pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}👋 Goodbye, Miner!{RESET}")
