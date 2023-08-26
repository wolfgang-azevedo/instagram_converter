# Instagram JSON to CSV Converter

# Developed by: Wolfgang Azevedo
# GitHub: https://github.com/wolfgang-azevedo/instagram_converter
# Version: 1.0

import json
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, Button, Label, PhotoImage

def load_multiple_json_files():
    filepaths = filedialog.askopenfilenames(title="Select both Following and Followers JSON files", filetypes=[("JSON files", "*.json")])
    
    if len(filepaths) != 2:
        messagebox.showerror("Error", "Please select both Following and Followers JSON files.")
        return None, None
    
    with open(filepaths[0], 'r') as file_1, open(filepaths[1], 'r') as file_2:
        data_1 = json.load(file_1)
        data_2 = json.load(file_2)
        
        if "relationships_following" in data_1:
            return data_2, data_1
        else:
            return data_1, data_2

def save_to_csv(data):
    keys = ["URL", "Profile", "Following back", "Type"]
    filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not filepath:
        return None
    with open(filepath, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, keys)
        writer.writeheader()
        writer.writerows(data)
    return filepath

def convert():
    followers_data, following_data = load_multiple_json_files()
    if not followers_data or not following_data:
        return

    followers_data_list = [string_data["value"] for relationship in followers_data for string_data in relationship.get("string_list_data", [])]

    all_data_list = []
    for relationship in following_data.get("relationships_following", []):
        for string_data in relationship.get("string_list_data", []):
            profile_type = "both" if string_data["value"] in followers_data_list else "following"
            all_data_list.append({
                "URL": string_data["href"],
                "Profile": string_data["value"],
                "Following back": "Yes" if string_data["value"] in followers_data_list else "No",
                "Type": profile_type
            })

    dest_path = save_to_csv(all_data_list)
    if dest_path:
        saved_file_label.config(text=f"Saved to: {dest_path}")

root = tk.Tk()
root.title("Instagram JSON to CSV converter")

# Colors and fonts for the instruction label
header_font = ("Arial", 14, "bold")
body_font = ("Arial", 12)
header_color = "#3D3D3D"  # dark gray
body_color = "#5A5A5A"  # medium gray

instructions = "Instructions:"
instruction_label_header = Label(root, text=instructions, padx=20, pady=10, font=header_font, fg=header_color)
instruction_label_header.grid(row=0, column=0, sticky=tk.W)

instructions_body = (
    "1. Click on 'Convert JSON to CSV'.\n"
    "2. Select BOTH the 'Following' and 'Followers' JSON files.\n"
    "3. Choose where you'd like to save the combined CSV file.\n"
    "4. The CSV file will be generated with the combined data."
)
instruction_label_body = Label(root, text=instructions_body, padx=20, pady=10, font=body_font, fg=body_color, justify=tk.LEFT)
instruction_label_body.grid(row=1, column=0, sticky=tk.W)

# Assuming save_icon.png is in the current directory
save_icon = PhotoImage(file="ico/save_icon.png")
Button(root, text="Convert JSON to CSV", image=save_icon, compound=tk.LEFT, command=convert).grid(row=2, column=0, pady=20)

saved_file_label = Label(root, text="")
saved_file_label.grid(row=3, column=0, pady=10)

root.mainloop()