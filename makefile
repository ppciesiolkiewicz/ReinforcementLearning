

__start__: lecture

lecture:
	python src/main.py settings.ini lecture plot

site:
	python src/main.py settings.ini site plot

clean:
	find . -name *.pyc | xargs rm -rf
	find . -name __pycache__ | xargs rm -rf
