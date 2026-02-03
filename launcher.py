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
    
    # Run the main virus script
    try:
        # Get the directory where this launcher is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        virus_script = os.path.join(script_dir, 'virus.py')
        
        if not os.path.exists(virus_script):
            print("Error: virus.py not found in the same directory!")
            sys.exit(1)
            
        # Run virus.py as a separate process using the same python executable
        # This is safer than exec() as it avoids scope issues with imports
        subprocess.check_call([sys.executable, virus_script])
        
    except subprocess.CalledProcessError as e:
        # Child process failed
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
