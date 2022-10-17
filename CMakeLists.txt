cmake_minimum_required(VERSION 3.10)

project(cmake_header_generation_sample)

find_package (Python3 COMPONENTS Interpreter)

if(NOT Python3_Interpreter_FOUND)
    message(FATAL_ERROR "Python 3 interpreter not found!!!")
endif()

add_custom_command(
    OUTPUT genconfig.cpp
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/scripts/scr.py ${CMAKE_CURRENT_SOURCE_DIR}/scripts/string.txt ${CMAKE_CURRENT_BINARY_DIR}/genconfig.cpp
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/scripts/scr.py ${CMAKE_CURRENT_SOURCE_DIR}/scripts/string.txt
)

include_directories(src)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(program1_SRC
	src/src1.cpp
    genconfig.cpp
)

set(program1_NAME program1)
add_executable(${program1_NAME})

target_sources(${program1_NAME} PRIVATE ${program1_SRC})
