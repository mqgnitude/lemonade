import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class CLI:
    def render_header(self, state):
        print(f"--- Year {state.year} | Month {state.month} ---")
        print(f"Cash: ${state.cash:,.2f} | Inventory: {state.inventory}")
        print(f"Price: ${state.price:.2f} | Marketing: ${state.marketing_spend:.2f}")
        print(f"Employees: {state.employees} | Loan: ${state.loan_balance:,.2f}")
        print("-" * 40)

    def render_menu(self):
        print("1. Set Price")
        print("2. Buy Inventory")
        print("3. Set Marketing Budget")
        print("4. Hire Employee")
        print("5. Fire Employee")
        print("6. Take Loan ($1000)")
        print("7. Repay Loan ($1000)")
        print("8. End Turn")
        print("9. Save/Load")
        print("0. Quit")

    def get_input(self):
        return input("Choice > ")