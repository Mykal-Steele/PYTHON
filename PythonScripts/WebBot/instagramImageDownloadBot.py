from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
import pickle
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Basic setup
SAVE_DIR = os.path.join(os.getcwd(), "instagram_images")
os.makedirs(SAVE_DIR, exist_ok=True)
COOKIES_FILE = os.path.join(os.getcwd(), "instagram_cookies.pkl")
print(f"Saving images to: {SAVE_DIR}")

# Get Instagram login info from environment variables
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

# Check if environment variables are loaded correctly
if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD or not CHROMEDRIVER_PATH:
    print("❌ Missing necessary environment variables. Make sure .env is correctly configured.")
    exit()

# Start browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)

try:
    # Check if cookies file exists
    if os.path.exists(COOKIES_FILE):
        print("Loading cookies from file...")
        driver.get("https://www.instagram.com/")
        with open(COOKIES_FILE, "rb") as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        print("Cookies loaded. Logged in session restored.")
        time.sleep(5)
    else:
        # Login to Instagram
        print("Attempting to login to Instagram...")
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys(INSTAGRAM_USERNAME)  # Use env variable
        driver.find_element(By.NAME, "password").send_keys(INSTAGRAM_PASSWORD + Keys.RETURN)  # Use env variable
        print("Login credentials entered, waiting for page load...")    
        time.sleep(10)  # Wait for login

        # Save cookies to file
        print("Saving cookies for future use...")
        with open(COOKIES_FILE, "wb") as f:
            pickle.dump(driver.get_cookies(), f)

    # Go to target page
    print("Navigating to target Instagram page...")
    driver.get("https://www.instagram.com/ofc.zalika/")
    time.sleep(5)

    # Track downloads
    downloaded_urls = set()
    image_count = 1
    end_flag = False

    # Main download loop
    while True:
        # Find images
        images = driver.find_elements(By.CSS_SELECTOR, 'img[src]')

        print(f"\nFound {len(images)} total images on current page")
        new_downloads = 0

        # Download new images
        for img in images:
            img_url = img.get_attribute("src")
            if img_url and img_url not in downloaded_urls:
                try:
                    print(f"Downloading image {image_count}... ", end='', flush=True)
                    response = requests.get(img_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                    if response.status_code == 200:
                        filename = os.path.join(SAVE_DIR, f"image_{image_count}.jpg")
                        with open(filename, 'wb') as f:
                            f.write(response.content)
                        downloaded_urls.add(img_url)
                        print(f"SUCCESS - Saved as image_{image_count}.jpg")
                        image_count += 1
                        new_downloads += 1
                    else:
                        print(f"FAILED - Status code: {response.status_code}")
                except Exception as e:
                    print(f"FAILED - Error: {e}")

        print(f"\nDownloaded {new_downloads} new images in this batch")
        print(f"Total images downloaded so far: {len(downloaded_urls)}")

        # Check if we should continue scrolling
        if new_downloads == 0:
            print("\nNo new images found, checking if page end reached...")
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Scrolled to bottom, waiting for content load...")
            time.sleep(3)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                if end_flag:
                    print("\n🏁 Reached end of page - No new content after double check")
                    break
                print("Page height unchanged, waiting to confirm...")
                time.sleep(2)
                end_flag = True
            else:
                end_flag = False
                print("New content loaded, continuing...")

        time.sleep(2)

    print(f"\n✅ Download complete! Total images downloaded: {len(downloaded_urls)}")

except Exception as e:
    print(f"\n❌ An error occurred: {e}")

finally:
    print("\nClosing browser...")
    driver.quit()
