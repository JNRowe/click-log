# -*- coding: utf-8 -*-
# flake8: noqa

import click

__version__ = '0.1.1'


if not hasattr(click, 'get_current_context'):
    raise RuntimeError('You need Click 5.0.')

from .core import (
    ClickStream,
    ColorFormatter,
    get_level,
    init,
    set_level,
)

from .options import simple_verbosity_option
