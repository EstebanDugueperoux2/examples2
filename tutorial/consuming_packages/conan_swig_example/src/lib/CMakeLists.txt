add_library(conan_swig_example_lib conan_swig_example.cpp)
target_include_directories(conan_swig_example_lib PUBLIC ../../include)

# Python binding
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

set(swig_sources conan_swig_example.i)
set_property(SOURCE ${swig_sources} PROPERTY CPLUSPLUS ON)

set(CMAKE_SWIG_OUTDIR ${CMAKE_CURRENT_BINARY_DIR})

swig_add_library(${target}
	TYPE SHARED
	LANGUAGE python
    SOURCES	${swig_sources}
)



install(TARGETS conan_swig_example_lib)
