import tkinter as tk

class FullScreenFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        parent.grid_rowconfigure(0, weight=1)  # Make the first row expandable
        parent.grid_columnconfigure(0, weight=1)  # Make the first column expandable

        self.grid(row=0, column=0, sticky="nsew")  # Frame fills all available space

        label = tk.Label(self, text="Fullscreen Frame", font=("Arial", 20))
        label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fullscreen Frame Example")
    root.geometry("400x300")

    fullscreen_frame = FullScreenFrame(root, bg="orange")
    fullscreen_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
