PROJECT_NAME=silver-trader

CUR_DIR=$(CURDIR)
PYTHON_CMD=python

all: run

run:
	$(PYTHON_CMD) $(CUR_DIR)/trader/main.py