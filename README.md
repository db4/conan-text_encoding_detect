# conan-text_encoding_detect

[Conan.io](https://conan.io) package for [C# and C++ UTF8/UFT16 encoding detection library](https://github.com/AutoItConsulting/text-encoding-detect)

| Appveyor | Travis |
|-----------|--------|
|[![Build Status](https://ci.appveyor.com/api/projects/status/github/db4/conan-text_encoding_detect?branch=master&svg=true)](https://ci.appveyor.com/project/db4/conan-text_encoding_detect)|[![Build Status](https://travis-ci.org/db4/conan-text_encoding_detect.svg?branch=master)](https://travis-ci.org/db4/conan-text_encoding_detect)|

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload text_encoding_detect/0.0.1/stable --all

## Reuse the packages

### Basic setup

    $ conan install text_encoding_detect/0.0.1/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    text_encoding_detect/0.0.1/stable

    [generators]
    txt
    cmake


