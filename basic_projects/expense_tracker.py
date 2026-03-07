# Expense Tracker
# Track daily expenses, view summaries, and manage your budget

from datetime import datetime

expenses = []


def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Invalid amount!")
        return

    categories = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")

    try:
        choice = int(input("Select category: "))
        if not 1 <= choice <= len(categories):
            print("Invalid choice!")
            return
        category = categories[choice - 1]
    except ValueError:
        print("Invalid input!")
        return

    note = input("Add a note (optional): ").strip()
    date_str = input("Date (DD-MM-YYYY) or press Enter for today: ").strip()

    if date_str:
        try:
            date = datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format!")
            return
    else:
        date = datetime.now()

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date,
    }
    expenses.append(expense)
    print(f"\nAdded: ₹{amount:.2f} under '{category}' on {date.strftime('%d-%m-%Y')}")


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    print(f"\n{'No.':<5} {'Date':<12} {'Category':<15} {'Amount':>10}  {'Note'}")
    print("-" * 60)
    for i, exp in enumerate(expenses, 1):
        print(f"{i:<5} {exp['date'].strftime('%d-%m-%Y'):<12} {exp['category']:<15} ₹{exp['amount']:>9.2f}  {exp['note']}")

    total = sum(exp["amount"] for exp in expenses)
    print("-" * 60)
    print(f"{'TOTAL':<33} ₹{total:>9.2f}")


def category_summary():
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    summary = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    total = sum(summary.values())

    print(f"\n{'Category':<15} {'Amount':>10}  {'Percentage':>10}")
    print("-" * 40)
    for cat in sorted(summary, key=summary.get, reverse=True):
        pct = (summary[cat] / total) * 100
        bar = "█" * int(pct // 5)
        print(f"{cat:<15} ₹{summary[cat]:>9.2f}  {pct:>6.1f}%  {bar}")
    print("-" * 40)
    print(f"{'Total':<15} ₹{total:>9.2f}")


def monthly_summary():
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    monthly = {}
    for exp in expenses:
        key = exp["date"].strftime("%B %Y")
        monthly[key] = monthly.get(key, 0) + exp["amount"]

    print(f"\n{'Month':<20} {'Amount':>10}")
    print("-" * 32)
    for month, amount in sorted(monthly.items()):
        print(f"{month:<20} ₹{amount:>9.2f}")


def delete_expense():
    view_expenses()
    if not expenses:
        return

    try:
        idx = int(input("\nEnter expense number to delete: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            print(f"Deleted: ₹{removed['amount']:.2f} - {removed['category']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Invalid input!")


def budget_check():
    try:
        budget = float(input("Enter your monthly budget: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    current_month = datetime.now().strftime("%B %Y")
    spent = sum(exp["amount"] for exp in expenses if exp["date"].strftime("%B %Y") == current_month)
    remaining = budget - spent

    print(f"\n--- Budget Report for {current_month} ---")
    print(f"  Budget:    ₹{budget:.2f}")
    print(f"  Spent:     ₹{spent:.2f}")
    print(f"  Remaining: ₹{remaining:.2f}")

    if remaining < 0:
        print(f"  ⚠ You are ₹{abs(remaining):.2f} over budget!")
    elif remaining < budget * 0.2:
        print(f"  ⚠ Warning: Less than 20% budget remaining!")
    else:
        print(f"  ✓ You're within budget.")


def main():
    print("=" * 40)
    print("      EXPENSE TRACKER")
    print("=" * 40)

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Delete Expense")
        print("6. Budget Check")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            budget_check()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
