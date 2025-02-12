# Secret Santa 🎅🏻🎁  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
A modular, extensible, and well-tested Secret Santa assignment system with logging, error handling, and CSV support.

---

## 📌 Features  
✅ **Modular OOP Design** - Clean, structured, and extensible.  
✅ **Automated Assignments** - Ensures valid Secret Santa pairings.  
✅ **Prevents Repeats** - Avoids previous year's assignments.  
✅ **CSV Integration** - Reads and writes assignments in CSV format.  
✅ **Logging & Error Handling** - Tracks execution and handles issues.  
✅ **Unit Tested** - Ensures correctness with test cases.  

---

## 📚 Project Structure  
```
secret_santa/
├── src/
│   ├── __init__.py
│   ├── secret_santa.py       # Core Secret Santa logic
│   ├── utils.py              # Validation helpers
│   └── logger.py             # Logger setup
├── tests/
│   ├── __init__.py
│   ├── test_secret_santa.py  # Tests for SecretSanta class
│   └── test_utils.py         # Tests for utility functions
├── data/
│   ├── employees.csv          # List of employees
│   └── previous_assignments.csv  # Last year's assignments
├── logs/
│   └── secret_santa.log  # Logs output here
├── README.md            # Project documentation
├── requirements.txt     # Dependencies
└── main.py              # Entry point to run Secret Santa
```

---

## 🔧 Installation & Setup  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Mehmedx7/secret_santa.git
cd secret_santa
```

### 3️⃣ Install Dependencies(Optional)
```bash
pip install -r requirements.txt
```

### 4️⃣ Ensure Dependencies Are Up to Date  
```bash
pip install --upgrade pip
pip freeze > requirements.txt
```

---

## ▶️ Running the Secret Santa Program  
Run the script to generate assignments:  
```bash
python main.py
```
📌 **Output:** A new `data/assignments.csv` file is created with Secret Santa pairings.  

**Example CSV Output:**  
```csv
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Hamish Murray,hamish.murray@acme.com,Spencer Allen,spencer.allen@acme.com
Layla Graham,layla.graham@acme.com,Matthew King,matthew.king.jr@acme.com
...
```

---

## 🧠 Running Tests  
To verify functionality, run:  
```bash
python -m unittest discover tests -v
```
📌 **Example Test Output:**  
```
INFO - SecretSanta initialized with employees and previous assignments.
INFO - Attempt 1 to assign Secret Santa.
INFO - Secret Santa assignments completed successfully.
ok
...
Ran 8 tests in 0.003s

OK
```

---

## 📝 Solution Design & Expectations  
✅ **Modular & Extensible:**  
   - Code is structured with **separate modules** for maintainability.  
✅ **Error Handling:**  
   - Handles **invalid input, missing files**, and **incorrect data formats** gracefully.  
✅ **Automated Testing:**  
   - Includes **unit tests** for core functionality.  
✅ **Version Control:**  
   - Managed via GitHub: [Secret Santa Repo](https://github.com/Mehmedx7/secret_santa).  

---

🎅 **Enjoy Secret Santa!** 🎁  

