from Config import Config
from FileManager import FileManager
import click

@click.command()
@click.option('--yaml')
@click.option('--writeto')

def _cli_outputs(yaml,writeto):
    return [yaml, writeto]

if __name__ == '__main__':
    FileManager(_cli_outputs()[0], _cli_outputs()[1])