#!/usr/bin/env python3
import click


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()
def sync():
    click.echo('Synching')


@cli.command()
@click.argument('arg', type=click.Choice['1', '2', '3'])
def sub(arg):
    click.echo('Sub command, %s' % arg)


if __name__ == '__main__':
    cli()
# vim: ts=4 sw=4 sts=4 expandtab
