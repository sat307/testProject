import pytest
import sys
sys.path.append('..')

from expiringDict import ExpiringDict

try:
    from collections import OrderedDict
except ImportError:
    # Python < 2.7
    from ordereddict import OrderedDict


def test_expiring_dict_copy_from_dict():
    dict_test = dict()
    dict_test['test'] = 1
    exp_dict_test = ExpiringDict(max_len=200000, max_age_seconds=1800, items=dict_test)
    assert 1 == exp_dict_test['test']


def test_expiring_dict_copy_from_expiring_dict_original_timeout_and_length():
    exp_dict_test = ExpiringDict(max_len=200000, max_age_seconds=1800)
    exp_dict_test['test'] = 1
    exp_dict_test2 = ExpiringDict(max_len=None, max_age_seconds=None, items=exp_dict_test)
    assert 1 == exp_dict_test2['test']
    assert 200000 ==  exp_dict_test2.max_len
    assert 1800 == exp_dict_test2.max_age


def test_expiring_dict_copy_from_expiring_dict_new_timeout_and_length():
    exp_dict_test = ExpiringDict(max_len=200000, max_age_seconds=1800)
    exp_dict_test['test'] = 1
    exp_dict_test2 = ExpiringDict(max_len=100000, max_age_seconds=900, items=exp_dict_test)
    assert 1 == exp_dict_test2['test']
    assert 100000 == exp_dict_test2.max_len
    assert 900 ==  exp_dict_test2.max_age
