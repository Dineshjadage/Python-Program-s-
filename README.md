# README: Downloading a Git Repository & Opening .py Files in IDLE

## Downloading a Git Repository

### Windows
1. Install [Git for Windows](https://git-scm.com/download/win) if not already installed.
2. Open **Git Bash** or **Command Prompt**.
3. Navigate to the directory where you want to clone the repository:
   ```sh
   cd path/to/your/directory
   ```
4. Clone the repository using:
   ```sh
   git clone https://github.com/username/repository.git
   ```
5. Navigate into the cloned repository:
   ```sh
   cd repository
   ```

### Linux
1. Open Terminal.
2. Ensure Git is installed:
   ```sh
   sudo apt update && sudo apt install git  # Debian/Ubuntu
   sudo yum install git  # CentOS/RHEL
   sudo dnf install git  # Fedora
   ```
3. Navigate to the desired directory:
   ```sh
   cd /path/to/your/directory
   ```
4. Clone the repository:
   ```sh
   git clone https://github.com/username/repository.git
   ```
5. Enter the repository folder:
   ```sh
   cd repository
   ```

### Mac
1. Open Terminal.
2. Install Git if not installed:
   ```sh
   brew install git  # Using Homebrew
   ```
3. Navigate to the target directory:
   ```sh
   cd /path/to/your/directory
   ```
4. Clone the repository:
   ```sh
   git clone https://github.com/username/repository.git
   ```
5. Navigate into the repository:
   ```sh
   cd repository
   ```

## Opening .py Files with IDLE

### Windows
1. Right-click on the `.py` file.
2. Select **Open With** > **Choose another app**.
3. Choose **IDLE (Python x.x)** from the list.
4. Check **Always use this app to open .py files** (optional).
5. Click **OK**.

Alternatively, open IDLE and use **File > Open** to browse and open the file.

### Linux & Mac
1. Open Terminal.
2. Run the following command:
   ```sh
   idle3 filename.py  # For Python 3
   idle filename.py   # For Python 2 (if installed)
   ```

Alternatively, open IDLE and navigate to **File > Open** to browse for the file.

---

## Contributing
Feel free to open an issue or pull request if you have any suggestions!

## License
This project is licensed under the MIT License.

