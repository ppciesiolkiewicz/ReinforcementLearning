

__start__: 
	python src/main.py settings.ini $(section) $(plot)

lecture:
	python src/main.py settings.ini lecture $(plot)

site:
	python src/main.py settings.ini site $(plot)


extra:
	python src/main.py settings.ini extra $(plot)



clean:
	find . -name *.pyc | xargs rm -rf
	find . -name __pycache__ | xargs rm -rf

help:
	@echo plot parameter indices for which field
	@echo plot should be painted. 
	@echo Fields are numerated as follows: from left to right and bottom up
	@echo 8 9 10 11
	@echo 4 5 6  7
	@echo 0 1 2  3
	@echo To paint plot for field 0,2,11 - make plot=[0,2,11] 

