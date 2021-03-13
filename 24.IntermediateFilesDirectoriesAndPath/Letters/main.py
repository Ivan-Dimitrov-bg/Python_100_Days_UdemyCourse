#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
new_letters = []
with open("Input/Names/invited_names.txt", mode='r') as fileNames:
    names = fileNames.readlines()

with open("Input/Letters/starting_letter.txt", mode='r') as fileLatter:
    t_letter = fileLatter.read()
    for name in names:
        striped_name = name.strip()
        new_test = t_letter.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_{striped_name}_.txt", mode="w") as new_file:
            new_file.write(new_test)



