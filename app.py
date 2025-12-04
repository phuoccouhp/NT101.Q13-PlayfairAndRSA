from tkinter import *
from gui.main_menu import MainMenu

def main():
    root = Tk()
    root.geometry("1220x660")
    root.title("Cryptography Toolkit")

    # Hiển thị màn hình main menu
    MainMenu(root)

    root.mainloop()

if __name__ == "__main__":
    main()
