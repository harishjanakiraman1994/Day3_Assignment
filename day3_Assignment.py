import pyautogui
import time
import webbrowser

# Step 1: Open the web browser and navigate to the desired website
website_url = "https://www.bbc.com" 
webbrowser.open(website_url)

# Step 2: Wait for the website to load
time.sleep(5)  # Adjust the sleep time as needed based on your internet speed   

# Step 3: Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()

#step 4: Save the screenshot to a file
screenshot.save("screenshot.png")  # Save the screenshot as "screenshot.png" in the current directory

print("Screenshot saved as 'screenshot.png' in the current directory.")
