# The name of the application to be built (binary will be this with a `.aplx`
# extension)
APP = arma

# Directory to place compilation artefacts (must include trailing slash)
BUILD_DIR = ./build/

# The sources to be compiled
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
CURRENT_DIR := $(dir $(MAKEFILE_PATH))
SOURCE_DIR := $(abspath $(CURRENT_DIR))/src
SOURCE_DIRS := $(SOURCE_DIR)

SOURCES = arma.c

# will editing this here work to add -std=c99? yes but it doesn't help... 
CFLAGS += -fcx-limited-range $(OSPACE) -l m
# OFLAGS += -fcx-limited-range 

include ../../Makefile.common
