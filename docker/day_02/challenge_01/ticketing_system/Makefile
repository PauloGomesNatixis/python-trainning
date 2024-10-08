#make run para executar

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic -c --noinput

run: makemigrations migrate collectstatic
	poetry run python manage.py runserver

