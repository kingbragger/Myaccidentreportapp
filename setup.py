import subprocess
import sys
from pathlib import Path

# Check if Python version is 3.6 or higher
if sys.version_info < (3, 6):
    print("Python 3.6 or higher is required.")
    sys.exit(1)

# Create a virtual environment
subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)

# Activate the virtual environment based on the operating system
if sys.platform == "win32":
    subprocess.run([str(Path('venv', 'Scripts', 'activate.bat'))], check=True, shell=True)
else:
    subprocess.run([str(Path('venv', 'bin', 'activate'))], check=True, shell=True)

# Install required dependencies
subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)

print("Setup completed. To activate the virtual environment, run:")
print("   On Windows: .\\venv\\Scripts\\activate")
print("   On macOS/Linux: source venv/bin/activate")
print("Then, run your app with: python app.py")
