# StarNavi test task  

To start project type:
```sh
python manage.py runserver
```

## Main endpoints:  
**/admin/** - django administration  
**/posts/** - post-list and post-creation  
**/posts/<int:pk>/like/** - Like post  
**/posts/<int:pk>/unlike/** - Unlike post  
**/posts/<int:pk>/fans/** - List of users who liked post  
**/analitics/?date_from=YYYY-MM-DD&date_to=YYYY-MM-DD/** - Get the statistics on number of likes grouped by day. The first date is inclusive, but the second date is exclusive  
**/users/** - List of users  
**/users/<int:pk>/** - user view  
**/users/<int:pk>/posts/** - list of posts created by user  
**/users/<int:pk>/activity/** - view of user activity (last_login+last_activity)  
**/register/** - user registration  
**/token/** - JWT token acquiring  
**/token/refresh/** - JWT token refresh  

## Tests:  
There are tests that check user`s registration, post_creation with JWT-token and post-list view.

To run them type:
```sh
python manage.py test
```