import os
import csv
import tkinter as tk
from tkinter import messagebox, ttk
class LinearRegression:
  """Least-squares regression implemented without an external dependency."""
  def fit(self, X, y):
    if not X or len(X) != len(y):
      raise ValueError("Training data must contain matching feature and target rows.")
    rows = [[1.0] + [float(value) for value in row] for row in X]
    columns = len(rows[0])
    if any(len(row) != columns for row in rows):
      raise ValueError("All training rows must have the same number of features.")
    augmented = [
        [sum(row[i] * row[j] for row in rows) for j in range(columns)]
        + [sum(row[i] * float(target) for row, target in zip(rows, y))]
        for i in range(columns)
    ]
    pivot_row = 0
    pivots = []
    for column in range(columns):
      if pivot_row == columns:
        break
      best = max(range(pivot_row, columns),
                 key=lambda index: abs(augmented[index][column]))
      if abs(augmented[best][column]) < 1e-12:
        continue
      augmented[pivot_row], augmented[best] = augmented[best], augmented[pivot_row]
      divisor = augmented[pivot_row][column]
      augmented[pivot_row] = [value / divisor for value in augmented[pivot_row]]
      for index in range(columns):
        if index != pivot_row:
          factor = augmented[index][column]
          augmented[index] = [
              value - factor * pivot_value
              for value, pivot_value in zip(augmented[index], augmented[pivot_row])
          ]
      pivots.append(column)
      pivot_row += 1
    self.coefficients_ = [0.0] * columns
    for index, column in enumerate(pivots):
      self.coefficients_[column] = augmented[index][-1]
    return self
  def predict(self, X):
    return [
        self.coefficients_[0] + sum(
            coefficient * float(value)
            for coefficient, value in zip(self.coefficients_[1:], row)
        )
        for row in X
    ]
class SalaryPredictorApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Employee Salary Predictor")
    self.root.geometry("450x350")
    self.root.resizable(False, False)

    # Load data and train model
    self.csv_filename = "employee_salary_data.csv"
    self.model = None
    self.edu_mapping = {"Bachelor's": 1, "Master's": 2, "PhD": 3}
    self.train_predictive_model()

    # Create UI Components
    self.create_widgets()

  def train_predictive_model(self):
    """Loads CSV, maps text labels to numbers, and fits a Linear Regression model."""
    if not os.path.exists(self.csv_filename):
      messagebox.showerror(
          "Error", f"Could not find the dataset file: '{self.csv_filename}'"
      )
      self.root.destroy()
      return
    try:
      X = []
      y = []
      with open(self.csv_filename, newline="", encoding="utf-8-sig") as csv_file:
        for row in csv.DictReader(csv_file):
          education = row["Education"].strip()
          education_num = self.edu_mapping.get(education, 1)
          X.append([education_num, float(row["Experience"])])
          y.append(float(row["Salary"]))
      self.model = LinearRegression()
      self.model.fit(X, y)
    except Exception as e:
      messagebox.showerror(
          "Training Error", f"Failed to process CSV/train model:\n{str(e)}"
      )
      self.root.destroy()
  def create_widgets(self):
    """Builds a structured graphical user interface layout."""
    main_frame = ttk.Frame(self.root, padding="20 20 20 20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    title_label = ttk.Label(
        main_frame, text="Salary Forecast Engine", font=("Arial", 16, "bold")
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="w")
    ttk.Label(main_frame, text="Education Level:", font=("Arial", 11)).grid(
        row=1, column=0, sticky="w", pady=10
    )
    self.edu_var = tk.StringVar()
    self.edu_combo = ttk.Combobox(
        main_frame,
        textvariable=self.edu_var,
        values=list(self.edu_mapping.keys()),
        state="readonly",
        width=22,
        font=("Arial", 10),
    )
    self.edu_combo.grid(row=1, column=1, sticky="w", padx=10)
    self.edu_combo.current(0)  # Default selection to Bachelor's
    ttk.Label(main_frame, text="Experience (Years):", font=("Arial", 11)).grid(
        row=2, column=0, sticky="w", pady=10
    )
    self.exp_var = tk.DoubleVar(value=1.0)
    self.exp_spin = ttk.Spinbox(
        main_frame,
        from_=0.0,
        to=50.0,
        increment=0.5,
        textvariable=self.exp_var,
        width=21,
        font=("Arial", 10),
    )
    self.exp_spin.grid(row=2, column=1, sticky="w", padx=10)
    predict_btn = ttk.Button(
        main_frame, text="Predict Salary", command=self.calculate_prediction
    )
    predict_btn.grid(row=3, column=0, columnspan=2, pady=25, ipadx=10, ipady=4)
    self.result_var = tk.StringVar(value="Predicted Salary: --")
    result_label = ttk.Label(
        main_frame,
        textvariable=self.result_var,
        font=("Arial", 13, "bold"),
        foreground="#1b5e20",
    )
    result_label.grid(row=4, column=0, columnspan=2, pady=5)
  def calculate_prediction(self):
    """Triggered on button click to handle user input values and output model math."""
    try:
      selected_edu = self.edu_var.get()
      edu_numeric = self.edu_mapping[selected_edu]
      experience = self.exp_var.get()
      if experience < 0:
        raise ValueError("Experience cannot be negative.")
      input_features = [[edu_numeric, experience]]
      predicted_salary = self.model.predict(input_features)[0]
      predicted_salary = max(0.0, predicted_salary)
      self.result_var.set(f"Predicted Salary: ${predicted_salary:,.2f}")
    except ValueError as ve:
      messagebox.showwarning("Invalid Input", f"Please check entries: {ve}")
    except Exception as e:
      messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
if __name__ == "__main__":
  # Initialize the Tkinter application lifecycle loop
  root = tk.Tk()
  app = SalaryPredictorApp(root)
  root.mainloop()