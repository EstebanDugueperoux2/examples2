from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class ConanSwigExampleConan(ConanFile):
    name = "conan_swig_example"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of ConanSwigExample here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    requires = ("swig/4.0.2")
    tool_requires = ("cmake/3.23.2", "ninja/1.11.0", "ccache/4.6")
    build_policy = "missing"
    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["conan_swig_example_lib"]
        self.cpp_info.bin = ["conan_swig_example_exe"]
