import argparse
import time
import webbrowser
import random

logo = """______    _                _          
| ___ \  | |              | |         
| |_/ /___| | ___  __ _ __| | ___ _ __ 
|   // _ \ |/ _ \ / _` |/ _` |/ _ \ '__|
| |\ \ __/ | (_) | (_| | (_| | __/ |  
\_| \_\___|_|\___/ \__,_|\__,_|\___|_|
                     FB/Sharif Ansari
"""

print(logo)

# Function to open the link in Firefox
def open_link(link):
   webbrowser.get('firefox').open(link)

# Main function to run the reloader
def run_reloader(link, min_interval, max_interval):
   try:
       while True:
           interval = random.randint(min_interval, max_interval) * 60  # Convert minutes to seconds
           time.sleep(interval)
           open_link(link)
           print(f"Profile Opened Successfully in {interval/60} Minutes ✔")
   except KeyboardInterrupt:
       print("\nExit...")

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Reloader tool with required username parameter.")
   parser.add_argument("-u", "--username", type=str, help="Username to replace in the link.", required=True)
   args = parser.parse_args()

   # Replace the link with your desired link
   username = args.username
   link = f"https://www.fiverr.com/users/{username}/seller_dashboard"
   min_interval = 5  # Minimum interval in minutes
   max_interval = 10  # Maximum interval in minutes

   # Call the main function to start the reloader
   run_reloader(link, min_interval, max_interval)
