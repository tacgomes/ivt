ivt
===

`ivt` it a tool to exercise and test the input validation paths for a command
line tool which allows to specify options in the conventional GNU/POSIX syntax.
`ivt` stands for Input Validation Tester.

It requires as input a spec file which defines the options that the command
line tool supports, their valid combinations, and which are the valid input
values for those options.

Each spec file consists in set of lines that starts with a keyword (_regex_,
_range_ or _enum_) or with the name of the tool being tested.  Empty lines or
lines starting with '#' are ignored.

Lines that start with a keyword define variables that can be used to specify
which are the valid input values for some option.  Variables of type _regex_
allow to define a constraint on the string value based on a regular expression,
variables of type _range_ allow to define which are the lowest and/or highest
valid numeric values, variables of type _enum_ allow to define the allowed
fixed set of string constants.

Lines starting with the name of the tool lines specify the valid combination of
options, and which are their valid input values for its arguments based on the
variables which have been defined. Options defined inside square brackets mean
that they can be omitted.

See `example.spec` for an example and further documentation.

`ivt` will check that the command will fail if the input value does not match
the regex, or its lower/higher than the lower/upper limit, or it isn't on the
list of string constants.  The opposite check will also be performed: whether
the command succeeds if the input value is valid accordingly to the defined
variable.  Executing commands with their optional options omitted will also be
tested.

The check for whether the input validation succeed or not based is on the
command exit status. It's possible that the command failed due some other
reason than the validation not being done properly.  To handle this situation,
you can pass a `--error-string="Error: invalid value"` option which will search
on the command's standard error for the given string.


Caveats
-------
Optional arguments (an argument can be or not given for some option) and
multiple short options without arguments (e.g. -abc) are not supported.
