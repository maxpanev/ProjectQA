class CommandLineUtility:
    def __init__(self, args):
        self.command = args[0]
        self.options = {}
        self.parse_args(args[1:])

    def parse_args(self, args):
        i = 0
        while i < len(args):
            arg = args[i]

            if arg.startswith('--'):
                option = arg[2:]
            elif arg.startswith('-'):
                option = arg[1:]
            else:
                i += 1
                continue

            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                self.options[option] = args[i + 1]
                i += 1
            else:
                self.options[option] = True

            i += 1

    def get_command(self):
        return self.command

    def get_options(self):
        return self.options