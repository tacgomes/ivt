#!/usr/bin/env python

import sys
import re
import optparse

def raise_invalid_value(option, value):
    sys.stderr.write("Error: invalid value '{0}' for '{1}'\n".format(
                     value, option))
    sys.exit(1)

def raise_missing_option(option):
    sys.stderr.write("Error: option '{0}] was not give\n".format(option))
    sys.exit(2)

def main():
    parser = optparse.OptionParser()
    parser.add_option('--hour', action="store", type="int")
    parser.add_option('--minute', action="store", type="int")
    parser.add_option('--second', action="store", type="int")
    parser.add_option('--timezone', action="store")
    parser.add_option('--username', action="store")
    parser.add_option('-v', '--verbosity', action="store")
    options, args = parser.parse_args()

    subcommand=args[0]
    if subcommand == 'show-log':
         pass
         if options.verbosity:
             if options.verbosity not in ['info','warn','error']:
                 raise_invalid_value('verbosity', options.verbosity)
    elif subcommand == 'set-time':
        if options.hour:
            if options.hour < 0 or options.hour > 24:
                raise_invalid_value('hour', options.hour)
        else:
            raise_missing_option('hour')
        if options.minute:
            if options.minute < 0 or options.minute > 60:
                raise_invalid_value('minute', options.minute)
        else:
            raise_missing_option('minute')
        if options.second:
            if options.second < 0 or options.second > 60:
                raise_invalid_value('second', options.second)
        else:
            raise_missing_option('second')
        if options.timezone is not None:
            if not re.match('\w+$', options.timezone):
                raise_invalid_value('timezone', options.timezone)
    elif subcommand == 'add-user':
        if options.username is not None:
            if not re.match('[a-z_][a-z0-9_]+$', options.username):
                raise_invalid_value('username', options.username)
        else:
            raise_missing_option('username')
    elif subcommand == 'help':
         pass
    else:
        sys.stderr.write("Error: invalid value\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
