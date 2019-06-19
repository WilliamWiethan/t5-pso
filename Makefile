install:
	pip install -r requirements.txt

test:
	pipenv run pytest source/test_deploy.py
	cd ./source && python manage.py test