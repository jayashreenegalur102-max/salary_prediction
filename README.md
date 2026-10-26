# Employee Salary Prediction System

## 📌 Project Overview

The Employee Salary Prediction System is a Python-based machine learning project that predicts an employee's salary based on their education level and years of work experience.

The project uses a **Linear Regression algorithm** implemented from scratch using Python. It also provides a simple graphical user interface (GUI) developed using Tkinter, allowing users to enter employee details and view the predicted salary.

## 🎯 Objectives

- To predict employee salaries based on education and experience.
- To understand the working of the Linear Regression algorithm.
- To implement a machine learning model without external machine learning libraries.
- To develop a user-friendly GUI using Tkinter.
- To read employee data from a CSV file and train a prediction model.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning Algorithm:** Linear Regression
- **GUI Framework:** Tkinter
- **Data Handling:** CSV module
- **Other Modules:** OS, Messagebox, and ttk

## 📂 Project Structure

```text
Employee-Salary-Prediction/
│
├── salary_predictor.py
├── employee_salary_data.csv
└── README.md
```

**File descriptions:**

- `salary_predictor.py` – Contains the Linear Regression implementation and GUI application.
- `employee_salary_data.csv` – Contains employee education, experience, and salary data.
- `README.md` – Provides project documentation and usage instructions.

## 📊 Dataset Description

The dataset is stored in `employee_salary_data.csv` and contains the following columns:

| Column | Description |
|---|---|
| Education | Employee's education level |
| Experience | Years of work experience |
| Salary | Employee's salary |

### Sample Dataset

```csv
Education,Experience,Salary
Bachelor's,7,59600
Master's,4,61273
PhD,5,73393
Bachelor's,10,67202
Master's,11,80413
```

*Note: These are sample rows. Use your actual dataset for training and prediction.*

## ⚙️ Algorithm Used

### Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values.

In this project, the model uses two input features:

1. Education level
2. Years of experience

The education levels are converted into numerical values:

- Bachelor's = 1
- Master's = 2
- PhD = 3

The model learns the relationship between these features and salary using the **least-squares method**.

The general prediction equation is:

```text
Salary = b0 + b1 × Education + b2 × Experience
```

Where:

- `b0` represents the intercept.
- `b1` represents the education coefficient.
- `b2` represents the experience coefficient.

The trained model uses these coefficients to predict the salary of a new employee.

## 💻 Requirements

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.
- The employee salary CSV dataset.
- Tkinter, which is generally included with standard Python installations.

**No external machine learning libraries are required** because the Linear Regression algorithm is implemented directly in Python.

## 🚀 How to Run the Project

### Step 1: Download or Clone the Project

Download the project files or clone your GitHub repository.

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Check the Files

Make sure both files are present in the same folder:

- `salary_predictor.py`
- `employee_salary_data.csv`

### Step 4: Open the Terminal

In VS Code, select **Terminal → New Terminal**.

### Step 5: Run the Program

Execute the following command:

```bash
python salary_predictor.py
```

If your system uses the Python launcher, you can also try:

```bash
py salary_predictor.py
```

### Step 6: Predict the Salary

1. Select the employee's education level.
2. Enter the years of experience.
3. Click the **Predict Salary** button.
4. View the predicted salary on the screen.

## 🖥️ Features

- Simple and user-friendly graphical interface.
- Education selection using a dropdown menu.
- Experience input using a spinbox.
- Automatic model training using CSV data.
- Salary prediction using Linear Regression.
- Input validation and error messages.
- Displays the predicted salary in a readable format.

## 📈 Working Process

1. Load employee salary data from the CSV file.
2. Convert education levels into numerical values.
3. Separate the input features and salary targets.
4. Train the Linear Regression model using the least-squares method.
5. Accept education and experience from the user.
6. Predict the salary using the trained model.
7. Display the result in the Tkinter GUI.

## ⚠️ Limitations

- Prediction accuracy depends on the quality and quantity of the dataset.
- The model considers only education level and work experience.
- Education is encoded as 1, 2, and 3, which assumes a numerical relationship between education categories.
- Predicted salaries are estimates and may not reflect actual market salaries.
- The program expects the CSV file to have the required column names.

## 🔮 Future Enhancements

- Add more employee features, such as job role, location, and industry.
- Improve the education encoding method.
- Display model evaluation metrics.
- Add charts to visualize salary trends.
- Store prediction history.
- Improve the GUI design.

## 👩‍💻 Author

**Project:** Employee Salary Prediction System

**Language:** Python

**Domain:** Machine Learning

## 📄 License

This project is intended for educational and academic purposes.
