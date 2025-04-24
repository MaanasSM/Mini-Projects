from selenium import webdriver
import pickle
import time

# Open WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# Wait for the page to fully load before adding cookies
time.sleep(10)  # Give WhatsApp time to load

# Load saved session cookies
cookies = pickle.load(open("whatsapp_cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh page to apply cookies
# driver.get("https://web.whatsapp.com")  # Instead of refresh()
driver.refresh()
time.sleep(5)  # Allow time to verify login

print("Logged in successfully!")