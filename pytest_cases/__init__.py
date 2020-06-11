from .fixture_core1_unions import fixture_union, NOT_USED, unpack_fixture, ignore_unused
from .fixture_core2 import pytest_fixture_plus, fixture_plus, param_fixtures, param_fixture
from .fixture_parametrize_plus import pytest_parametrize_plus, parametrize_plus, fixture_ref, lazy_value

from .case_funcs import case_name, test_target, case_tags, cases_generator
from .case_parametrizer import cases_data, CaseDataGetter, unfold_expected_err, get_all_cases, THIS_MODULE, \
    get_pytest_parametrize_args, cases_fixture


try:
    # -- Distribution mode --
    # import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # -- Source mode --
    # use setuptools_scm to get the current version from src using git
    from setuptools_scm import get_version as _gv
    from os import path as _path
    __version__ = _gv(_path.join(_path.dirname(__file__), _path.pardir))

__all__ = [
    '__version__',
    # the submodules
    'case_funcs', 'case_parametrizer', 'fixture_core1_unions', 'fixture_core2', 'fixture_parametrize_plus',
    # all symbols imported above
    # --cases_funcs
    'lazy_value',
    'case_name',  'test_target', 'case_tags', 'cases_generator',
    # --main_fixtures
    'cases_fixture', 'pytest_fixture_plus', 'fixture_plus', 'param_fixtures', 'param_fixture', 'ignore_unused',
    'fixture_union', 'NOT_USED', 'pytest_parametrize_plus', 'parametrize_plus', 'fixture_ref', 'unpack_fixture',
    # --main params
    'cases_data', 'CaseDataGetter', 'THIS_MODULE', 'unfold_expected_err', 'get_all_cases',
    'get_pytest_parametrize_args',
]

try:  # python 3.5+ type hints
    from pytest_cases.case_funcs import CaseData, Given, ExpectedNormal, ExpectedError, MultipleStepsCaseData
    __all__ += ['CaseData', 'Given', 'ExpectedNormal', 'ExpectedError', 'MultipleStepsCaseData']
except ImportError:
    pass
