import pandas as pd


df = pd.read_csv("C:/Users/gpanc/OneDrive/Documents/python-challenge/PyPoll/Resources/election_data.csv")
candidate_names = list(df["Candidate"].unique())
candidates = (df["Candidate"])
percent1 = 0
greatest_count_votes = 0
winner = 0
total = len(df)

print()
print("Election Results")
print()
print("--------------------------------")
print()
print("Total Votes:", len(df))
print()
print("--------------------------------")
print()


txt_file = open("C:/Users/gpanc/OneDrive/Documents/python-challenge/PyPoll/analysis/results_file.txt", "w")
txt_file.write("Election Results\n")
line1 = ("---------------------------------------\n")
txt_file.write(line1)
total_votes = "Total Votes: " +str(len(df))+ "\n"
txt_file.write(total_votes)
line2 = ("---------------------------------------\n")
txt_file.write(line2)




for name in candidate_names:
    count_names = 0
    for candidate in candidates:
        if name == candidate:
            count_names +=1 
    if(greatest_count_votes < count_names):
        greatest_count_votes = count_names
        winner = name    
    print(name, "{:.3%}".format(count_names/len(df)), count_names)


    candidate_lists = name + " " +"{:.3%}".format(count_names/len(df))+ " "+ str(count_names)+ "\n"
    txt_file.write(candidate_lists)
line3 = ("---------------------------------------\n")
txt_file.write(line3)
txt_file.write("Winner: " + winner+ "\n")
line4 = ("---------------------------------------\n")
txt_file.write(line4)

txt_file.close()




print()
print("--------------------------------")
print()
print("Winner:", winner)
print()
print("---------------------------------")




