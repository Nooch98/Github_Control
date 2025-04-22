import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Example Plugin")
    root.geometry("300x100")
    
    label = tk.Label(root, text="Hello, world!")
    label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()
