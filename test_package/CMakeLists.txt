cmake_minimum_required(VERSION 2.8.12)

project(test CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test main.cpp)
target_link_libraries(test CONAN_PKG::text_encoding_detect)

