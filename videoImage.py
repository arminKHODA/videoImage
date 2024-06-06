import os
import subprocess

def list_python_files(directory):
    python_files = [f for f in os.listdir(directory) if f.endswith('.py')]
    return python_files

def display_files(files):
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")

def get_user_selection(files):
    while True:
        try:
            selection = int(input("Select the number of the Python file you want to run: "))
            if 1 <= selection <= len(files):
                return files[selection - 1]
            else:
                print(f"Please select a number between 1 and {len(files)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_python_file(file_path):
    subprocess.run(["python", file_path], check=True)

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(current_directory, "lib")
    

    python_files = list_python_files(directory)
    
    if not python_files:
        print("No Python files found in the directory.")
        return


    display_files(python_files)


    selected_file = get_user_selection(python_files)


    file_path = os.path.join(directory, selected_file)
    run_python_file(file_path)

if __name__ == "__main__":
    main()
