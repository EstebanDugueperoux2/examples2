#pragma once

#ifdef _WIN32
  #define conan_swig_example_EXPORT __declspec(dllexport)
#else
  #define conan_swig_example_EXPORT
#endif

conan_swig_example_EXPORT void conan_swig_example();
