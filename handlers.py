import argparse

import sqlalchemy
from sqlalchemy import select

import settings
from db.schema import Category

engine = sqlalchemy.create_engine(settings.sql_uri)

def get_with_prompts(field_names):
    results = {}
    for field, pretty_name in field_names.items():
        value = input(f"{pretty_name}: ")
        results[field] = None if value == "" else value

    return results


def new_category(args: argparse.Namespace):
    if args.is_interactive:
        fields = get_with_prompts({
            "name": "Name",
        })

        name = fields["name"]
    else:
        name = args.name


    with sqlalchemy.orm.Session(engine) as session:
        c = Category(name=name)
        session.add(c)
        session.commit()

    
def get_category(args: argparse.Namespace):
    if args.category_id is None:
        with sqlalchemy.orm.Session(engine) as session:
            categories = session.execute(select(Category)).all()
    else:
        with sqlalchemy.orm.Session(engine) as session:
            query = select(Category).where(Category.category_id == args.category_id)
            categories = session.execute(query).all()

    for row in categories:
        category = row[0]
        print(f"{category.category_id}: {category.name}")

            
def update_category(args: argparse.Namespace):
    ...


def delete_category(args: argparse.Namespace):
    ...
