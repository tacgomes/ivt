#!/usr/bin/env python

import sys
import re
import optparse

def raise_invalid_value():
    sys.stderr.write("Error: invalid value\n")
    sys.exit(1)

def raise_missing_value():
    sys.stderr.write("Error: missing value\n")
    sys.exit(2)

def main():
    parser = optparse.OptionParser()
    parser.add_option('--hour', action="store", type="int")
    parser.add_option('--username', action="store")
    parser.add_option('--day', action="store")
    options, args = parser.parse_args()

    subcommand=args[0]
    if subcommand == 'set-time':
        if options.hour:
            if options.hour < 0 or options.hour > 24:
                raise_invalid_value()
        else:
            raise_missing_value()

        if options.day:
            if options.day not in ['mon','tue','wed','thu',
                                   'fri', 'sat', 'sun']:
                raise_invalid_value()
    elif subcommand == 'adduser':
        if options.username:
            if not re.match('[a-z_][a-z0-9_]{0,30}', options.username):
                raise_invalid_value()
        else:
            raise_missing_value()
    else:
        sys.stderr.write("Error: invalid value\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
