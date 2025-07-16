   #  Explanation

#      🔧 What is Scripting?
# Scripting refers to writing small programs (scripts) that automate simple tasks. These scripts often:

# Run directly (without compiling)

# Are used for automation, file handling, system operations, etc.

# Are often written in languages like Python, Bash, PowerShell

# 🤖 What is Automation?
# Automation is the process of using software to perform repetitive tasks without human intervention. Examples include:

# Renaming multiple files

# Sending automated emails

# Scraping websites for data

# Moving files based on rules

# Scheduled backups 

# import os

# # Folder containing text files
# folder_path = "C:/Users/YourName/Desktop/files"

# # Rename all .txt files in the folder
# for count, filename in enumerate(os.listdir(folder_path)):
#     if filename.endswith(".txt"):
#         old_file = os.path.join(folder_path, filename)
#         new_file = os.path.join(folder_path, f"document_{count+1}.txt")
#         os.rename(old_file, new_file)

# print("Files renamed successfully!")

# import datetime

# print("Todays date is", datetime.date.today())

# import requests
#
# url = 'https://fb.com'
# response = requests.get(url)
#
# if response.status_code == 200:
#     with open('downloaded_page.html', 'w', encoding='utf-8') as file:
#         file.write(response.text)
#     print("Web page downloaded and saved as 'downloaded_page.html'")
# else:
#     print(f"Failed to download page. Status code: {response.status_code}")

# import datetime

# # Define a special date (e.g., someone's birthday)
# birthday = datetime.date(2025, 6, 19)
# today = datetime.date.today()

# if today == birthday:
#     print("🎉 Today is the birthday! Send your wishes!")
# else:
#     days_left = (birthday - today).days
#     print(f"{days_left} days left until the birthday.")


