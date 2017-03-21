## Why need shared library?
  extension, dynamically loadable module

  ### Compiler and object files
  compiler converts source files to object file. Object file has serveral different sections.
  * text: machine code instructions
  * data: global variable
  * read-only: constants
  * symbol table: identifiers appear in the source file (Unix command "nm" to check symbol table of object file)
  
  ### Linker and executable
  linker collects object files and library into executable.
  * concatenate all object files together into one file
  * bind symbol name to real memory address
  
  ### Static library
  collection of raw object files
  weakpoint: many copies in different application; need to recompile/relink if update the static libarary
  
  ### Shared library
  delay the link to runtime
  All application/binary that depend on the library share the same instance in memory.
  
  "the operating system can arrange to place library code in read-only memory regions shared among processes (using page-sharing and other virtual memory techniques)."
  "the dynamic linker searches libraries in the same order as they were specified on the link line and uses the first definition of the symbol encounted."
  
  ### Dynamic binding
  watch the binding by setting LD_DEBUG=bindings
  "When a program linked with shared libraries runs, program execution does not immediately start with that program’s first statement. Instead, the operating system loads and executes the dynamic linker (usually called ld.so), which then scans the list of library names embedded in the executable."
  
  "To locate the libraries, the dynamic linker uses a configurable library search path. This path’s default value is normally  stored  in  a  system  configuration  file  such  as /etc/ld.so.conf . Additionally, other library search directories might be embedded in the executable or specified by the user in the LD_LIBRARY_PATH environment variable."
  
  "You can obtain detailed information about how the dynamic linker loads libraries by setting the LD_DEBUG environment variable to libs"
  
  set LD_LIBRARY_PATH is always a bad idea for redirect the linker search path.
  
  Instead, A better solution is to embed customized search paths in the executable itself using special linker options such as -R or -Wl, -rpath


  
  [Reference: the inside story on shared libraries and dynamic loading]( https://cseweb.ucsd.edu/~gbournou/CSE131/the_inside_story_on_shared_libraries_and_dynamic_loading.pdf)
  
## What is shared library?

## How to generate SO?

## How SO used/linked?

readelf -d lib.so
