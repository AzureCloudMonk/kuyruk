import os
import sys
import logging
import importlib
from collections import namedtuple
from contextlib import contextmanager

logger = logging.getLogger(__name__)


def import_task(module_name, class_name, function_name, path=None):
    """Find and return the function for given function name."""
    namespace = import_task_module(module_name, path)
    if class_name:
        cls = getattr(namespace, class_name)
        namespace = cls
    else:
        cls = None

    task = getattr(namespace, function_name)
    ImportResult = namedtuple('ImportResult', ['task', 'cls'])
    return ImportResult(task=task, cls=cls)


def import_task_module(module_name, path=None):
    """Import module by searching main module, current working directory and
    python path.

    """
    logger.debug("Importing module %r" % module_name)
    main_module, main_module_name = get_main_module()
    if module_name == main_module_name:
        return main_module

    if path is None:
        path = os.getcwd()

    with custom_path(path):
        return importlib.import_module(module_name)


@contextmanager
def custom_path(path):
    if path in sys.path:
        yield
    else:
        sys.path.insert(0, path)
        try:
            yield
        finally:
            sys.path.remove(path)


def get_main_module():
    """:return main module and module name pair"""
    main_module = sys.modules['__main__']
    if not hasattr(main_module, '__file__'):
        # if run from interactive shell
        return None, None
    filename = os.path.basename(main_module.__file__)
    module_name, ext = os.path.splitext(filename)
    MainModule = namedtuple('MainModule', ['module', 'name'])
    return MainModule(module=main_module, name=module_name)
