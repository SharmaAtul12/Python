# Contact Book
# Store, search, update, and manage your contacts

contacts = {}


def add_contact():
    name = input("Enter name: ").strip().title()
    if not name:
        print("Name cannot be empty!")
        return

    if name in contacts:
        print(f"'{name}' already exists. Use update option to modify.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()
    address = input("Enter address (optional): ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
    }
    print(f"\nContact '{name}' added successfully!")


def view_contacts():
    if not contacts:
        print("\nNo contacts found!")
        return

    print(f"\n{'Name':<20} {'Phone':<15} {'Email':<25} {'Address'}")
    print("-" * 80)
    for name in sorted(contacts):
        c = contacts[name]
        print(f"{name:<20} {c['phone']:<15} {c['email']:<25} {c['address']}")
    print(f"\nTotal contacts: {len(contacts)}")


def search_contact():
    query = input("Search by name or phone: ").strip().lower()
    if not query:
        print("Search query cannot be empty!")
        return

    results = []
    for name, info in contacts.items():
        if query in name.lower() or query in info["phone"]:
            results.append((name, info))

    if not results:
        print("No matching contacts found!")
        return

    print(f"\nFound {len(results)} result(s):")
    print(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Address'}")
    print("-" * 80)
    for name, c in results:
        print(f"{name:<20} {c['phone']:<15} {c['email']:<25} {c['address']}")


def update_contact():
    name = input("Enter the name of the contact to update: ").strip().title()
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return

    print(f"\nCurrent details for '{name}':")
    c = contacts[name]
    print(f"  Phone: {c['phone']}")
    print(f"  Email: {c['email']}")
    print(f"  Address: {c['address']}")

    print("\nLeave blank to keep current value.")
    phone = input(f"New phone [{c['phone']}]: ").strip()
    email = input(f"New email [{c['email']}]: ").strip()
    address = input(f"New address [{c['address']}]: ").strip()

    contacts[name]["phone"] = phone if phone else c["phone"]
    contacts[name]["email"] = email if email else c["email"]
    contacts[name]["address"] = address if address else c["address"]
    print(f"Contact '{name}' updated!")


def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip().title()
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
    if confirm == "y":
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Deletion cancelled.")


def export_contacts():
    if not contacts:
        print("No contacts to export!")
        return

    filename = input("Enter filename (e.g. contacts.txt): ").strip()
    if not filename:
        filename = "contacts.txt"

    with open(filename, "w") as f:
        f.write(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Address'}\n")
        f.write("-" * 80 + "\n")
        for name in sorted(contacts):
            c = contacts[name]
            f.write(f"{name:<20} {c['phone']:<15} {c['email']:<25} {c['address']}\n")

    print(f"Contacts exported to '{filename}'!")


def main():
    print("=" * 40)
    print("        CONTACT BOOK")
    print("=" * 40)

    while True:
        print("\n1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
