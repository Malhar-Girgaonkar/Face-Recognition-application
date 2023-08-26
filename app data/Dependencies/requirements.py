import importlib
import subprocess

required_modules = [
    "CTkMessagebox",
    "customtkinter",
    "tkinter",
    "mysql.connector",
    "mysql"
    "PIL",
    "opencv-python",
    "os",
    "shutil"
]

def install_missing_module(module_name):
    subprocess.call(["pip", "install", module_name])

def check_and_install_dependencies():
    for module_name in required_modules:
        try:
            importlib.import_module(module_name)
            print(f"{module_name} is already installed.")
        except ImportError:
            print(f"{module_name} is not installed. Installing...")
            install_missing_module(module_name)
            print(f"{module_name} has been successfully installed.")

if __name__ == "__main__":
    check_and_install_dependencies()
