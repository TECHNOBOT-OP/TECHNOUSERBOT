from .extdl import *
from .paste import *

type = True
check = 0
while type:
    try:
        from . import format as _format
        from . import tools as _technotools
        from . import utils as _technoutils
        from .events import *
        from .format import *
        from .tools import *
        from .utils import *

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
