# stup import hooks
import xonsh.imphooks
from xonsh.built_ins import XSH
from xonsh.execer import Execer

XSH.load(execer=Execer())
execer = XSH.execer
xonsh.imphooks.install_import_hooks(execer=execer)

__version__ = '0.5.1'

del xonsh
