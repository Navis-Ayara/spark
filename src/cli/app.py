from .helpers import (create_spark, get_sparks, get_sparks_by_context,
                      edit_spark, delete_spark)
import click

import os

@click.group()
def cli():
    pass

@cli.command("add")
@click.argument("content")
def add_spark(content):
    current_directory = os.getcwd()

    create_spark(content, current_directory)

    click.echo(f"Spark added to '{current_directory}'")

@cli.command("list")
@click.option("--all", is_flag=True)
def list_sparks(all):
    if all:
        for spark in get_sparks():
            click.echo(f"{spark.id} | {spark.content} | {spark.context}")
    
    else:
        current_directory = os.getcwd()
        for spark in get_sparks_by_context(current_directory):
            click.echo(f"{spark.id} | {spark.content} | {spark.context}")

@cli.command("edit")
@click.argument("id")
@click.argument("content")
def edit(id, content):
    data = edit_spark(id, content)

    if data:
        pass
    else:
        click.echo("Spark not found!")

@cli.command("delete")
@click.argument("id")
def delete(id):
    data = delete_spark(id)

    if data:
        pass
    else:
        click.echo("Spark not found!")
