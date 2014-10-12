# Spec file for testing the validation of example.py
# ==================================================

# Variables definition
# --------------------
#
# On a variable definition, there shouldn't be any whitespace before and after
# '='. Regexes should be a Perl-style regular expression pattern.  Ranges
# should have their lowest and highest value separated by '..' (the lowest or
# highest value can be omitted).  Enums should have each string constant
# separated by a ','.
regex timezone=\w+
regex username=[a-z_][a-z0-9_]+
range hour=0..24
range minsec=0..60
enum  verbosity=info,warn,error

# Options definition
# ------------------
#
# Variables can be referenced by prefixing the name of the variable with '$'.
# Each option and variable should be separated by '=' and not whitespace.  This
# stands for both sort and long options (although GNU getopt does not support
# separating a short option and its argument by '=', internally '=' will be
# converted to whitespace).  Options defined inside square brackets are not
# required for some command/subcommand.
./example.py help
./example.py add-user --username=$username
./example.py set-time --hour=$hour --minute=$minsec --second=$minsec [ --timezone=$timezone ]
./example.py show-log [ --verbosity=$verbosity ]
./example.py show-log [ -v=$verbosity ]
