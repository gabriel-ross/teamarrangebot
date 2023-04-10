from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.instagram.com/")
    # "class name"
    # By.ClassName
    browser.find_element(by=By.CLASS_NAME, value="_ab37").click()
    while(True):
        pass

if __name__ == "__main__":
    main()