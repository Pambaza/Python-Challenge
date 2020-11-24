import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
print(csvpath)

votes = []
candidates =[]

with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    print(csv_header)

#     for column in csvreader: 
#         votes.append(column[0])
#         candidates.append(column[2])

#     total_votes =(len(votes))
#     print(f"Total Votes: {total_votes}")    
    
  
# #   * A complete list of candidates who received votes

candidates.sort()
# Setting uniques candidates in 'uniqueCandidates' list
uniqueCandidates = set(candidates)
print(uniqueCandidates)


# khan_total = 0
# correy_total = 0
# li = 0
# otooley_total = 0

with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    

    for row in csvreader: 
                          
        if row[2] =="khan":
            khan_total +=1
            
        elif row[2] =="correy":
            correy_total +=1   

        elif row[2] =="li":
            li_total +=1 

        elif row[2] =="O'Tooley":
            otoole_total +=1  


#percentage calculation of votes
khan_pc = (khan_total/total_votes)*100
print(khan_pc)
correy_pc =(correy_total/total_votes)*100
print(correy_pc)
li_pc =(li_total/total_votes)*100
print(li_pc)
otoole_pc =(otooley_total/total_votes)*100
print(otooley_pc)

#summary table 
with open(csvpath_out, 'w', newline= '') as txtfile:

    txtfile.write('Election Results\n')
    txtfile.write('----------------------------\n')

    txtfile.write((f"Total Votes: {total_votes}" '\n')    
    txtfile.write('----------------------------\n')

   

           
    



# #   * A complete list of candidates who received votes

# #   * The percentage of votes each candidate won

# #   * The total number of votes each candidate won

# #   * The winner of the election based on popular vote.

# # * As an example, your analysis should look similar to the one below:
