import os
import sys
import click

@click.command(name='bibtex2yaml')
@click.argument('bibtex-file', required=True)
@click.argument('yaml-file', required=True)
def bibtex2yaml(bibtex_file,yaml_file):
    """
    Conver BibTex to Yaml
    """
    os.system('{0} bibtex2bibjson.py {1} > {2}.json'.format(sys.executable, bibtex_file,yaml_file))
    os.system('cat {0}.json | {1} json2yaml.py | tee {0}'.format(yaml_file, sys.executable))
    os.system('rm {0}.json'.format(yaml_file))


if __name__ == "__main__":
    bibtex2yaml()
