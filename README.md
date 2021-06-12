# StarNavi test task

To start project type:
```sh
python manage.py runserver
```

## Main endpoints: 
**/admin/** - django administration  
**/posts/** - post-list and post-creation  
**/posts/<int:pk>/like** - Like post  
**/posts/<int:pk>/unlike** - Unlike post  
**/posts/<int:pk>/fans** - List of users who liked post  
**api/analitics/?date_from=YYYY-MM-DD&date_to=YYYY-MM-DD** - Get the statistics on number of likes grouped by day. The first date is inclusive, but the second date is exclusive  
**/users** - List of users  
**/users/<int:pk>** - user view  
**/register** - user registration  
**/api/token** - JWT token acquiring  
**api/token/refresh/** - JWT token refresh  