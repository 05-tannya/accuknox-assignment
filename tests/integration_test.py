import time
import requests 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

message_from_backend = ""
message_from_frontend = "" 

def test_backend_api():
    url = "http://localhost:3000/greet"
    response = requests.get(url)
    if response.status_code == 200:
        print("Backend API is up and running!")
        print(f"Message from backend: {response.json().get('message')}")
        message_from_backend = response.json().get('message')
        return True
    else:
        print(f"Backend API test failed with status code {response.status_code}")
        
        return False
    
def test_frontend():
    cService = webdriver.ChromeService(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service = cService)
      
    # Open the frontend application
    driver.get("http://localhost:80")


    # Get data from frontend 
    try:
        message_from_frontend = driver.find_element(By.TAG_NAME, "h1").text 
        print("Message from frontend: ",message_from_frontend)
        
    except Exception as e:
        print(f"Frontend interaction failed: {e}")
        return False
    finally:
        driver.quit()

def verification_success():

    test_backend_api() 
    test_frontend()
    verify_messages(message_from_backend,message_from_frontend)
    

def verification_failed():
    test_backend_api() 
    test_frontend()
    verify_messages(message_from_backend,'test')
    
def verify_messages(a,b):

    is_text_correct = a == b
    assert is_text_correct, f"Expected text '{b}', but got '{a}'"
    if is_text_correct:
        print("Test verified: messages are matching")

if __name__ == "__main__":
    verification_success()
    #verification_failed()
