import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from py.game_engine import Engine
from py.ui_cli import CLI, clear_screen
from py.save_manager import SaveManager
from py.tutorial import get_tip

def main():
    engine = Engine()
    ui = CLI()
    saver = SaveManager()
    clear_screen()
    print("Welcome to Lemonade Tycoon (CLI Edition)")
    input("Press Enter to Start...")
    while True:
        clear_screen()
        ui.render_header(engine.state)
        if engine.state.last_turn_log:
            print("\nLAST MONTH REPORT:")
            for log in engine.state.last_turn_log:
                print(f" > {log}")
            print("")
        ui.render_menu()
        choice = ui.get_input()
        if choice == '1':
            try:
                p = float(input("New Price: "))
                engine.state.price = p
            except: print("Invalid number")
        elif choice == '2':
            try:
                amt = int(input("Amount to buy: "))
                success, msg = engine.buy_inventory(amt)
                print(msg)
                if not success: input("Press Enter...")
            except: print("Invalid number")
        elif choice == '3':
            try:
                m = float(input("New Marketing Budget: "))
                engine.state.marketing_spend = m
            except: print("Invalid number")
        elif choice == '4':
            print(engine.hire_employee())
        elif choice == '5':
            print(engine.fire_employee())
        elif choice == '6':
            print(engine.take_loan(1000))
        elif choice == '7':
            print(engine.repay_loan(1000))
        elif choice == '8':
            logs = engine.process_turn()
            print("\n-- Processing Turn --")
            print(f"Tip: {get_tip('cash')}")
            input("Press Enter to continue...")
        elif choice == '9':
            sub = input("(S)ave or (L)oad? ").lower()
            if sub == 's':
                saver.save_to_file(engine.state, 'saves/savegame.json')
                print("Game Saved.")
            elif sub == 'l':
                st = saver.load_from_file('saves/savegame.json')
                if st: engine.state = st
                print("Game Loaded.")
            input("Wait...")
        elif choice == '0':
            break

if __name__ == "__main__":
    main()