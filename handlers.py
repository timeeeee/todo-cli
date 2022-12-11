import argparse
import os

import sqlalchemy

sql_uri = os.env["TODO_DB"]
engine = sqlalchemy.create_engine(sql_uri)

def get_with_prompts(field_names):
    results = {}
    for field, pretty_name in field_names.items():
        value = input(f"{pretty_name}: ")
        results[field] = None if value == "" else value

    return results


def new_category(args: argparse.Namespace):
    if argparse.Namespace.is_interactive:
        fields = get_with_prompts({
            "name": "Name",
        })

        name = fields["name"]
    else:
        name = args.name

    with engine.begin() as conn:
        

    
def get_category(args: argparse.Namespace):
    ...


def update_category(args: argparse.Namespace):
    ...


def delete_category(args: argparse.Namespace):
    ...
