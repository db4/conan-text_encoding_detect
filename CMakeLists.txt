cmake_minimum_required(VERSION 2.8.12)

project(text_encoding_detect CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

include_directories(${SRC_DIR})

add_library(${PROJECT_NAME} ${SRC_DIR}/text_encoding_detect.cpp)
