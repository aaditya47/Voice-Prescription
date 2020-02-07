import speech_recognition as sr
from selenium import webdriver
import csv
import pandas as pd
import pdfkit as pdf

config = pdf.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

r = sr.Recognizer()

def inp_audio():
        while(True):
                with sr.Microphone() as source:
                        print("Say Something!")
                        audio = r.record(source, duration = 6)
        
                        try:
                                stdin = r.recognize_google(audio)
                        except:
                                print('Sorry! Can you try again?')
                        
                        else:
                                break
        return stdin
        
print("Enter the name,age and gender of the patient:")
inf = inp_audio()
info=inf.split(', ')
if(info[2]=='mail'):
    info[2]='male'
#print(inf)
print(info)
print("Enter the symptoms:")
symptoms = inp_audio()
print(symptoms)
print("Enter the diagnosis:")
diagnosis = inp_audio()
print(diagnosis)
print("Enter the Prescription:")
prescription = inp_audio()
print(prescription)
print("Enter general advice:")
advice = inp_audio()
print(advice)

driver=webdriver.Chrome()
# open url
driver.get('D:/SIH/index.html')
# Click on describe
describe_button=driver.find_element_by_xpath('/html/body/button')
describe_button.click()
# Enter name
name_field=driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/centre/input[1]')
name_field.send_keys(info[0])
# Enter age
age_field=driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/centre/input[2]')
age_field.send_keys(info[1])
# Enter gender
gender_field=driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/centre/input[3]')
gender_field.send_keys(info[2])
# Enter symptoms
symptoms_field=driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/centre/input[4]')
symptoms_field.send_keys(symptoms)
# Enter diagnosis by doctor
diagnosis_field=driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/centre/input[5]')
diagnosis_field.send_keys(diagnosis)
# Enter prescription
prescription_field=driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/centre/input[6]')
prescription_field.send_keys(prescription)
# Enter advice
advice_field=driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/centre/input[7]')
advice_field.send_keys(advice)

# Flask integration here

with open('data.csv',mode='w') as database:
        fieldnames = ['name', 'age', 'gender', 'symptoms', 'diagnosis', 'prescription', 'advice'] 
        writer = csv.DictWriter(database, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
                        'name':info[0],
                        'age':info[1],
                        'gender':info[2],
                        'symptoms':symptoms,
                        'diagnosis':diagnosis,
                        'prescription':prescription,
                        'advice':advice})

# Convert CSV to PDF
csv_file='D:\SIH\data.csv'
html_file=csv_file[:-3]+'html'
pdf_file=csv_file[:-3]+'pdf'

df = pd.read_csv(csv_file, sep=',')
df.to_html(html_file)
# pdf.from_file(html_file, pdf_file)
pdf.from_file(html_file,pdf_file,configuration=config)
