
import tkinter as tk  # Imports the built-in Tkinter library for GUI design, aliasing it as tk for shorter syntax.

class Calculator:  # Defines a blueprint class called Calculator to manage the logic and UI structure.
    def __init__(self, root):  # The initialization method that runs automatically when a new calculator object is created. It takes the main window (root) as an argument.
        self.root = root  # Saves a reference to the main window container inside the class.
        self.root.title("Calculator")  # Sets the text that appears in the title bar of the application window.
        self.root.geometry("350x500")  # Defines the starting dimensions of the window as 350 pixels wide by 500 pixels high.
        self.root.configure(bg="#17171c")  # Adjusts the main window background color to a sleek dark charcoal gray hex color.
        self.root.resizable(False, False)  # Disables window resizing for both width and height, preventing the layout from warping.

        self.expression = ""  # Initializes an empty string that will act as the internal text record tracking the math problem (e.g., "7*8+2").

        # Display Screen Setup
        self.display_var = tk.StringVar(value="0")  # Creates a special dynamic Tkinter string variable used to automatically push updates to labels, defaulting it to "0".
        self.create_display()  # Executes the internal helper method to construct the top portion screen area.

        # Buttons Layout Setup
        self.create_buttons()  # Executes the internal helper method to lay out the operational grid of buttons.

        # Keyboard Bindings Setup
        self.bind_keys()  # Executes the internal helper method to connect real keyboard buttons to the program actions.

    def create_display(self):  # Helper method dedicated to initializing the visual display area layout.
        display_frame = tk.Frame(self.root, bg="#17171c")  # Generates an invisible layout box component (Frame) at the top of the main window to isolate the text screen.
        display_frame.pack(expand=True, fill="both")  # Places the frame into the window, allowing it to dynamically stretch and fill all available top space.

        # Configures a text label container to show characters, binding it to self.display_var, anchoring text to the right side (e), using a large 36pt font, and making text white (#ffffff).
        display_label = tk.Label(
            display_frame, 
            textvariable=self.display_var, 
            anchor="e", 
            bg="#17171c", 
            fg="#ffffff", 
            padx=24, 
            font=("Arial", 36, "bold")
        )
        display_label.pack(expand=True, fill="both")  # Places the label securely inside its parent frame, taking up all matching grid space.

    def create_buttons(self):  # Helper method dedicated to generating and building the button grid.
        buttons_frame = tk.Frame(self.root, bg="#17171c")  # Generates another invisible layout frame strictly to hold the interactive keypad buttons.
        buttons_frame.pack(expand=True, fill="both")  # Places the button keypad wrapper below the screen, stretching to fill the remaining lower half.

        for i in range(5):  # Loops 5 times to distribute vertical grid rows evenly...
            buttons_frame.rowconfigure(i, weight=1)  # ...ensuring they scale proportionally if needed.
        for j in range(4):  # Loops 4 times to distribute horizontal columns evenly...
            buttons_frame.columnconfigure(j, weight=1)  # ...guaranteeing perfect alignment.

        # Defines a hardcoded structural map containing tuples representing each button's (Text label, row index, column index, hex color code).
        button_layout = [
            ('C', 0, 0, '#4e4e54'), ('±', 0, 1, '#4e4e54'), ('%', 0, 2, '#4e4e54'), ('/', 0, 3, '#ff9f0a'),
            ('7', 1, 0, '#2c2c2e'), ('8', 1, 1, '#2c2c2e'), ('9', 1, 2, '#2c2c2e'), ('*', 1, 3, '#ff9f0a'),
            ('4', 2, 0, '#2c2c2e'), ('5', 2, 1, '#2c2c2e'), ('6', 2, 2, '#2c2c2e'), ('-', 2, 3, '#ff9f0a'),
            ('1', 3, 0, '#2c2c2e'), ('2', 3, 1, '#2c2c2e'), ('3', 3, 2, '#2c2c2e'), ('+', 3, 3, '#ff9f0a'),
            ('0', 4, 0, '#2c2c2e'), ('.', 4, 2, '#2c2c2e'), ('=', 4, 3, '#ff9f0a')
        ]

        for text, row, col, color in button_layout:  # Steps line-by-line through the mapping list to construct each unique button.
            colspan = 2 if text == '0' else 1  # Evaluates if the loop is processing the zero button; if yes, it stretches across 2 columns instead of 1.
            
            # Instantiates a Tkinter button widget with specific parameters (text, border-free styling, hover active colors).
            btn = tk.Button(
                buttons_frame, 
                text=text, 
                bg=color, 
                fg="#ffffff", 
                font=("Arial", 18), 
                bd=0, 
                relief="flat",
                activebackground="#5e5e64" if color != '#ff9f0a' else "#cc7f08",
                activeforeground="#ffffff",
                command=lambda t=text: self.on_button_click(t)  # Generates an inline function on the fly. When pressed, it forwards that specific button's letter or number to the handling logic.
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)  # Snaps the newly created button into the invisible grid system, anchoring it to stretch in all directions (nsew) with a 1-pixel gap boundary.

    def on_button_click(self, char):  # High-level traffic controller method executing rules depending on which character was selected.
        if char == 'C':  # Triggers if the 'Clear' button is hit...
            self.expression = ""  # ...resets the internal math tracker string to empty...
            self.display_var.set("0")  # ...and drops the display to 0.
        elif char == '=':  # Triggers if the equal key is hit...
            self.evaluate_expression()  # ...shifts the operation to the mathematical parsing engine.
        elif char == '±':  # Triggers if the sign inversion button is tapped.
            if self.expression:  # If there is an active expression...
                if self.expression.startswith('-'):  # ...and it already begins with a negative sign...
                    self.expression = self.expression[1:]  # ...strips away that negative sign.
                else:
                    self.expression = '-' + self.expression  # Prepends a negative character symbol to the front if the string is currently positive.
                self.display_var.set(self.expression)  # Immediately reflects the updated tracking formula on the UI screen.
        elif char == '%':  # Triggers when the percentage modifier icon is used.
            if self.expression:
                try:
                    val = float(eval(self.expression)) / 100  # Safely evaluates the active operation, divides the snapshot result by 100 to yield a percentage decimal fraction...
                    self.expression = str(val)  # ...saves the decimal fraction as the new expression...
                    self.display_var.set(self.expression)  # ...and displays it.
                except Exception:
                    self.display_var.set("Error")  # Catches logical calculation failures here and writes "Error" out to the user instead of breaking the app.
                    self.expression = ""  # Wipes the broken expression.
        else:  # Handles normal number entries and symbol modifiers (+, -, *, /).
            if self.display_var.get() == "0" and char not in ['+', '-', '*', '/']:  # Checks if the display is currently resting on a default 0. If a number is typed...
                self.expression = char  # ...it overwrites that zero rather than chaining onto it.
            else:
                self.expression += char  # Appends the newly chosen digit or sign symbol directly onto the growing internal calculation string.
            self.display_var.set(self.expression)  # Updates the calculator panel display to match the active equation string.

    def evaluate_expression(self):  # Computes the final mathematical result of the built string.
        try:
            result = eval(self.expression)  # Leverages Python's internal core evaluation engine eval() to translate the formula string into a number output.
            if isinstance(result, float) and result.is_integer():  # Safely determines if a floating-point result ends with a flat decimal (like 5.0)...
                result = int(result)  # ...and converts it to a standard whole integer (5).
            self.expression = str(result)  # Converts the outcome back to readable characters, saving it so operations can continue using it...
            self.display_var.set(self.expression)  # ...and prints it onto the UI screen.
        except ZeroDivisionError:  # Catches explicit mathematical division by zero faults...
            self.display_var.set("Error (Div by 0)")  # ...printing a clear custom notice on the display screen.
            self.expression = ""  # Wipes out the current calculation sequence.
        except Exception:  # Acts as a secondary generic safety net for malformed arithmetic...
            self.display_var.set("Error")  # ...showing "Error"...
            self.expression = ""  # ...and wiping variables.

    def bind_keys(self):  # Helper method matching hardware keyboard clicks to application behaviors.
        self.root.bind('<Return>', lambda event: self.evaluate_expression())  # Maps the desktop Enter key to match hitting the equal symbol button.
        self.root.bind('<Escape>', lambda event: self.on_button_click('C'))  # Maps the desktop Escape key to serve as hitting the 'Clear' command.
        self.root.bind('<BackSpace>', lambda event: self.handle_backspace())  # Links the computer Backspace button to drop individual characters.
        
