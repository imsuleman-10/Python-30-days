# day_one.py

# 1. Variables (Notice: just assign the value, Python figures out the type)
project_name = "AI Agent Backend"
days_remaining = 30
is_learning = True

# 2. Lists (Like TS arrays) and Dictionaries (Like TS objects)
tech_stack = ["Python", "FastAPI", "LangChain"]
developer_profile = {
    "role": "Backend Engineer",
    "machine": "ThinkBook",
    "languages": ["TypeScript", "Python"]
}

# 3. Functions (Defined with 'def'. Indentation is strictly required!)
def start_training(days: int, project: str) -> str:
    # Python supports type hinting (like the : int and -> str above)
    if days <= 0:
        return "Time's up!"
    else:
        # f-strings are like JS template literals (` `), but with an 'f' in front
        return f"Starting day 1 of {days} for the {project} project."

# 4. Loops and Control Flow
print(start_training(days_remaining, project_name))

print("\n--- Current Stack ---")
# A standard for-in loop iterating over a list
for tech in tech_stack:
    if tech == "Python":
        print(f"> {tech} (Initializing...)")
    else:
        print(f"> {tech} (Pending...)")

print("\n--- Profile ---")
# Iterating through a dictionary requires .items() to get both key and value
for key, value in developer_profile.items():
    print(f"{key.capitalize()}: {value}")
