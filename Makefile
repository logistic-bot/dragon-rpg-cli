run:
	python src/main.py

test:
	pytest --cov=src --cov-config=.coveragerc -v

commit:
	git status
	git diff

style:
#	black src -l 100
	pylint -f colorized src -s yes --exit-zero
#	flake8 --max-complexity=5 --exit-zero --show-source
#	bandit src/main.py -q -s B311 -s B322
