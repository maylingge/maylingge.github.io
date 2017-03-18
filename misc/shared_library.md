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
  * conca
  
  [Reference: the inside story on shared libraries and dynamic loading]( https://cseweb.ucsd.edu/~gbournou/CSE131/the_inside_story_on_shared_libraries_and_dynamic_loading.pdf)
  
## What is shared library?

## How to generate SO?

## How SO used/linked?

readelf -d lib.so
