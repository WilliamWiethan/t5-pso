install:
	pip install -r requirements.txt

test:
	cd ./source && python manage.py test 
	pipenv run pytest test/test_django_heroku.py