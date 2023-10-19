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

**We have moved to https://codeberg.org/KOLANICH-libs/ELFRelocs.py , grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

A framework to compute relocations for ELF file format.

You inherit the class `Relocator` and `RelocWrapper` and implement everything which is NotImplemented. Then you call the method `computeRelocatedPtr` passing there **RAW Virtual address of a pointer** and **its value**, and get the relocated address (linker gonna patch the program, replacing that pointer with this value when loading, if everything dependent is loaded by the desired addresses).

`libs` submodule contains some already implemented relocators for some libs.


Requirements
------------
* [`ELFMachine`](https://codeberg.org/KOLANICH-libs/ELFMachine.py)
