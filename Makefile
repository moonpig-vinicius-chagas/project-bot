.PHONY: build


all: setup

setup:
	pipenv install --dev --skip-lock

web:
	pipenv run python3 app-web.py

util:
	pipenv run python3 util.py

test:
	pipenv run python3 test.py
	
clean:
	pipenv --rm

