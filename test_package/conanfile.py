from conans import ConanFile, CMake
import os

class TestConan(ConanFile):
    settings = "os", "arch", "compiler"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run("bin%stest %s" % (os.sep, os.path.join(self.source_folder, "utf8.txt")))
