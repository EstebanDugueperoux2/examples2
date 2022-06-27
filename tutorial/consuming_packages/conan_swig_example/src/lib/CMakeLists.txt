add_library(conan_swig_example_lib conan_swig_example.cpp)
target_include_directories(conan_swig_example_lib PUBLIC ../../include)

# Python binding
find_package(SWIG REQUIRED)
# To access Python.h
find_package(Python3 COMPONENTS Interpreter Development)
include(${SWIG_USE_FILE})

set(swig_sources conan_swig_example.i)
set_property(SOURCE ${swig_sources} PROPERTY CPLUSPLUS ON)

set(CMAKE_SWIG_OUTDIR ${CMAKE_CURRENT_BINARY_DIR})

swig_add_library(conan_swig_example_lib_python_binding
TYPE SHARED
LANGUAGE python
SOURCES	${swig_sources}
)
target_include_directories(conan_swig_example_lib_python_binding PRIVATE ${Python3_INCLUDE_DIRS})



install(TARGETS conan_swig_example_lib)

install(TARGETS conan_swig_example_lib_python_binding)
#install(FILES conan_swig_example_lib_python_binding.py)