.PHONY: build


all: setup

setup:
	pipenv install --dev --skip-lock

main:
	pipenv run python3 main.py

util:
	pipenv run python3 util.py

test:
	pipenv run python3 test.py
	
clean:
	pipenv --rm