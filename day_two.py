# day_two.py

# 1. Classes and Objects (The blueprint)
class AIAgent:
    # The __init__ method is the constructor. 
    # 'self' must be the first parameter in instance methods.
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.is_active = True

    def status_report(self) -> str:
        # A simple one-line if/else (Python's ternary operator)
        state = "Online" if self.is_active else "Offline"
        return f"[{state}] {self.name} is ready for {self.role} tasks."

# 2. Inheritance (Building on the AIAgent class)
class CodingAgent(AIAgent):
    def __init__(self, name: str, language: str):
        # super() calls the parent class constructor to set name and role
        super().__init__(name, role="Backend Development")
        self.language = language

    def write_code(self, task: str):
        print(f"{self.name} is writing {self.language} code for: {task}")

# 3. Error Handling (try / except blocks)
def assign_critical_task(agent: AIAgent, task_id):
    print(f"\nAttempting to assign task {task_id} to {agent.name}...")
    try:
        if type(task_id) is not int:
            # Manually triggering an error if the input is wrong
            raise TypeError("Task ID must be an integer!")
        print(f"Success: Task #{task_id} assigned.")
    
    except TypeError as error:
        # Catching the specific error we raised
        print(f"Error caught: {error}")
    
    finally:
        # This block runs no matter what happens
        print("Task assignment process concluded.")

# --- Execution Section ---

# Instantiating objects from our classes
manager = AIAgent(name="Overseer", role="Task Delegation")
developer = CodingAgent(name="DevBot-X", language="Python")

# Calling methods
print(manager.status_report())
print(developer.status_report())
developer.write_code("REST API Routing")

# Testing the error handling
assign_critical_task(manager, 101)        # This will succeed (101 is an integer)
assign_critical_task(developer, "abc")    # This will trigger the exception (string instead of int)
