1st commit- Admin can create users and create entities on user behalf------

Admin can create user, and can create entities on user behalf. A entity table is made with foreign key i.e.,user.id. A One-to-many 
relationship is created from User to Entity.


2nd commit- New user can register through api

New users can register through api using url http://127.0.0.1:8000/register/ and new object of user will be created in user model, on 
every new registration, we check if username and e-mail is unique or not. As username and e-mail should be unique for each user.
We can see the list of all users using url http://127.0.0.1:8000/allusers/. 

