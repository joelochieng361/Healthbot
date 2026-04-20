import pandas as pd

#Load your data into the frame
df = pd.read_csv("health_data.csv")
# print(df)

print("Healthbot: Hello there, I am your Health assistant bot, How may I help you")

while True:
    #Get the user input ans store the same into a variable
    user_text = input("\n You: ").lower()
    
    #Check if the user wants to exit
    if user_text == "quit":
        print("Healthnot: Goodbye! Nice to have been at your service, thank you")
        break
    
    #Create a variable which will store the structure found in the csv file
    found_answer =False
    
    #Come up with a loop that loops through the entire data file
    for index, row in df.iterrows():
        #clean up the keys from the csv row
        keywords_list = str(row['Keywords']).split(',')
        
        # Below we check every keyword in that given row (Keyword)
        
        for word in keywords_list:
            clean_word = word.strip().lower()
            
            #If the keyword is inside of the users sentence
            if clean_word in user_text:
                print("Healthbot: ", row["response"])
                found_answer = True
                break
    
    if found_answer:
        break # stop looking for other answers since we already found a match

# If we went through the entire data file and did not find any match, we can print a default response
if not found_answer:
    print("Healthbot: I'm sorry, I don't have an answer for that. Can you please rephrase or ask something else?")