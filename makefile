

__start__: lecture

lecture:
	python src/main.py settings.ini lecture

site:
	python src/main.py settings.ini site

clean:
	find . -name *.pyc | xargs rm -rf
	find . -name __pycache__ | xargs rm -rf
