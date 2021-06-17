PROJECT_NAME := two-sum

# Build directories location
INC_DIR := .
SRC_DIR := .
OBJ_DIR := obj
OUT_DIR := .

# Object files list
CPP_FILES := $(wildcard $(SRC_DIR)/*.cpp)
O_FILES := $(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(CPP_FILES))

# Cross-compiler setup
CC=clang++
AR=ar

# Base name for output files (.elf, .bin, .sym, .S etc)
TARGET_NAME := $(PROJECT_NAME)
TARGET := $(OUT_DIR)/$(TARGET_NAME)

# C compiler parameters
C_PARAMS += -O2 -g -fsanitize=address

# GCC warnings
C_WARN += -Wall -Wextra -Wconversion -Wsign-conversion -Weffc++ -Wno-unused-function

# C linker parameters
L_PARAMS += -flto -Wl,--gc-sections -lasan

all: prep build

.PHONY: build
build: $(TARGET)

.PHONY: prep
prep:
	mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o: %.cpp
	@echo "# $<:"
	$(CC) $(C_PARAMS) $(C_WARN) $(C_DEF) -c -o $@ $<

$(TARGET): $(O_FILES)
# Link object files
	@echo "# Linking '$(TARGET)'"
	$(CC) $(L_PARAMS) -o $(TARGET).elf $(O_FILES)

# Show sections size
	@echo "# Binary info"
	size $(TARGET).elf

.PHONY: clean
clean:
	@echo "# Cleaning build-time generated files"
	rm -f $(OBJ_DIR)/*.o
	rm -f $(OUT_DIR)/$(TARGET_NAME).elf
