import tkinter as tk
from tkinter import messagebox
import winreg

def apply_changes():
    key_path = winreg.HKEY_CURRENT_USER
    subkey_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
    
    try:
        key = winreg.OpenKey(key_path, subkey_path, 0, winreg.KEY_READ | winreg.KEY_WRITE)
            
        try:
            # Verify if BingSearchEnabled exists
            value, type = winreg.QueryValueEx(key, "BingSearchEnabled")
        except FileNotFoundError:
            # If it doesn't exist, create it
            winreg.SetValueEx(key, "BingSearchEnabled", 0, winreg.REG_DWORD, 0)
        try:
            # Verify if CortanaConsent exists
            value, type = winreg.QueryValueEx(key, "CortanaConsent")
        except FileNotFoundError:
            # If it doesn't exist, create it
            winreg.SetValueEx(key, "CortanaConsent", 0, winreg.REG_DWORD, 0)
        
        messagebox.showinfo("Info", "The web search is disable.")
        winreg.CloseKey(key)
    
    except FileNotFoundError:
        messagebox.showerror("Error", "Registry key not found.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied. Run as administrator.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def delete_registry_key():
    key_path = winreg.HKEY_CURRENT_USER
    subkey_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
    
    try:
        key = winreg.OpenKey(key_path, subkey_path, 0, winreg.KEY_READ | winreg.KEY_WRITE)
        
        # Delete the registry keys if they exist
        try:
            winreg.DeleteValue(key, "BingSearchEnabled")
        except FileNotFoundError:
            # Dont send any message if it does not exist
            pass
        
        try:
            winreg.DeleteValue(key, "CortanaConsent")
        except FileNotFoundError:
            # Dont send any message if it does not exist
            pass
        
        messagebox.showinfo("Info", "The web search is enabled.")
        winreg.CloseKey(key)

    except FileNotFoundError:
        messagebox.showerror("Error", "Registry key not found.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied. Run as administrator.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            

# Create the main window

root = tk.Tk()
root.title("Web search settings")
root.geometry("300x150")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Disable web search in Windows 10", bg="#f0f0f0", font=("Arial", 12))
label.pack(pady=10)# Replace with your icon file path

apply_button = tk.Button(root, text="Disable web search", command=apply_changes)
apply_button.pack(pady=5)

delete_button = tk.Button(root, text="Active web search", command=delete_registry_key)
delete_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()