# etags-gen

Generate a TAGS file using `etags` with a basic list of include folders, exclude folders, and include file extensions as input. Here's a sample config file:

    [etags-gen-config]

    include-paths =
      /home/user/project/src
      /home/user/someother/src

    exclude-paths =
      /home/user/project/src/uninteresting_files

    include-extensions =
      .h
      .hpp
      .c
      .cxx
      .cpp
