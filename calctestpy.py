def calculator():
  # This function performs the calculation
  def calculate():
    # Get the values and operator
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = entry3.get()
    
    # Perform the calculation
    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      result = num1 / num2
      
    # Clear the entries and set the result
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry1.insert(0, result)
  
  # Create the UI
  import tkinter as tk
  window = tk.Tk()
  window.title("Calculator")
  
  # Create the entries for the numbers and operator
  entry1 = tk.Entry(window)
  entry2 = tk.Entry(window)
  entry3 = tk.Entry(window)
  
  # Create the button for the equals sign
  button = tk.Button(window, text="=", command=calculate)
  
  # Create the labels for the numbers and operator
  label1 = tk.Label(window, text="Number 1:")
  label2 = tk.Label(window, text="Number 2:")
  label3 = tk.Label(window, text="Operator (+, -, *, /):")
  
  # Place the widgets in the UI
  label1.grid(row=0, column=0)
  entry1.grid(row=0, column=1)
  label2.grid(row=1, column=0)
  entry2.grid(row=1, column=1)
  label3.grid(row=2, column=0)
  entry3.grid(row=2, column=1)
  button.grid(row=3, column=0, columnspan=2)
  
  # Run the main loop
  tk.mainloop()

# Run the calculator function
calculator()