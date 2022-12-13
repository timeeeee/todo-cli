import argparse

import sqlalchemy
from sqlalchemy import select

import settings
from db.schema import Category

engine = sqlalchemy.create_engine(settings.sql_uri)

def prompt_for_field(field_name: str, old_value: str=None) -> str:
    if old_value is None:
        prompt = f"{field_name}: "
    else:
        prompt = f"{field_name} (currently '{old_value}'): "

    result = ""
    while result == "":
        result = input(prompt)

    return result


def new_category(args: argparse.Namespace):
    name = prompt_for_field("name") if args.name is None else args.name

    with sqlalchemy.orm.Session(engine) as session:
        c = Category(name=name)
        session.add(c)
        session.commit()

        print(f"created category {c.category_id} with name '{name}'")

    
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
    with sqlalchemy.orm.Session(engine) as session:
        category = session.get(Category, args.category_id)
        
        if args.name is None:
            name = prompt_for_field("name", old_value=category.name)
        else:
            name = args.name
            print(f"renaming category {category.category_id} from '{category.name}' to '{name}'")

        category.name = name
        session.commit()


def delete_category(args: argparse.Namespace):
    # TODO: what happens when tasks or projects have this category?
    # TODO: what happens when it's not found?
    with sqlalchemy.orm.Session(engine) as session:
        category = session.get(Category, args.category_id)
        session.delete(category)
        session.commit()

        print(f"deleted category {category.category_id}: '{category.name}'")
