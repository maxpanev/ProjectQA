from crs.cli_util import CommandLineUtility

class TestCommandLineUtility:
    def test_command_only(self):
        cli = CommandLineUtility(['mycommand'])
        assert cli.get_command() == 'mycommand'
        assert cli.get_options() == {}

    def test_short_option_without_value(self):
        cli = CommandLineUtility(['mycommand', '-o'])
        assert cli.get_command() == 'mycommand'
        assert cli.get_options() == {'o': True}

    def test_short_option_with_value(self):
        cli = CommandLineUtility(['mycommand', '-o', 'value'])
        assert cli.get_command() == 'mycommand'
        assert cli.get_options() == {'o': 'value'}

    def test_long_option_without_value(self):
        cli = CommandLineUtility(['mycommand', '--option'])
        assert cli.get_command() == 'mycommand'
        assert cli.get_options() == {'option': True}

    def test_long_option_with_value(self):
        cli = CommandLineUtility(['mycommand', '--option', 'value'])
        assert cli.get_command() == 'mycommand'
        assert cli.get_options() == {'option':'value'}

    def test_mixed_options(self):
        cli = CommandLineUtility(['mycommand', '-o', 'value', '--flag'])
        assert cli.get_command() == 'mycommand'
        assert cli.get_options() == {'o': 'value', 'flag': True}

