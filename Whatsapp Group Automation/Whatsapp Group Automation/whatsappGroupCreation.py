from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import pickle

# Load phone numbers from Excel
file_path = "participants.xlsx"  # Your Excel file
df = pd.read_excel(file_path)
phone_numbers = df.iloc[:, 0].astype(str).tolist()  # Convert to string list

# Open WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# Wait for manual login
input("Scan the QR code and press Enter to continue...")

# Save cookies after login
pickle.dump(driver.get_cookies(), open("whatsapp_cookies.pkl", "wb"))
print("Cookies saved!")

# Click on "New Chat" (assuming the sidebar is open)
# new_chat_xpath = '//div[@title="New chat"]'  # Adjust if needed
print("\n\nAbout to click the button NEW CHAT\n\n")
new_chat_xpath = '//button[@aria-label="New chat"]'
# new_chat_button = driver.find_element(By.XPATH, new_chat_xpath)
new_chat_button = driver.find_element(By.XPATH, new_chat_xpath)
new_chat_button.click()
time.sleep(2)
print("\n\nNEW CHAT Button Clicked !!!!\n\n")


# Click on "New Group"
print("\n\nAbout to click the button NEW GROUP\n\n")
new_group_xpath = '//div[contains(text(),"New group")]'
new_group_button = driver.find_element(By.XPATH, new_group_xpath)
new_group_button.click()
time.sleep(2)
print("\n\nNEW GROUP Button Clicked !!!!\n\n")


# Add Participants
search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search name or number"]')

for number in phone_numbers:
    #search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search name or number"]')
    print("\n\nNumber ",number,"Entered\n")
    search_box.send_keys(number)
    time.sleep(2)  # Allow search results to load
    print("Number", number, "searching........")
    search_box.send_keys(Keys.ENTER)  # Select contact
    print("Contact SELECTED\n\n")
    time.sleep(1)

print("\n\nALL CONTACTS SELECTED\n\n")

search_box.send_keys(Keys.ENTER)
time.sleep(2)

# print("\n\nLET US INPUT THE GROUP NAME\n\n")

print("\n\nFAMILY GROUP CREATEDDDDD\n\n")
print("\n\n################################## STEP1 done ##############################################\n\n")



# Enter Group Name
# Locate the Group Subject input field
group_subject_xpath = '//div[@contenteditable="true" and @aria-label="Group subject (optional)"]'
group_subject = driver.find_element(By.XPATH, group_subject_xpath)
print("\n\nLET US INPUT THE GROUP NAME\n\n")
# Enter group name
group_subject.send_keys("My New Group")
time.sleep(2)

print("\n\nTHE GROUP NAME ENTERED\n\n")

group_subject.send_keys(Keys.ENTER)

print("\n\nFAMILY GROUP CREATEDDDDD\n\n")

input("press Enter to continue...")

driver.refresh()  # Refresh the page to update chat list
time.sleep(3)

input("Press enter to continue...")

print("WhatsApp Group Created Successfully! 🎉")

driver.quit()  # Close browser