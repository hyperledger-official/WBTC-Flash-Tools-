import subprocess
import os

def run_protected_script():
    script_path = os.path.join(os.path.dirname(__file__), 'protected_script.py')
    if os.path.exists(script_path):
        subprocess.run(['python', script_path])
    else:
        print("protected_script.py not found.")

if __name__ == "__main__":
    run_protected_script()
