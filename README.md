# rssFeeder
This was a simple fun project to get information on the new manga released. :)

Requirements:
Need to install FLASK, flask_sqlalchemy.

How to Run :-
Just setup ur DB, as mentioned in DB.png.
Setup the DB in rss_app.py, line number 
set ur username and password

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://<UserName>:<Password>@localhost/RSS_python"

i have setup a bassh script to run the server as well.

Where to check if its running:-

For my set up its running on port number 5876 on localhost.

"http://localhost:5876"

if you want to change the port, just change it in line number 95

app.run(debug=True, port=5876)

I have set up the debug to true, because i wanted to check the changes on website ASAP.

Hope you'll enjoy it,

Comments, review, questions and suggestion are always welcome on 
shashank17nov@gmail.com


And at last, as always thanks to all the stack overflow sources for the help.
