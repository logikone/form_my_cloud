.PHONY: help
help:
	@echo "clean - clean up"

.PHONY: clean
clean:
	rm -rf build
	rm -rf *.egg-info
	rm -rf .eggs
	rm -rf .coverage
	find . -type f -name *.pyc -delete
