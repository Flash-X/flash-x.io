---
layout: page
title: Flash-X Source
subtitle:  
---

# Obtaining the Code
The source code is hosted at [https://github.com/Flash-X/Flash-X](https://github.com/Flash-X/Flash-X). 
It is distributed under Apache 2.0 license. The repository is not public, however, because we are required 
by our funders to maintain a list of users who obtain the code from the repository. Therefore you must 
be a GitHub user and become a collaborator of the repository to obtain the code from us. Please email 
<a href="mailto:flash-x@lists.cels.anl.gov">flash-x@lists.cels.anl.gov</a> with your github ID to get access.

<hr>

# Documentation
- [Flash-X User Guide](https://flash-x.github.io/Flash-X-docs/#)
- [Flash-X API](../../api/index.html)

<hr>

# Naming Conventions
- Units: Unit names have their first letter capitalized, for example
  `Grid`, `Eos`, `Hydro` etc.

- Sub-units: Sub-units have composite names that include a full unit name
  followed by a capitalized word describing the subunit, for example `GridMain`, 
  `GridParticles`, `HydroMain` etc. Every unit has at least one subunit named `UnitMain`.

- Sub-units Implementations: The directories containing implementations of sub 
  units have the following convention: If there are no implementations of the unit API 
  in any of its child directories, then the current directory name is capilaized, otherwise 
  it is all smallcase. 

- Organizational directories: These directory are normal unix directories, used for 
  organizational purposes. For example `physics` is an organizational directory
  for all the physics units. All helper and utilities directories are lowercase too.

- Unit API functions: `Unit_routineName` is the typical format of API function names.
  The unit name is followed by an underscore. The first word in the  remaining part of 
  the name is lowercase and all subsequent words are capitalized. For example, 
  `Grid_fillGuardcells`, `Driver_getDt` etc.

- Private Unit funtions: The private functions are named `un_routineName`, where `un` 
  stands for a short string (usually 2 or 3 letters) derived from the unit name. For example 
  `gr_createDomain` is a private function in the `Grid` unit.

- Kernel functions: They are not required to, but encouraged to follow the Private unit
  function convention.

- Unit Data modules: The main data modules are named `Unit_main`. For additional data 
  modules, the naming convention is similar to private functions, the unit name is replaced 
  by the short string. There are no such data modules in the current release, but an
  example would be `hy_ppmData`, if we needed a data module for the PPM kernel in the `Hydro` unit.

- Constants: The Constants are mostly defined in the pre-processor format 
  `#define CONSTANT_NAME` value. They are all uppercase, sometimes multiple words are separated 
   by an underscore. They are avaiable in `name.h` header files

- Variables: The unit-scope variables, defined in `Unit_data`, begin with `un_`, similar to the 
  convention for private function. For example, `gr_myPe` and `gr_procGrid` are variables in the 
  `Grid` unit. Variables local to a function are not constrained to be named in any specific way.

<hr>

# Contribution Policies
We encourage code contributions from the community. Contributors with
read only permission should use the following guidelines to create a
pull request:

- Create a fork.
- Make your changes.
- Create a PR to the **staged** branch whenever you wish.
  Give your PR a title that begins with the word "Draft".
  This will allow any discussion about the pull
  request to be conducted on github.
- When you are ready for the pull request to be accepted, merge from **main**
into your forked code, to ensure that your fork is not out of sync.
- Run a local version of your test suite and make sure everything
passes.
- Make sure your latest commit has been pushed.
- Remove "Draft" from your pull request name. If no further problems
are found, this will cause the PR
to be merged. The test suite is run at night if one of more
PRs have been merged into the **staged** branch.
- If the test suite passes, a composite PR will be created from
**staged** into **main**, and you won't have to do anything more.
- If the test suite fails, it is expected that you will resolve the
  failures immediately. If the failures continue over several
  iterations, or if the conflicts prove to be non-trivial, the
  resolution will involve someone designated by the Council to work
  with you.

Contributors with write permission should create a feature branch
instead of a fork. The remainder of the workflow remains the same.
