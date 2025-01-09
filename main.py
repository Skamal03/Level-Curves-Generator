import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

class LevelCurveGenerator:

    def __init__(self, func_str, x_range=(-10, 10), y_range=(-10, 10), levels=10):
        """
        func_str: The function
        x_range: Range for x-axis
        y_range: Range for y-axis
        levels: Number of level curves to display
        """
        self.func_str = func_str
        self.x_range = x_range
        self.y_range = y_range
        self.levels = levels

    def Graph(self):

        x = np.linspace(self.x_range[0], self.x_range[1], 500)
        y = np.linspace(self.y_range[0], self.y_range[1], 500)
        X, Y = np.meshgrid(x, y)  # forms the grid

        try:
            # Evaluating the function to compute Z
            Z = eval(self.func_str)
        except Exception as e:
            return f"Error evaluating function: {e}"

        # Plotting the level curves
        plt.figure(figsize=(8, 6))
        cp = plt.contour(X, Y, Z, levels=self.levels, cmap='viridis')
        plt.colorbar(cp, label="Function Value")
        plt.title(f"Level Curves for f(x, y) = {self.func_str}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()


class LevelCurveGUI:

    def __init__(self, root):
        self.root = root

        # frame
        self.root.title("Level Curve Generator")
        self.root.geometry("500x500")
        self.root.config(bg="steel blue")

        # main heading
        self.heading_label = tk.Label(root,
                                      text="Level Curve Generator",
                                      font=("Helvetica", 24, "bold"),
                                      fg="steel blue")

        self.heading_label.pack(fill="x", pady=20)

        # Function label
        self.func_label = tk.Label(root,
                                   text="Enter the function ",
                                   font=("Arial", 12, "bold"),
                                   background="steel blue",
                                   fg="white")

        self.func_label.pack(padx=10, pady=10)

        # Function entry
        self.func_entry = tk.Entry(root, width=40)
        self.func_entry.pack(padx=10, pady=10)

        # Generate button
        self.generate_button = tk.Button(root,
                                         text="Generate Level Curves",
                                         font=("Arial", 12),
                                         background="light grey",
                                         command=self.generate)
        self.generate_button.pack(pady=20)

        # Error label
        self.error_label = tk.Label(root,
                                    text="",
                                    fg="red",
                                    background="steel blue")
        self.error_label.pack(pady=20)

        # making taskbar
        self.taskbar_text = tk.StringVar()
        self.taskbar_text.set("Developed by Muhammad Sannan")

        # Create taskbar label
        self.taskbar = tk.Label(root, textvariable=self.taskbar_text, fg="black", bg="light blue", height=2)
        self.taskbar.pack(side="bottom", fill="x")

    def generate(self):
        func_str = self.func_entry.get()

        # Check if the function string is empty
        if not func_str:
            self.error_label.config(text="There is an Error in Function or is Empty!")
            return

        generator = LevelCurveGenerator(func_str)
        result = generator.Graph()

        if isinstance(result, str):
            self.error_label.config(text=result)
        else:
            self.error_label.config(text="")


root = tk.Tk()
interface = LevelCurveGUI(root)

root.mainloop()
