from Config import Config
from FileManager import FileManager
import click
import os

@click.command()
@click.option('--yaml')
@click.option('--writeto')
@click.option('--delete')

def _cli_outputs(yaml, writeto, delete):
    if delete:
        os.remove(delete)
    else:
        FileManager(yaml, writeto)



if __name__ == '__main__':
    _cli_outputs()

