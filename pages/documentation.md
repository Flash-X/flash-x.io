---
layout: page
title: Flash-X Documentation
subtitle:  
---

# [User's guide](https://flash-x.github.io/Flash-X-docs/#)


# [API](https://flash-x.github.io/Flash-X-docs/doxygen/#)

# Inheritance 
A child of an included components inherits all
functions from the parent, except those for which it has its own
implementation. 

The implementation in the lowest level offspring replaces
all implementations that came before.

The Config files arbitrate on multiple implementations
existing at peer level by specifying ``DEFAULT''

An explicit ``include'' for a particular path in a Config file
causes all function implemented in lowest level directory in the path
to be selected.

An implementation in the problem specific directory of the Simulation
unit overrides all implementations elsewhere in the source tree. 


# Naming Conventions

Units
    Unit names have their first letter capitalized, for example
    Grid, Eos, Hydro etc

 Sub-units 
    Sub-units have composite names that include a full unit name
    followed by a capitalized word describing the subunit, for example  
    GridMain, GridParticles, HydroMain etc.
    Every unit has at least one subunit named UnitMain.

 Sub-units Implementations
    The directories containing implementations of sub units have the 
    following convention:
    If there are no implementations of the unit API in any of its child 
    directories, then the current directory name is capilaized, otherwise 
    it is all smallcase. 

 Organizational directories
    These directory are normal unix directories, used for organizational
    purposes. For example <physics> is an organizational directory
    for all the physics units. All helper and utilities directories are 
    lowercase too.

Unit API functions:
    Unit_routineName is the typical format of API function names.
    The unit name is followed by an underscore. The first word in the 
    remaining part of the name is lowercase and all subsequent words are
    capitalized. For example, Grid_fillGuardcells, Driver_getDt} etc

Private Unit funtions
    The private functions are named un_routineName, where {un} stands for
    a short string (usually 2 or 3 letters) derived from the unit name.
    For example gr_createDomain is a private function in the Grid unit.

Kernel functions 
    They are not required to, but encouraged to follow the Private unit
    function convention.

Unit Data modules
    The main data modules are named Unit_main.
    For additional data modules, the naming convention is similar
    to private functions, the unit name is replaced by the short string.
    There are no such data modules in the current release, but an
    example would be hy_ppmData, if we needed a data module for the PPM
    kernel in the Hydro unit.

Constants
    The Constants are mostly defined in the pre-processor format 
    #define CONSTANT_NAME value. They are all uppercase, sometimes
    multiple words are separated by an underscore. They are avaiable 
    in "name.h" header files

Variables
    The unit-scope variables, defined in Unit_data, begin
    with "un_'', similar to the convention for private function.
    For example, gr_myPe and gr_procGrid are variables in the Grid unit.
    Variables local to a function are not constrained to be 
    named in any specific way.


