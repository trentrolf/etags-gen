# etags-gen

Generate a TAGS file using `etags` with a basic list of include folders, exclude folders, and include file extensions as input.
The tool must be executed from a directory containing a file `etags-gen.ini` like the sample below.
Paths in the `.ini` can be relative to the current working directory, or absolute.

```
[etags-gen-config]

include-paths =
  ../src
  ../some-sdk

exclude-paths =
  ../build
  ../some-sdk/lib

include-extensions =
  .h
  .c
  .cxx
  .cpp
```
