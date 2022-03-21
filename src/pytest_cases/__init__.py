# Authors: Sylvain MARIE <sylvain.marie@se.com>
#          + All contributors to <https://github.com/smarie/python-pytest-cases>
#
# License: 3-clause BSD, <https://github.com/smarie/python-pytest-cases/blob/master/LICENSE>
from .common_pytest_lazy_values import lazy_value, is_lazy
from .common_others import unfold_expected_err, assert_exception, AUTO

from .fixture_core1_unions import fixture_union, NOT_USED, unpack_fixture, ignore_unused
from .fixture_core2 import pytest_fixture_plus, fixture_plus, fixture, param_fixtures, param_fixture
from .fixture_parametrize_plus import pytest_parametrize_plus, parametrize_plus, parametrize, fixture_ref

from .case_funcs import case, copy_case_info, set_case_id, get_case_id, get_case_marks, \
    get_case_tags, matches_tag_query, is_case_class, is_case_function
from .case_parametrizer_new import parametrize_with_cases, THIS_MODULE, get_all_cases, get_parametrize_args, \
    get_current_case_id, get_current_cases, get_current_params, CasesCollectionWarning

try:
    # -- Distribution mode --
    # import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # -- Source mode --
    # use setuptools_scm to get the current version from src using git
    from setuptools_scm import get_version as _gv
    from os import path as _path
    __version__ = _gv(_path.join(_path.dirname(__file__), _path.pardir, _path.pardir))


AUTO2 = AUTO
"""Deprecated symbol, for retrocompatibility. Will be dropped soon."""


__all__ = [
    '__version__',
    # the submodules
    'case_funcs', 'case_parametrizer_new',
    'common_mini_six', 'common_others', 'common_pytest', 'common_pytest_lazy_values', 'common_pytest_marks',
    'filters',
    'fixture__creation', 'fixture_core1_unions', 'fixture_core2', 'fixture_parametrize_plus',

    # all symbols imported above
    'unfold_expected_err', 'assert_exception',

    # --fixture core1
    'fixture_union', 'NOT_USED', 'unpack_fixture', 'ignore_unused',
    # -- fixture core2
    'pytest_fixture_plus', 'fixture_plus', 'fixture', 'param_fixtures', 'param_fixture',
    # -- fixture parametrize plus
    'pytest_parametrize_plus', 'parametrize_plus', 'parametrize', 'fixture_ref', 'lazy_value', 'is_lazy',

    # V2 symbols
    'AUTO', 'AUTO2',
    # case functions
    'case', 'copy_case_info', 'set_case_id', 'get_case_id', 'get_case_marks',
    'get_case_tags', 'matches_tag_query', 'is_case_class', 'is_case_function',
    # test functions
    'get_all_cases', 'parametrize_with_cases', 'THIS_MODULE', 'get_parametrize_args', 'get_current_case_id',
    'get_current_cases', 'get_current_params', 'CasesCollectionWarning'
]
