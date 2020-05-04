1st commit- Admin can create users and create entities on user behalf------

Admin can create user, and can create entities on user behalf. A entity table is made with foreign key i.e.,user.id. A One-to-many 
relationship is created from User to Entity.


2nd commit- New user can register through api

New users can register through api using url http://127.0.0.1:8000/register/ and new object of user will be created in user model, on 
every new registration, we check if username and e-mail is unique or not. As username and e-mail should be unique for each user.
We can see the list of all users using url http://127.0.0.1:8000/allusers/. 


3rd commit- Entity api is created and user can view,create,update and delete their entities

New user can register successfully now. Authorized user can create entities. Owner of the entity can see theirs entities,update or delete
entities. User can login and logout in their accounts.

urls working-

http://127.0.0.1:8000/api/ = Home page
http://127.0.0.1:8000/api/register = To register new user
http://127.0.0.1:8000/api/allusers = To show all users
http://127.0.0.1:8000/api/api-auth/login = To login the account of users
http://127.0.0.1:8000/api/list-entities/ = To show all entities of a user
http://127.0.0.1:8000/api/entity/id/ = To get the specific entity of a user, so that user can view,update or delete this entity




