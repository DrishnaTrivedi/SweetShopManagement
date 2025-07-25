# Sweet Shop Management System

A simple Python-based Sweet Shop Management System built using **Test-Driven Development (TDD)**. The system allows adding, deleting, viewing, searching, sorting, purchasing, and restocking sweets.


## 📦 Features

- ✅ Add new sweets to the inventory
- ✅ Delete existing sweets by ID
- ✅ View all available sweets
- ✅ Search sweets by:
  - Name
  - Category
  - Price range
- ✅ Sort sweets by:
  - Name (A-Z)
  - Price (Low to High)
- ✅ Purchase sweets (with stock validation)
- ✅ Restock sweets
- ✅ All functionality fully covered by unit tests



## 🔧 Tech Stack

- **Language:** Python 3.x
- **Testing:** Pytest
- **Development Style:** Test-Driven Development (TDD)

## ✅ Test Coverage
- This project uses pytest with coverage.py to ensure code reliability and thorough testing.

- ✅ Overall Coverage: 92%

- 📄 Tested Modules: All core modules including SweetShop, Sweet, and custom errors.

- 🧪 Testing Includes:

- Adding, deleting, updating, and retrieving sweets.

- Sorting and searching sweets.

- Edge cases like duplicate IDs, not found errors, and stock validations.



## 🔧 Setup

- [git clone](https://github.com/DrishnaTrivedi/SweetShopManagement.git)
- pip install -r requirements.txt

## Run tests

- pytest -v
- pytest -v > test_report.txt

 ## To generate a new coverage report 

- pytest --cov=app --cov-report=html

## Open coverage report at
 - htmlcov/index.html





Some sections of the README and boilerplate code were enhanced using AI tools like ChatGPT for better clarity and structure.

