"""
Auto-installing launcher for virus.py
This script automatically installs required dependencies and runs the main script
"""
import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])

def main():
    # Check and install required packages
    required_packages = ['keyboard']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} already installed")
        except ImportError:
            print(f"✗ {package} not found, installing...")
            try:
                install_package(package)
                print(f"✓ {package} installed successfully")
            except Exception as e:
                print(f"✗ Failed to install {package}: {e}")
                sys.exit(1)
    
    print("\n" + "="*50)
    print("All dependencies installed! Starting script...")
    print("="*50 + "\n")
    
    # Import and run the main virus script
    try:
        # Get the directory where this launcher is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        virus_script = os.path.join(script_dir, 'virus.py')
        
        # Execute the virus.py script
        with open(virus_script, 'r', encoding='utf-8') as f:
            code = f.read()
        exec(code)
    except FileNotFoundError:
        print("Error: virus.py not found in the same directory!")
        sys.exit(1)
    except Exception as e:
        print(f"Error running script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
