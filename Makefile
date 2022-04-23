build:
	docker build -t amazonscraper .

develop:
	docker build -t amazonscraper .
	docker run -it --rm --name amazonscraper -v ~/Desktop/amazonpricetrackservice:/app amazonscraper bash