# Project-CIS1051-Pinkow
--Video demonstrating the project details below:

https://www.loom.com/share/d2ee019b4bfb4adeb5b5cbcdd13d7e50?sid=53776b11-2833-4483-b005-b6790f4004fb

*If you cannot access the video, please immediately email me @tup16404@temple.edu

--PowerPoint Presentation Detailing the content below:

https://tuprd-my.sharepoint.com/:p:/g/personal/tup16404_temple_edu/EUUxSFfXuGVPpib4ZryoSD0BuN_jhdVcEjBM7QfdcD433g

Others:



Motives:


1. The motive behind this project includes people like my parents, friends, etc. Many of us desire to achieve nutrition goals (others may not, which is okay). 

   --With this, come some drawbacks, which include costs (inflation can dissuade), restrictions, having consistency, or simply a lack of knowledge. The goal of my program is to reduce this.




Successful Challenges:

1. Being able to successfully overcome the ValueError on the program
   
2. To reduce redundancy, calling upon other functions (like fourEveryone()). It saved many lines of code
   
3. Being able to account for allergies/restrictions without printing out a statement that
   calls for an ingredient that they are allergic to. Same goes with restrictions(vegan) and not printing anything like "You should buy milk". There might be a "if keto, you should consider" but nothing that urges themm to buy something the user is allergic to.
  
4. Successfully being able to account for various answers, such as lowercase, etc. Some of the restrictions had similar first couple of letters (like vegetarian and vegan), which I was 
able to adapt the code so that a vegan's input is not given a vegetarian input, etc.



5. Successfully able to automate sending email messages. This took some lines of code,
ended up performing my main task (what takes this even further). I effectively learned how emails from my gmail (and possibly gmails in general) are sent


6. Successfully able to hide a password. This took me some time. If you look at GmailReminder.Survey.py, you might've noticed I imported a file called cred. This is another private file that I have on PyCharm. The reason I imported this is because it contains some confidential information. By having it stored in a secure spot, I learned that I can run code (while hiding the password) so it cannot be taken. An essential component of cybersecurity

   




Unsuccessful Challenges:

1. If one has multiple allergies/dietary restrictions, the algorithm does not   account for it
    --Slicing can’t account for factors like these. There were instances where I attempted to 
       use the in and not in operators for these two variables, but they were ineffective, leading me to stick to slicing. 

2. Attempting to remove certain punctuation from the printing statements
--In the print statements, the lists would end up printing “ ( ‘ ”, “ [( “,” [ ‘ ”, etc.
    I attempted to use the REGEX module to either remove these redundancies or replace them with a comma from the print statements, but I came up slightly short.





Conclusion:

1. Even though my program had a few shortfalls, I believe this project greatly improved my understanding of interactions/modules when dealing with automating tasks, matching, etc. with many Python functions.
         --Lists, for-if-while conditionals, usage of functions to simplify code
     --Random, Time, Schedule, Regex, etc.


2. Additionally, I think that this program can help people make conscious decisions about their spending habits with groceries and maintain consistency to ensure that they’re on their way to achieving their desired goals without being exclusive of their preferences/allergies. We’re all in this together.




