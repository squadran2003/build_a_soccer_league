## The app, reads a csv file of players in a team and divides them equally based on experience

## Example code

```python

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


  ```

# To run the file, execute the script league_builder.py and pass in the filename i.e 
# python league_builder.py soccer_players.csv





