""""""
import Click
from clients import commands as clients_commands

@click.group()
@click.pass_context
def cli():
    ctx.obj = {}


cli.add_command(clients_commands.all)