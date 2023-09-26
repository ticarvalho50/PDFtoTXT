import re
import pandas as pd

txt_path = r'path do txt'

#in this pdf i wanted to grab some infos from each of the messages that the pdf had

#create a list for saving the info

transactions = []

#open the txt
with open(txt_path, 'r', encoding= 'utf-8') as txt_file:
    #read the txt and remove the page counter
    text = re.sub(r'Page \d+ of \d+', ''. txt_file.read())

#Then I divided the transactions in blocs, each block started with Message Type

blocos = re.split(r'Message Type', text)[1:]

#Now we want to define the patterns for our regex.
#for defining the patterns there are multiple ways, gonna put down 3 patterns that i used

pattern_decision = r'Decision\n(.*?)\n' #Here I grab what was the Decision
pattern_acquisition_date = r'Acquisition date (\d+ \w+ \d{4})' #here i grab the date of the acquisition
pattern_reference = r"Reference (.+)"

#Starting creating variables for storing the infos

current_message_type = None
current_transaction = {}

capturing = False
Index = 0

#iterate per block
for bloco in blocos:

    #creating columns for sotring the the DT
    match_decision = re.search(pattern_decision, bloco)
    if match_decision:
        current_transaction["Decision"] = match_decision.group(1)

    match_acquisition_date = re.search(pattern_acquisition_date, bloco)
    if match_acquisition_date:
        current_transaction["Acquisition Date"] = match_acquisition_date.group(1)

    match_reference = re.search(pattern_reference, bloco)
    if match_reference:
        current_transaction["Reference"] = match_reference.group(1)

#Now we want to send the info to a DT
#Then we export the DT to an Excel

excel_path = r'Excelpath.xlsx'
df= pd.DataFrame(transactions)

print(df)


df.to_excel(excel_path, index = False)

print(f'O arquivo foi salvo em {excel_path}.')


