from conans import ConanFile, CMake
#from conans import tools
#import os


class ImguiConan(ConanFile):
    name = "ImGui"
    version = "latest"
    license = "MIT"
    url = "https://github.com/thoughton/conan-imgui"
    description = "Bloat-free Immediate Mode Graphical User interface for C++ with minimal dependencies."

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "LICENSE"

    def source(self):
        self.run("git clone https://github.com/ocornut/imgui.git")

    def build(self):
        cmake = CMake(self)
        self.run('cmake . %s' % (cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="imgui", excludes="examples/*", keep_path=True)
        self.copy("*.lib", dst="lib", excludes="*/examples/*", keep_path=False)
        self.copy("*.dll", dst="bin", excludes="*/examples/*", keep_path=False)
        self.copy("*.so", dst="lib", excludes="*/examples/*", keep_path=False)
        self.copy("*.a", dst="lib", excludes="*/examples/*", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["imgui"]

