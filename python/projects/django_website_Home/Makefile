#make run para executar

poetry_init:
	#poetry init

poetry_install:
	poetry install

poetry_add_Django:
	poetry add Django

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

collectstatic:
# 	poetry run python manage.py collectstatic -c --noinput --no-post-process

run: poetry_install poetry_init poetry_add_Django makemigrations migrate collectstatic
	poetry run python manage.py runserver

