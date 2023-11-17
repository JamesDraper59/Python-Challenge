#modernize a small town's voting process

#import csv module
import csv

#create lists and variables to store appropriate data
candidates = []
unique_candidate = []
candidates_votes = []
vote_percentage = []
total_votes = 0

#set working directory using a raw string
election_data = r'C:\Users\James\Python-Challenge\PyPoll\Resources\election_data.csv'

#open and read through csv file
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    header = next(reader)

    #loop through each row of the election data file
    for row in reader:
        
        #total the amount of votes
        total_votes = total_votes + 1

        #introduce the name of the candidate to the list
        candidates.append(row[2])

    #place each unique candidate name in the list
    for names in set(candidates):
        unique_candidate.append(names)

        #votes per each unique candidate by the amount of times they appear in the candidates list
        vpc = candidates.count(names)
        
        #store the total number of votes that candidate recieved in the list
        candidates_votes.append(vpc)

        #calculate the percentage of votes each candidate received and limit to two decimal places
        popularity = 100*(vpc/total_votes)
        popularity = round(popularity, 2)
        vote_percentage.append(popularity)


    #determine and store the winner of the election
    popular_candidate = max(candidates_votes)
    winning_candidate = unique_candidate[candidates_votes.index(popular_candidate)]

    #print election results to terminal
    print("Election Results" + "\n")   
    print("-------------------------" + "\n")
    print("Total Votes :" + str(total_votes) + "\n")    
    print("-------------------------" + "\n")
    for candidates in range(len(unique_candidate)):
            print(unique_candidate[candidates] + ": " + str(vote_percentage[candidates]) +"% (" + str([candidates])+ ")" + "\n")
    print("-------------------------" + "\n")
    print("The winner is: " + winning_candidate + "\n")
    print("-------------------------")

    #create and write results into txt document
    with open('election_results.txt', 'w') as text:
        text.write("Election Results" + "\n")
        text.write("---------------------------------------" + "\n")
        text.write("Total Vote: " + str(total_votes) + "\n")
        text.write("---------------------------------------" + "\n")
    for candidates in range(len(set(unique_candidate))):
        text.write(unique_candidate[candidates] + ": " + str(vote_percentage[candidates]) +"% (" + str(candidates_votes[candidates]) + ")\n")
        text.write("---------------------------------------" + "\n")
        text.write("The winner is: " + winning_candidate + " "+ "\n")
        text.write("---------------------------------------" + "\n")