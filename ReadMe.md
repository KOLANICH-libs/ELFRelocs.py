ELFRelocs.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[wheel (GitLab)](https://gitlab.com/KOLANICH/ELFRelocs.py/-/jobs/artifacts/master/raw/dist/ELFRelocs-0.CI-py3-none-any.whl?job=build)~~
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/ELFRelocs.py/workflows/CI/master/ELFRelocs-0.CI-py3-none-any.whl)~~
~~![GitLab Build Status](https://gitlab.com/KOLANICH/ELFRelocs.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/ELFRelocs.py/badges/master/coverage.svg)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/ELFRelocs.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/ELFRelocs.py/actions/)~~
![N∅ hard dependencies](https://shields.io/badge/-N∅_Ъ_deps!-0F0)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/ELFRelocs.py.svg)](https://libraries.io/github/KOLANICH-libs/ELFRelocs.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

A framework to compute relocations for ELF file format.

You inherit the class `Relocator` and `RelocWrapper` and implement everything which is NotImplemented. Then you call the method `computeRelocatedPtr` passing there **RAW Virtual address of a pointer** and **its value**, and get the relocated address (linker gonna patch the program, replacing that pointer with this value when loading, if everything dependent is loaded by the desired addresses).

`libs` submodule contains some already implemented relocators for some libs.


Requirements
------------
* [`ELFMachine`](https://codeberg.org/KOLANICH-libs/ELFMachine.py)
