""" """
import Click

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass

@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """creates a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """updates a client"""
    pass


@clients.command()
@click.pass_context
def detele(ctx, client_uid):
    """Deletes a client"""
    pass


"""Create alias"""

all = clients