from selenium import webdriver
import random
import os
import time

chrome_diver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chromedriver")  # Path to the chromedriver ()
number = int(input("Enter the number of times you want to submit the form: "))
web = input("Enter the link to the form: ")
driver = webdriver.Chrome(executable_path=chrome_diver_path)
for i in range(number):  # Number of times you want to submit the form
    driver.get(web)  # Link to the form
    all_questions = driver.find_elements_by_class_name("Qr7Oae")  # Find all the questions
    time.sleep(2)
    for question in all_questions:  # Loop through all the questions
        choice = question.find_elements_by_class_name("nWQGrd")  # Find all the options
        time.sleep(0.75)
        random.choice(choice).click()
    submit = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")  # Find the submit button (Might not work, Trying to find the xpath of the submit button by yourself)
    submit.click()
