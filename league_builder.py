import csv,sys,datetime

num_of_teams = 3

# assign 3 teams Raptors,Sharks,Dragons
Raptors = [] # team1
Sharks = []  # team2
Dragons = [] # team3

exp_and_non_exp_players_count = 0 # hold on to the count for exp and non exp players
experienced_players=[]# will hold all exp players
non_experienced_players=[]# will hold all non exp players
exp_players_per_team = 0 # num exp players each team should have
non_exp_players_per_team = 0 # num of non exp players each team should have

def sort_player_with_team(mydict,mylist):
  """adds each dic to the relevant  list i.e team"""
  mylist.append(mydict)
  
def create_team_sheet(mylist2,team):
  """takes a list and string as an argument. Loops around the list 
  and prints out each dict prefixed with the team"""
  with open("text.csv",'a')as csvfile:
    csvfile.write(""+"\n")
    csvfile.write(team+"\n")
    for mydict in mylist2:
      csvfile.write("{Name}, {Soccer Experience},{Guardian Name(s)}".format(**mydict)+"\n")
      
def letter_to_guardians(mydict3,team):
  """takes a dict and a team name. Then creates a individual letter to his or her guardian
  first_name_and_surname = mydict3['Name'].split(" ")
  above, the string is split into a list of  name and surname
  using the contents of the list to create the firstname and surname file name"""
  
  with open("{}_{}.txt".format(first_name_and_surname[0].lower(),
                               first_name_and_surname[1].lower()),
                                'a')as csvfile:
    csvfile.write("Dear {},".format(mydict3['Guardian Name(s)'])+"\n")
    csvfile.write("{}, {}, {}".format(mydict3['Name'],team,
                                      datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")))
    
def assign_players_to_teams(players,teams,team_names,players_per_team):
  """looping through exp and non exp players and assigning them to teams
    players = list of dictionaries where each is a player ; 
    teams= list of the teams i.e [Raptors,Sharks]; 
    team_names = list of string representation of the teams i.e ["Raptors" "Sharks"] etc
    players_per_team= No of exp or non exp players in a team"""
  
  for exp_and_non_exp_players_count in range(len(players)):
    if exp_and_non_exp_players_count < players_per_team:# first batch of players. 
      sort_player_with_team(players[exp_and_non_exp_players_count],teams[0])# adds players to teams
      letter_to_guardians(players[exp_and_non_exp_players_count],team_names[0])# create a letter for each player    
    elif exp_and_non_exp_players_count < (players_per_team * 2):# next batch of players
      sort_player_with_team(players[exp_and_non_exp_players_count],teams[1])# adds players to r=teams
      letter_to_guardians(players[exp_and_non_exp_players_count],team_names[1])  # create a letter for each player        
    else: # rest of the exp and non exp players
      sort_player_with_team(players[exp_and_non_exp_players_count],teams[2])# adds players to teams
      letter_to_guardians(players[exp_and_non_exp_players_count],team_names[2]) # create a letter for each player     
    exp_and_non_exp_players_count+=1 #  incrementing the count. This helps to works out how many players to add to each list

         

      
      
if __name__=="__main__":
  #read the file in and sort experienced from non experienced players
  with open(sys.argv[1],newline='')as csvfile:
    reader =csv.DictReader(csvfile,delimiter=",")
    for row in reader:
      if row['Soccer Experience']=="YES":
        experienced_players.append(row)# getting all exp players
      else:
        non_experienced_players.append(row)# getting all non exp players
        
  # calculating the no of exp players for eachteam. list of exp players / no of teams
  exp_players_per_team = len(experienced_players)/num_of_teams
  # calculating the no of non exp players for eachteam. list of non exp players / no of teams
  non_exp_players_per_team = len(non_experienced_players)/num_of_teams

  assign_players_to_teams(experienced_players,[Raptors,Dragons,Sharks],["Raptors","Dragons","Sharks"],exp_players_per_team)
  assign_players_to_teams(non_experienced_players,[Raptors,Dragons,Sharks],["Raptors","Dragons","Sharks"],non_exp_players_per_team)
      
  create_team_sheet(Raptors,"Raptors")   
  create_team_sheet(Dragons,"Dragons") 
  create_team_sheet(Sharks,"Sharks") 


      

    
    
    
    
    
    

      

