# Define the Python environment and the script to run
PYTHON=python
SCRIPT=process_data.py
CSV_INPUT=offers.csv
CSV_OUTPUT=transformed_offers.csv

# Default target
all: transform

# Target to transform the data
transform:
	$(PYTHON) $(SCRIPT)

# Clean up generated files
clean:
	rm -f $(CSV_OUTPUT)

.PHONY: all transform clean

