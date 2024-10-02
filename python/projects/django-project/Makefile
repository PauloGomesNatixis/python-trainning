#make run para executar
makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic -c --noinput --no-post-process

run: collectstatic makemigrations migrate
	poetry run python manage.py runserver

test:
	poetry run pytest -sv -k test_monkeypatch