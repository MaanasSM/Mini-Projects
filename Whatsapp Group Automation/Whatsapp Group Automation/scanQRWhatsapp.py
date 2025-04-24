from selenium import webdriver
import pickle
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
driver.get("https://web.whatsapp.com")

# Wait for user to scan QR code manually
input("Scan the QR code on WhatsApp Web and press Enter to continue...\n\n")

# Save session cookies after login
cookies = driver.get_cookies()
pickle.dump(cookies, open("whatsapp_cookies.pkl", "wb"))

print("Login successful! Session saved.")
driver.quit()
