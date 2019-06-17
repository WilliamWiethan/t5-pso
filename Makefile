install:
	pip install -r requirements.txt

test:
	cd ./source && python manage.py test && python test_deploy.py