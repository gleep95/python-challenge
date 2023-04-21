import pandas as pd

#Open and read election poll data
#Works Cited: https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/
df = pd.read_csv("C:/Users/gpanc/OneDrive/Documents/python-challenge/PyPoll/Resources/election_data.csv")

#Create a list of the unique names of the candidates, then the whole list of candidates
#Works Cited: https://stackoverflow.com/questions/71098589/pandas-return-column-data-as-list-without-duplicates
candidate_names = list(df["Candidate"].unique())
candidates = (df["Candidate"])

#Set variables/counters
percent1 = 0
greatest_count_votes = 0
winner = 0

#Get the total votes
total = len(df)

#Print the Election Results statement and total votes
print()
print("Election Results")
print()
print("--------------------------------")
print()
print("Total Votes:", len(df))
print()
print("--------------------------------")
print()

#Write the Election Results statement and total votes to a results text file
#Works Cited: https://blog.finxter.com/how-to-print-a-percentage-value-in-python/
txt_file = open("C:/Users/gpanc/OneDrive/Documents/python-challenge/PyPoll/analysis/results_file.txt", "w")
txt_file.write("Election Results\n")
line1 = ("---------------------------------------\n")
txt_file.write(line1)
total_votes = "Total Votes: " +str(len(df))+ "\n"
txt_file.write(total_votes)
line2 = ("---------------------------------------\n")
txt_file.write(line2)



#Loop through names of unique list and set a counter
for name in candidate_names:
    count_names = 0
    
    #Loop through whole candidates list looking for the unique names and counting them
    for candidate in candidates:
        if name == candidate:
            count_names +=1 
    
    #Find the names that has the greatest amount of votes
    if(greatest_count_votes < count_names):
        greatest_count_votes = count_names
        winner = name    
    
    #Print the results of the candidate name, percentage of votes and total votes
    print(name, "{:.3%}".format(count_names/len(df)), count_names)

    #Write the results of the candidate name, percentage of votes and total votes to results text file
    #As well as writing the winner
    #Works Cited: #Works Cited: https://blog.finxter.com/how-to-print-a-percentage-value-in-python/
    candidate_lists = name + " " +"{:.3%}".format(count_names/len(df))+ " "+ str(count_names)+ "\n"
    txt_file.write(candidate_lists)
line3 = ("---------------------------------------\n")
txt_file.write(line3)
txt_file.write("Winner: " + winner+ "\n")
line4 = ("---------------------------------------\n")
txt_file.write(line4)
txt_file.close()

#Print out the winner results
print()
print("--------------------------------")
print()
print("Winner:", winner)
print()
print("---------------------------------")




