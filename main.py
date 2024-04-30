import tkinter as tk
from ui import BreastCancerExpertSystemUI

def main():
    root = tk.Tk()
    app = BreastCancerExpertSystemUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
