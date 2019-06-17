install:
	pip install -r requirements.txt

test:
	cd ./source && python manage.py test 
	pipenv run pytest source/test_deploy.py