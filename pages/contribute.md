---
layout: page
title: Contribute Code

---

# Contribution Policies

We encourage code contributions from the community. Contributors with
read only persmission should use the following guidelines to create a
pull request:

- Create a fork
- Make your changes
- Create a PR to the **merge** branch whenever you wish, named as Draft-
  <my PR>". This will allow any discussion about the pull
  request to be conducted on github.
- When you are ready for pull request to be accepted merge from main to
ensure that your fork is not out of sync.
- Run a local version of your test suite and make sure everything
passes.
- Remove "Draft" from your pull request name. This will cause the PR
to be merged. The test-suite is run at night if one of more
PR have been merged into the **merge** branch
- If the test-suite passes a composite PR will be created from
**merge** into **main** and you won't have to do anything more
- If the test-suite fails, it is expected that you will resolve the
  failures immediately. If the failures continue over several
  iterations, or if the conflicts prove to be non-trivial, the
  resolution will involve someone designated by the Council to work
  with you.

Contributors with write permission should create a feature branch
instead of a fork. The remainder of the workflow remains the same.


