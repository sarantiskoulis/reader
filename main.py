from Config import Config
from FileManager import FileManager
import click
import os
import subprocess
import yaml

@click.command()
@click.option('--yamlfile')
@click.option('--writeto')
@click.option('--delete')

def _cli_outputs(yamlfile, writeto, delete):
    if delete:
        os.remove(delete)
    else:
        FileManager(yamlfile, writeto)



if __name__ == '__main__':
    _cli_outputs()

