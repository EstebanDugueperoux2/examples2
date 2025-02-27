# Conan 2.0 examples

## Tutorial

### Consuming packages

### [Build a simple CMake project using Conan](tutorial/consuming_packages/simple_cmake_project/)

- Use Conan to manage dependencies for a simple application, a string compressor that uses Zlib. [Docs](https://docs.conan.io/en/2.0-alpha/tutorial/consuming_packages/build_simple_cmake_project.html)

### [Using build tools as Conan packages](tutorial/consuming_packages/tool_requires/)

- Use Conan to install and use build tools like CMake. [Docs](https://docs.conan.io/en/2.0-alpha/tutorial/consuming_packages/use_tools_as_conan_packages.html)

### [Building for multiple configurations: Release, Debug, Static and Shared](tutorial/consuming_packages/different_configurations/)

- Learn how to build for different configurations, like Release or Debug and build shared or static libraries. [Docs](https://docs.conan.io/en/2.0-alpha/tutorial/consuming_packages/different_configurations.html)

### [Using conanfile.py vs conanfile.txt](tutorial/consuming_packages/conanfile_py/)

- Learn about the flexibility of using a conanfile.py instead a conanfile.txt. [Docs](https://docs.conan.io/en/2.0-alpha/tutorial/consuming_packages/the_flexibility_of_conanfile_py.html)

### [How to cross-compile your applications using Conan](tutorial/consuming_packages/cross_building/)

- Learn how to cross-compile your applications with Conan. [Docs](https://docs.conan.io/en/2.0-alpha/tutorial/consuming_packages/cross_building_with_conan.html)

### [How to use SWIG with Conan to have its package consumable from other languages as Python](tutorial/consuming_packages/cp,a,_swig_example/)

- Learn how to use SWIG with Conan to have its package consumable from Python:

- cd tutorial/consuming_packages/conan_swig_example/
- docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc7
# SWIG needs Python.h from python3-dev ubuntu package
- sudo apt-get update
- sudo apt-get install python3-dev
- cd project
- conan create . --profile profile
