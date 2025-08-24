# 💰 Smart Personal Finance Tracker

A **command-line Python application** to track your expenses, manage budgets, and generate insightful reports — complete with visualizations and export functionality.

---

## 🚀 Features
- **Expense Management**: Add, update, delete, and list expenses with categories, amounts, descriptions, and dates.
- **Budget Tracking**: Set and view category-wise budget limits with overspending alerts.
- **Reports & Insights**:
  - Spending by category (with optional date filters)
  - Weekly & monthly summaries
  - Average spending by category
  - Visualize spending using **pie charts & bar charts**
- **Export Options**: Save reports as **CSV** or **PDF**.
- **User-Friendly CLI**: Interactive, validated inputs for a smooth experience.

---

## 📦 Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/mukulchauuhan/python-ai-ml-project-based-learning.git
   cd smart-personal-finance-tracker
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the main program:
```bash
python main.py
```

Follow the interactive menu prompts to add expenses, set budgets, and generate reports.

---

## 📂 Exported Files

- CSV and PDF reports are saved in the **current working directory** by default.
- You can customize export paths in the `export_service.py` file.

---

## ⚙️ Dependencies

- Python **3.7+**
- `pandas`
- `matplotlib`
- `fpdf`

Install them with:
```bash
pip install pandas matplotlib fpdf
```

---

## 📁 Project Structure

```
finance_tracker/
├─ data/
│  └─ expenses.json
├─ main.py
├─ models/
│  ├─ budget.py
│  ├─ expense.py
│  └─ __init__.py
├─ requirements.txt
├─ services/
│  ├─ expense_service.py
│  ├─ export_service.py
│  ├─ report_service.py
│  └─ __init__.py
├─ utils/
│  ├─ file_handler.py
│  ├─ validator.py
│  └─ __init__.py
```

---

## ✨ Future Improvements

- 🔹 Add support for recurring expenses
- 🔹 Multi-user support with authentication
- 🔹 Web dashboard for reports

---

## 👨‍💻 Author

Developed with ❤️ by **[Mukul Chauhan](https://github.com/mukulchauuhan)**
