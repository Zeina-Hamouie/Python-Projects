"""
Skills Management Application
This script provides a command-line interface for managing skills and their progress.
"""

from my_procedure import skills_manager

def display_menu() -> str:
    """Display the main menu and get user input"""
    return input("""
What would you like to do?
's': Show all skills
'a': Add new skill
'd': Delete a skill
'u': Update a skill progress
'q': Quit the App
Your choice: """).strip().lower()

def main():
    """Main application loop"""
    commands = {
        's': skills_manager.show_skills,
        'a': skills_manager.add_skill,
        'd': skills_manager.delete_skill,
        'u': skills_manager.update_skill,
        'q': lambda: print("App is closed")
    }
    
    while True:
        choice = display_menu()
        
        if choice in commands:
            if choice == 'q':
                commands[choice]()
                skills_manager.save_close()
                break
            commands[choice]()
        else:
            print(f"Invalid command '{choice}'. Please try again.")

if __name__ == "__main__":
    main()
