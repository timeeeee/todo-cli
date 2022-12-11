"""
generally: has subcommands for each type of "thing"
each "thing" has subcommands for new, get, update, delete

TODO: why does making the subcommands required give me "expected str, got None" error
when running with no subcommand?
===============================================================================
"""

import argparse

import handlers

handlers = {
    "category": {
        "new": handlers.new_category,
        "get": handlers.get_category,
        "update": handlers.update_category,
        "delete": handlers.delete_category
    }
}
    

parser = argparse.ArgumentParser(
    prog = 'add_task',
    description = 'Add a task to Tim\'s todos')

subparsers = parser.add_subparsers(title="object type", dest="object")


# ========== tasks ==========

task_parser = subparsers.add_parser("task")
task_subparsers = task_parser.add_subparsers(title="action", dest="action")

new_task_parser = task_subparsers.add_parser("new")


# ========== categories ==========

category_parser = subparsers.add_parser("category")
category_subparsers = category_parser.add_subparsers(title="action", dest="action")

new_category_parser = category_subparsers.add_parser("new")
get_category_parser = category_subparsers.add_parser("get")
update_category_parser = category_subparsers.add_parser("update")
delete_category_parser = category_subparsers.add_parser("delete")

new_category_parser.add_argument("-i", "--interactive", action="store_true")

get_category_parser.add_argument("category_id")

update_category_parser.add_argument("-i", "--interactive", action="store_true")

delete_category_parser.add_argument("category_id")


# ========== projects ==========

project_parser = subparsers.add_parser("project")


"""
parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                                        action='store_true')  # on/off flag
"""


if __name__ == "__main__":
    args = parser.parse_args()

    handler = handlers[args.object][args.action]
    handler(args)
