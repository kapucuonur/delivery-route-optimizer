# Makefile for Delivery Route Optimizer

# Python interpreter from venv
PYTHON = venv/bin/python3
PIP = venv/bin/pip

.PHONY: install test run clean

# Default target
all: install test run

# Create venv and install dependencies
install:
	python3 -m venv venv
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencies installed successfully."

# Run unit tests
test:
	$(PYTHON) -m pytest tests
	@echo "✅ Tests passed."

# Run the application with default settings (30 stops, 3 vehicles)
run:
	$(PYTHON) main.py --stops 30 --vehicles 3
	@echo "✅ Application ran successfully. Check delivery_map.html"

# Clean up generated files
clean:
	rm -rf venv
	rm -rf __pycache__
	rm -rf delivery_optimizer/__pycache__
	rm -rf tests/__pycache__
	rm -f delivery_map.html
	@echo "🧹 Cleaned up project."
