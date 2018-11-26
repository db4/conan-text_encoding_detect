from conans import ConanFile, CMake, tools

class TextEncodingDetectConan(ConanFile):
    name = "text_encoding_detect"
    version = "0.0.1"
    license = "Apache License 2.0"
    url = "https://github.com/db4/conan-text_encoding_detect.git"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "*.patch"
    generators = "cmake"
    _revision = "44b48011e4180fe0da6aa0d06d13586d7c5006b5"

    @property
    def src_dir(self):
        return "text-encoding-detect-%s/TextEncodingDetect-C++/TextEncodingDetect" % self._revision

    def source(self):
        tools.get("https://github.com/AutoItConsulting/text-encoding-detect/archive/%s.zip" % self._revision,
                  md5="a0d3a50b3d1d45bdd86986ebf1e8d849")
        tools.patch(base_path=self.src_dir, patch_file='TextEncodingDetect.patch')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["SRC_DIR"] = self.src_dir
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*/LICENSE.txt", dst=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
