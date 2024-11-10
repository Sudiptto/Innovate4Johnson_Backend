from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import os
from dotenv import load_dotenv



def getListing(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")

    driver = uc.Chrome(options=chrome_options, service=Service(uc))
    driver.get(link)
    
    job_detail_elements = driver.find_elements(By.ID, "js-job-detail")
    
    job_text = ""
    for element in job_detail_elements:
        job_text += element.text + "\n"
    
    return job_text

print(getListing("https://jobs.jnj.com/en/jobs/2406199309w/technology-intern-2025-summer-jjt-intern/"))
    



