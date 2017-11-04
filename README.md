# website-blocker
This is the python program which does'nt allow websites to load which are distracting while working hours
This file will run automatically when you start your pc/laptop 

# Changes you can make in program as per your convenience
i have kept start_time = 8 and end_time = 16 in the program in order to block the websites if the time is in between 8 and 16
you can change the start_time and end_time variables in the program if you want to

And you can add websites that you want to block in the website_list variable

# For the program to auto run
To make your program run automatically do the following

For Mac and Linux users:
  You have to add this program in crontab file, you can do that by following command
  $sudo crontab -e
  
  after executing the above cammand, add the following line of code
  python3 ~/websiteblocker.py
  in the above line you have to specify the full path of the python program
 
For Windows users:
  You have to create a task in task Sceduler
  Steps:
  1. open task sceduler
  2. create task
  3. give any name to the task and check run with high previligies
  4. go to the trigger tab above and set begin the program as At startup
  5. in action tab select program as your websiteblocker.pyw file
  6. and in conditions tab uncheck the checkpoint which says start task only when on AC power
  7. press ok


# Credits
I learnt this from the python course of Ardit Sulce from udemy
