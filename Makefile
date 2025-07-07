#!/usr/bin/make -f
# -*- makefile -*-

SHELL         := /bin/bash
.SHELLFLAGS   := -eu -o pipefail -c
.DEFAULT_GOAL := help
.LOGGING      := 0

.ONESHELL:             ;	# Recipes execute in same shell
.NOTPARALLEL:          ;	# Wait for this target to finish
.SILENT:               ;	# No need for @
.EXPORT_ALL_VARIABLES: ;	# Export variables to child processes.
.DELETE_ON_ERROR:      ;	# Delete target if recipe fails.

# Modify the block character to be `-\t` instead of `\t`
ifeq ($(origin .RECIPEPREFIX), undefined)
	$(error This version of Make does not support .RECIPEPREFIX.)
endif
.RECIPEPREFIX = -


PROJECT_DIR := $(shell git rev-parse --show-toplevel)
SRC_DIR     := $(PROJECT_DIR)/src
BUILD_DIR   := $(PROJECT_DIR)/dist

default: $(.DEFAULT_GOAL)
all: help


define Lint
-	black $(SRC_DIR)
-	ruff check $(SRC_DIR) --fix
endef


define TypeCheck
	python3 -m mypy src            \
		--ignore-missing-imports   \
		--follow-imports=skip      \
		--show-error-codes         \
		--show-column-numbers      \
		--pretty
endef


define Bandit
	bandit                 \
		-v                   \
		-f txt               \
		-r $1                \
		-c "pyproject.toml"
endef


.PHONY: help
help: ## List commands <default>
-	echo -e "USAGE: make \033[36m[COMMAND]\033[0m\n"
-	echo "Available commands:"
-	awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\t\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


.PHONY: build
build: ## Build the application
-	pip install wheel
-	pip install --upgrade pip wheel
-	pip install --editable .
-	hatch build --clean --target wheel


.PHONY: run
run: ## Run the application
-	prison-agents


.PHONY: lint
lint: ## Lint the code
-	$(call Lint)


.PHONY: type
type: ## Type check the code
-	$(call TypeCheck)


.PHONY: bandit
bandit: ## Run bandit
-	$(call Bandit,./src)
