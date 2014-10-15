#!/usr/bin/env python3

import sys
import re
import argparse

def raise_invalid_value(option, value):
    sys.stderr.write("Error: invalid value '{}' for '{}'\n".format(
                     value, option))
    sys.exit(1)

def raise_missing_option(option):
    sys.stderr.write("Error: option '{}' was not given\n".format(option))
    sys.exit(2)

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    show_log_parser = subparsers.add_parser('show-log')
    show_log_parser.add_argument('-v', '--verbosity', action="store",
                                 choices=['info', 'warn', 'error'])

    add_user_parser = subparsers.add_parser('add-user')
    add_user_parser.add_argument('--username', action="store",
                                 required=True)

    set_time_parser = subparsers.add_parser('set-time')
    set_time_parser.add_argument('--hour', action="store",
                                 required=True, type=int)
    set_time_parser.add_argument('--minute', action="store",
                                 required=True, type=int)
    set_time_parser.add_argument('--second', action="store",
                                 required=True, type=int)
    set_time_parser.add_argument('--timezone', action="store")

    help_parser = subparsers.add_parser('help')

    namespace = parser.parse_args()

    if namespace.subcommand == 'show-log':
         pass
    elif namespace.subcommand == 'set-time':
        if namespace.hour:
            if namespace.hour < 0 or namespace.hour > 24:
                raise_invalid_value('hour', namespace.hour)
        else:
            raise_missing_option('hour')
        if namespace.minute:
            if namespace.minute < 0 or namespace.minute > 60:
                raise_invalid_value('minute', namespace.minute)
        else:
            raise_missing_option('minute')
        if namespace.second:
            if namespace.second < 0 or namespace.second > 60:
                raise_invalid_value('second', namespace.second)
        else:
            raise_missing_option('second')
        if namespace.timezone is not None:
            if not re.match('\w+$', namespace.timezone):
                raise_invalid_value('timezone', namespace.timezone)
    elif namespace.subcommand == 'add-user':
        if namespace.username is not None:
            if not re.match('[a-z_][a-z0-9_]+$', namespace.username):
                raise_invalid_value('username', namespace.username)
        else:
            raise_missing_option('username')
    elif namespace.subcommand == 'help':
         pass
    else:
        sys.stderr.write("Error: invalid value\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
