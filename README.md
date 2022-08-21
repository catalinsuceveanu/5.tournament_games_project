# Tournament games generator

During tournaments the organizers have to mix and match teams in plays which are going to entertain the public.
There are a few important rules in doing so. Never match teams that are close in score from the beginning of the tournament (you want the closest and most spectacular at the end)

This rule and a few others have been implemented in this tournament games generator.
You can see an execution of this program below:

```python
Enter the number of teams in the tournament: 6
Enter the name for team #1: AA
Enter the name for team #2: BB
Enter the name for team #3: CC
Enter the name for team #4: DD
Enter the name for team #5: EE
Enter the name for team #6: FF
Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 6
Enter the number of wins Team AA had: 1 
Enter the number of wins Team BB had: 4 
Enter the number of wins Team CC had: 3 
Enter the number of wins Team DD had: 4 
Enter the number of wins Team EE had: 2 
Enter the number of wins Team FF had: 7 
The maximum number of wins is 6, try again.
Enter the number of wins Team FF had: 5 
Generating the games to be played in the first round of the tournament...
Home: AA VS Away: FF
Home: EE VS Away: BB
Home: CC VS Away: DD
```
