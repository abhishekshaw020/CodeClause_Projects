import tkinter as tk
import time
import difflib

class TypingSpeedCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Calculator")
        
        self.words = "English has two articles: the and a/an. The is used to refer to specific or particular nouns; a/an is used to modify non-specific or non-particular nouns. We call the the definite article and a/an the indefinite article."
        self.words_list = self.words.split()
        
        self.start_time = None
        
        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.master, text="Type the following text:")
        self.instruction_label.grid(row=0, column=0, padx=10, pady=10)

        self.words_label = tk.Label(self.master, text=self.words)
        self.words_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.input_entry = tk.Entry(self.master, width=50)
        self.input_entry.grid(row=2, column=0, padx=10, pady=10)
        self.input_entry.bind("<Return>", self.check_typing)
        
        self.start_button = tk.Button(self.master, text="Start Typing", command=self.start_typing)
        self.start_button.grid(row=3, column=0, padx=10, pady=10)
        
        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_typing)
        self.reset_button.grid(row=5, column=0, padx=10, pady=10)

    def start_typing(self):
        self.input_entry.focus_set()
        self.start_time = time.time()
        self.result_label.config(text="")

    def check_typing(self, event):
        end_time = time.time()
        time_taken = end_time - self.start_time
        
        user_input = self.input_entry.get().lower()  # Convert to lowercase for comparison
        typed_words = user_input.split()
        
        correct_words = 0
        feedback = ""
        for typed_word, expected_word in zip(typed_words, self.words_list):
            # Using SequenceMatcher from difflib to find similarity ratio
            similarity_ratio = difflib.SequenceMatcher(None, typed_word, expected_word.lower()).ratio()
            if similarity_ratio >= 0.8:  # Consider a match if similarity ratio is high
                correct_words += 1
            else:
                feedback += f"Expected: {expected_word}\n"
        
        total_words = len(self.words_list)
        accuracy = (correct_words / total_words) * 100
        
        # Calculate speed in words per minute (WPM)
        if time_taken > 0:  # Avoid division by zero
            words_per_minute = int((correct_words / time_taken) * 60)
            # Set a maximum speed limit (adjust as needed)
            words_per_minute = min(words_per_minute, 30)
        else:
            words_per_minute = 0
        
        self.result_label.config(text=f"Accuracy: {accuracy:.2f}%\nSpeed: {words_per_minute} WPM\n{feedback}")

    def reset_typing(self):
        self.input_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None

def main():
    root = tk.Tk()
    app = TypingSpeedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
