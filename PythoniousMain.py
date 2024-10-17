import os
import importlib.util

## Nit Pick Variables
exit_string_command = "eq"
main_script_name = "PythoniousMain.py"

# Function to find all scripts in a directory and subdirectories
def find_scripts(base_dir):
    scripts = {}
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and file != "" :  # Exclude the main script
                script_name = os.path.splitext(file)[0] # Add the script to the dictionary
                scripts[script_name] = os.path.join(root, file)
    return scripts

# Function to run a script dynamically
def run_script(script_path):
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is not None:
        spec.loader.exec_module(module)
    else:
        print(f"Could not load module from {script_path}")

# CLI to select a script
def main():
    base_dir = os.path.dirname(__file__)
    scripts = find_scripts(base_dir)
    
    if not scripts:
        print("No scripts were loaded.")
        return
    
    while True:
        print("\nAvailable Scripts:")
        for i, script_name in enumerate(scripts):
            print(f"{i+1}. {script_name}")
        
        choice = input("\nEnter the script number to run (or type "+ exit_string_command+ " to quit): ")
        
        if choice.lower() == exit_string_command:
            break
        
        try:
            selected_script = list(scripts.values())[int(choice) - 1]
            print(f"Running {selected_script}...")
            run_script(selected_script)
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
