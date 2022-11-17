rm db.sqlite3
rm -rf ./lightningapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations lightningapi
python3 manage.py migrate lightningapi
python3 manage.py loaddata users
python3 manage.py loaddata rare_users
python3 manage.py loaddata tokens
python3 manage.py loaddata reactions
python3 manage.py loaddata categories
python3 manage.py loaddata tags 
python3 manage.py loaddata posts
python3 manage.py loaddata comments
python3 manage.py loaddata subscriptions
python3 manage.py loaddata post_tags
python3 manage.py loaddata post_reactions