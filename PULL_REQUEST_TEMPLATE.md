A similar PR may already be submitted! Please search among the [Pull request](../) before creating one.

Thanks for submitting a pull request! Please provide enough information so that others can review your pull request:

For more information, see the `CONTRIBUTING` guide.


## Summary

<!-- Summary of the PR -->

This PR fixes/implements the following **bugs/features**

* [ ] Bug 1
* [ ] Bug 2
* [ ] Feature 1
* [ ] Feature 2
* [ ] Breaking changes

<!-- You can skip this if you're fixing a typo or adding an app to the Showcase. -->

* **What kind of change does this PR introduce?** (Bug fix, feature, docs update, ...)

<!-- Bug fix, feature, docs update, ... -->

* **What is the current behavior?** (You can also link to an open issue here)

<!-- You can also link to an open issue here -->

* **What is the new behavior (if this is a feature change)?**

<!-- If this is a feature change -->

* **Does this PR introduce a breaking change?** (What changes might users need to make in their application due to this PR?)

<!-- Example: When "Adding a function to do X", explain why it is necessary to have a way to do X. -->

## Checklist

* **Please check if the PR fulfills these requirements**
- [ ] The commit message follows our guidelines
- [ ] Tests for the changes have been added (for bug fixes / features)
- [ ] Docs have been added / updated (for bug fixes / features)

## Test plan (required)

Demonstrate the code is solid. Example: The exact commands you ran and their output, screenshots / videos if the pull request changes UI.

<!-- Make sure tests pass -->

## Closing issues

<!-- Put `closes #XXXX` in your comment to auto-close the issue that your PR fixes (if such). -->
Fixes #

## Other information:

<!-- Any other information that is important to this PR such as screenshots of how the component looks before and after the change. -->

## Note for Windows users

This site can be developed on Windows, however a few potential gotchas need to be kept in mind:

1. Regular Expressions: Windows uses `\r\n` for line endings, while Unix-based systems use `\n`. Therefore, when working on Regular Expressions, use `\r?\n` instead of `\n` in order to support both environments. The Node.js [`os.EOL`](https://nodejs.org/api/os.html#os_os_eol) property can be used to get an OS-specific end-of-line marker.
2. Paths: Windows systems use `\` for the path separator, which would be returned by `path.join` and others. You could use `path.posix`, `path.posix.join` etc and the [slash](https://ghub.io/slash) module, if you need forward slashes - like for constructing URLs - or ensure your code works with either.
3. Bash: Not every Windows developer has a terminal that fully supports Bash, so it's generally preferred to write [scripts](/script) in JavaScript instead of Bash.
4. Filename too long error: There is a 260 character limit for a filename when Git is compiled with `msys`. While the suggestions below are not guaranteed to work and could cause other issues, a few workarounds include:
    - Update Git configuration: `git config --system core.longpaths true`
    - Consider using a different Git client on Windows