import sqlite3

class SkillsManager:
    """Class to manage skills database operations"""
    
    def __init__(self, db_name: str = "Skills.db"):
        """Initialize database connection"""
        self.db_name = db_name
        self.user_id = 1
        self.connection = None
        self.cursor = None
        self.connect_db()
        
    def connect_db(self) -> None:
        """Establish database connection and create table if not exists"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self._create_table()
            print("Connected to Database")
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            
    def _create_table(self) -> None:
        """Create skills table if it doesn't exist"""
        sql_command = '''
        CREATE TABLE IF NOT EXISTS skills(
            skill_name VARCHAR(20) NOT NULL,
            progress INTEGER CHECK(progress BETWEEN 0 AND 100),
            User_ID INTEGER,
            UNIQUE(skill_name, User_ID)
        )
        '''
        self.cursor.execute(sql_command)
            
    def save_close(self) -> None:
        """Save changes and close database connection"""
        try:
            if self.connection:
                self.connection.commit()
                self.connection.close()
                print("Database connection is closed")
        except sqlite3.Error as e:
            print(f"Error while closing database: {e}")

    def show_skills(self) -> None:
        """Display all skills for the current user"""
        try:
            self.cursor.execute("SELECT skill_name, progress FROM skills WHERE User_ID = ?", (self.user_id,))
            results = self.cursor.fetchall()
            if not results:
                print("No skills found")
                return
                
            print(f"\nYou have {len(results)} Skills:")
            for skill_name, progress in results:
                print(f"- {skill_name}: {progress}%")
        except sqlite3.Error as e:
            print(f"Error retrieving skills: {e}")

    def add_skill(self) -> None:
        """Add a new skill with progress"""
        try:
            skill_name = input("Input the name of a new skill: ").strip().capitalize()
            if not skill_name:
                print("Skill name cannot be empty")
                return
                
            progress = input("Input the progress (0-100): ").strip()
            if not progress.isdigit() or not (0 <= int(progress) <= 100):
                print("Progress must be a number between 0 and 100")
                return
                
            self.cursor.execute(
                "INSERT INTO skills (skill_name, progress, User_ID) VALUES (?, ?, ?)",
                (skill_name, int(progress), self.user_id)
            )
            self.connection.commit()
            print(f"Skill '{skill_name}' added successfully")
        except sqlite3.IntegrityError:
            print("This skill already exists")
        except sqlite3.Error as e:
            print(f"Error adding skill: {e}")

    def update_skill(self) -> None:
        """Update progress for an existing skill"""
        try:
            skill_name = input("Input the name of the skill: ").strip().capitalize()
            if not skill_name:
                print("Skill name cannot be empty")
                return
                
            # Check if skill exists
            self.cursor.execute("SELECT 1 FROM skills WHERE skill_name = ? AND User_ID = ?",
                              (skill_name, self.user_id))
            if not self.cursor.fetchone():
                print(f"Skill '{skill_name}' not found")
                return
                
            progress = input("Input the new progress (0-100): ").strip()
            if not progress.isdigit() or not (0 <= int(progress) <= 100):
                print("Progress must be a number between 0 and 100")
                return
                
            self.cursor.execute(
                "UPDATE skills SET progress = ? WHERE skill_name = ? AND User_ID = ?",
                (int(progress), skill_name, self.user_id)
            )
            self.connection.commit()
            print(f"Skill '{skill_name}' updated successfully")
        except sqlite3.Error as e:
            print(f"Error updating skill: {e}")

    def delete_skill(self) -> None:
        """Delete an existing skill"""
        try:
            skill_name = input("Input the name of the skill to delete: ").strip().capitalize()
            if not skill_name:
                print("Skill name cannot be empty")
                return
                
            self.cursor.execute(
                "DELETE FROM skills WHERE skill_name = ? AND User_ID = ?",
                (skill_name, self.user_id)
            )
            if self.cursor.rowcount > 0:
                self.connection.commit()
                print(f"Skill '{skill_name}' deleted successfully")
            else:
                print(f"Skill '{skill_name}' not found")
        except sqlite3.Error as e:
            print(f"Error deleting skill: {e}")

# Create global instance
skills_manager = SkillsManager()

# These functions are kept for backward compatibility
def save_close(): skills_manager.save_close()
def show_skills(): skills_manager.show_skills()
def add_skill(): skills_manager.add_skill()
def update_skill(): skills_manager.update_skill()
def delete_skill(): skills_manager.delete_skill()