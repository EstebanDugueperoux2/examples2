# find_package(S)

add_subdirectory(lib)

add_executable(conan_swig_example_exe main.cpp)

target_link_libraries(conan_swig_example_exe conan_swig_example_lib)
target_include_directories(conan_swig_example_exe PUBLIC ../include)

install(TARGETS conan_swig_example_exe)
