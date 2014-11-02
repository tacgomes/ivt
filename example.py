#!/usr/bin/env python3

import sys
import re
import argparse


def invalid_value_err(option, value):
    sys.stderr.write("Error: invalid value '{}' for '{}'\n".format(
                     value, option))
    sys.exit(1)


def missing_option_err(option):
    sys.stderr.write("Error: option '{}' was not given\n".format(
                     option))
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
                invalid_value_err('hour', namespace.hour)
        else:
            missing_option_err('hour')
        if namespace.minute:
            if namespace.minute < 0 or namespace.minute > 60:
                invalid_value_err('minute', namespace.minute)
        else:
            missing_option_err('minute')
        if namespace.second:
            if namespace.second < 0 or namespace.second > 60:
                invalid_value_err('second', namespace.second)
        else:
            missing_option_err('second')
        if namespace.timezone is not None:
            if not re.match('\w+$', namespace.timezone):
                invalid_value_err('timezone', namespace.timezone)
    elif namespace.subcommand == 'add-user':
        if namespace.username is not None:
            if not re.match('[a-z_][a-z0-9_]+$', namespace.username):
                invalid_value_err('username', namespace.username)
        else:
            missing_option_err('username')
    elif namespace.subcommand == 'help':
         pass
    else:
        sys.stderr.write("Error: invalid value\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
