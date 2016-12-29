from intel import util
import os
import subprocess


# Returns the absolute path to the top-level kcm script.
def kcm():
    return os.path.join(util.kcm_root(), "kcm.py")


# Returns the absolute path to the test config directory with the supplied
# name.
def conf_dir(name):
    return os.path.join(util.kcm_root(), "tests", "data", "config", name)


# Returns resulting stdout buffer from interpreting the supplied command with
# a shell. Raises process errors if the command exits nonzero.
def execute(cmd, args):
    cmd_str = "{} {}".format(cmd, " ".join(args))
    stdout = subprocess.check_output(cmd_str, shell=True)
    return stdout