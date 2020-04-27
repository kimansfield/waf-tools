#!/usr/bin/env python
# encoding: utf-8

from waflib.Configure import conf

from . import emscripten_common


@conf
def cxx_default_emscripten(conf):
    print('***emscripten_mkspecs.py::cxx_default_emscripten')
    """
    Detect and setup the default em++ compiler
    """
    conf.mkspec_emscripten_configure(1, 25, minimum=True)


@conf
def cxx_emscripten125(conf):
    print('***emscripten_mkspecs.py::cxx_emscripten125')
    """
    Detect and setup the em++ 1.25 compiler
    """
    conf.mkspec_emscripten_configure(1, 25)


@conf
def cxx_emscripten126(conf):
    print('***emscripten_mkspecs.py::cxx_emscripten126')
    """
    Detect and setup the em++ 1.26 compiler
    """
    conf.mkspec_emscripten_configure(1, 26)


@conf
def cxx_emscripten127(conf):
    print('***emscripten_mkspecs.py::cxx_emscripten127')
    """
    Detect and setup the em++ 1.27 compiler
    """
    conf.mkspec_emscripten_configure(1, 27)


@conf
def cxx_emscripten130(conf):
    print('***emscripten_mkspecs.py::cxx_emscripten130')
    """
    Detect and setup the em++ 1.30 compiler
    """
    conf.mkspec_emscripten_configure(1, 30)

    


@conf
def cxx_emscripten134(conf):
    print('***emscripten_mkspecs.py::cxx_emscripten134')
    """
    Detect and setup the em++ 1.34 compiler
    """
    conf.mkspec_emscripten_configure(1, 34)


@conf
def cxx_emscripten137(conf):
    print('***emscripten_mkspecs.py::cxx_emscripten137')
    """
    Detect and setup the em++ 1.37 compiler
    """
    conf.mkspec_emscripten_configure(1, 37)
