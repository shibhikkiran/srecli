# -*- config: utf-8 -*-

from click.testing import CliRunner
from srecli.cli import cli

def test_status_show():
    runner = CliRunner()
    result = runner.invoke(cli, ['status', 'show'])
    assert result.exit_code == 0
    assert 'echo msg' in result.output
    assert 'Hello' in result.output

def test_status_show_with_debug():
    runner = CliRunner()
    result = runner.invoke(cli, ['status', 'show', '--debug'])
    assert result.exit_code == 0
    assert 'echo msg' in result.output
    assert 'Hello' in result.output


def test_status_show_with_echo_msg():
    runner = CliRunner()
    result = runner.invoke(cli, ['status', 'show', '--echo-msg', 'World'])
    assert result.exit_code == 0
    assert 'echo msg' in result.output
    assert 'World' in result.output

def test_status_show_with_echo_msg_and_debug():
    runner = CliRunner()
    result = runner.invoke(cli, ['status', 'show', '--echo-msg', 'World', '--debug'])
    assert result.exit_code == 0
    assert 'echo msg' in result.output
    assert 'World' in result.output


