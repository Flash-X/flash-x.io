#!/usr/bin/env python3

import click
import os

@click.command(name='bibtex2yaml')
@click.argument('bibtex-file', required=True)
@click.argument('yaml-file', required=True)
def bibtex2yaml(bibtex_file,yaml_file):
    """
    Conver BibTex to Yaml
    """
    os.system('./bibtex2bibjson.py {0} > {1}.json'.format(bibtex_file,yaml_file))
    os.system('cat {0}.json | ./json2yaml.py | tee {0}'.format(yaml_file))
    os.system('rm {0}.json'.format(yaml_file))


if __name__ == "__main__":
    bibtex2yaml()
