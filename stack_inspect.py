# stack_inspect.py
import gdb

class StackInspect(gdb.Command):
    """Inspect the current stack"""

    def __init__(self):
        super(StackInspect, self).__init__("stack-inspect", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        frame = gdb.newest_frame()
        while frame:
            print("Frame: %s" % frame.name())
            frame = frame.older()

StackInspect()

