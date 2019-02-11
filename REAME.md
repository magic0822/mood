#Mood App

##Running: 
Login user name: admin  
password: secret

###1. Endpoint "/mood" w/GET method:
Returns the list of moods of the logged in user. (if user is not logged in, will redirect to the 'Log in' page" ).

###2. Endpoint "/mood" w/POST method:
Store the users adding moods.

###3. Endpoint "/login':
User login page, after submitting the form, app will verify the username and password.

##Q&A:
- Q: Document what, if anything, you would do differently if this were a production application and not an assessment? What tech would you use? How would you handle things differently if it needed to handle more users, more data, etc?  
A: In production environment, should use databse to store and modify all the datas. A relation database could handle different users and tables so that connect together.

- Q: Explain the implications of switching the type of data being used for mood values after an initial version is deployed. For example, if the value started as a float or a string, but needed to change to only support integers, how would you handle this change?  
A: I will try to add a rule to front-end and form input to force user input an Integer.

***
1. Create a web REST application with a '/mood' endpoint, which when POSTed to persists the submitted mood value.
2. Add a GET method to the '/mood' endpoint which returns all submitted mood values
3. Add the ability for users to login. The GET method for the '/mood' endpoint should now only return values submitted by the logged-in user.
4. Add to the body of the response for the ‘/mood’ endpoint the length of their current "streak".(A user is on a “streak” if that user has submitted at least 1 mood rating for each consecutive day of that streak.
For example, if on March 1st, March 2nd, March 3rd, and March 5th the user entered mood ratings, a 3-day streak will applied to the March 3rd rating and the streak will reset to a 1-day streak for the March 5th rating.)
5. Calculate the user's streak's percentile compared to other users, and if the percentile is >= 50%, return that percentile (A users’ longest streak is defined as largest number of consecutive days that user has submitted mood ratings. Compare this user’s streak to all other users’ longest streaks to determine the percentile.)
6. Add a new endpoint ‘/mood_streak_correlation’ which returns data explaining the correlation between the users’ moods and the length and consistency of their streaks.
7. Containerize your application (Set up your application for containerization such that it can be run on any machine that supports the containerization technology (e.g., Docker).)
***



