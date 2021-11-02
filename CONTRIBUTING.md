# Contributing

Contributions of features, and enhancements to this repository must be created in "issues", 
marked with appropriate flag and consensusly discussed among the group before making changes to the stable code base.


We have a code of conduct (CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Pull Request Process

1. Persist GITS project quality.
2. Link the ISSUE appropriately with the Pull request.
3. Request a PR to all the team members. The reviewer should not be the same as PR owner.
4. The reviewers must approve the pull request before merge the code. If not approved, discuss with comments to address the issue.
5. An appropriate issue description maintains quality of the project.
6. All the development code should accompany unit test cases to suppor the validation results.
7. Travis Builds should be passing while the code is generated.
8. The development code should be style checked, well formatted and syntax error free. Use of pep8, autoflake8 and flake8 tools will enable the users to get the required code quality.
9. Commit messages should company details of the changes been made.

## Bug Report Process

Bugs are tracked as GitHub issues. You need to create an issue and include all the following details if possible.

Explain the problem and include additional details to help maintainers reproduce the problem:

1. Before raising a GitHub issue, make sure that you are running the latest version of the application and have all recommended OS updates / patches installed
2. Use a clear and descriptive title for the issue to identify the problem.
3. Describe the exact steps which reproduce the problem in as many details as possible. For example, start by explaining how you started Atom, e.g. which command exactly you used in the terminal, or how you started Atom otherwise. When listing steps, don't just say what you did, but explain how you did it. For example, if you moved the cursor to the end of a line, explain if you used the mouse, or a keyboard shortcut or an Atom command, and if so which one?
4. Provide specific examples to demonstrate the steps. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use Markdown code blocks.
5. Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
6. Explain which behavior you expected to see instead and why.
7. Include screenshots and animated GIFs which show you following the described steps and clearly demonstrate the problem.


## Extension of project capability suggestion procedure

Bugs are tracked as GitHub issues. You need to create an issue and include all the following details if possible.

1. Use a clear and descriptive title for the issue to identify the suggestion.
2. Provide a step-by-step description of the suggested enhancement in as many details as possible.
3. Provide specific examples to demonstrate the steps.
4. Describe the current behavior and explain which behavior you expected to see instead and why.
5. Explain why this enhancement would be useful to most users and isn't something that can or should be implemented as a community package.
6. List some other repo or applications where this enhancement / feature exists. ( this is optional )

 
## Style Checker and Analyzer
We are using flake8 as our style checker and code analyzer. While contrivuting to this project, make sure you conform to norms dictated by flake8
### Flake8 
<b>Installation</b>
- `python<version> -m pip install flake8`

If you want Flake8 to be installed for your default Python installation, you can instead use:
- `python -m pip install flake8`

 <b>Using Flake8</b> 
 <br/>To start using Flake8, open an interactive shell and run one of the following,
- `flake8 path/to/code/to/check.py`
- `flake8 path/to/code/`

