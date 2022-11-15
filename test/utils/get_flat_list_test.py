from typing import List

import pytest

from src.utils import get_unique_sorted_values_from_list


def test_flat_simple_list_of_strings_items1():
    # arrange
    initial_list = [
        'Luna Wedler, Jannis Niewöhner, Milan Peschel, Edin Hasanović']
    # action
    actual = get_unique_sorted_values_from_list(initial_list)
    # assert
    expected = ['Edin Hasanović', 'Jannis Niewöhner',
                'Luna Wedler', 'Milan Peschel']
    assert expected == actual


def test_flat_simple_list_of_strings_items2():
    # arrange
    initial_list = [
        'Luna Wedler, Jannis Niewöhner, Milan Peschel, Edin Hasanović', 'Edin Hasanović']
    # action
    actual = get_unique_sorted_values_from_list(initial_list)
    # assert
    expected = ['Edin Hasanović', 'Jannis Niewöhner',
                'Luna Wedler', 'Milan Peschel']
    assert expected == actual


def test_flat_simple_list_of_strings_items3():
    # arrange
    initial_list = ['Luna Wedler',
                    'Jannis Niewöhner, Milan Peschel, Edin Hasanović']
    # action
    actual = get_unique_sorted_values_from_list(initial_list)
    # assert
    expected = ['Edin Hasanović', 'Jannis Niewöhner',
                'Luna Wedler', 'Milan Peschel']
    assert expected == actual


def test_flat_simple_list_of_strings_items4():
    # arrange
    initial_list = ['Luna Wedler',
                    'Jannis Niewöhner', 'Milan Peschel, Edin Hasanović']
    # action
    actual = get_unique_sorted_values_from_list(initial_list)
    # assert
    expected = ['Edin Hasanović', 'Jannis Niewöhner',
                'Luna Wedler', 'Milan Peschel']
    assert expected == actual


def test_flat_simple_list_of_strings_items4():
    # arrange
    initial_list = ['Luna Wedler',
                    'Milan Peschel',
                    'Jannis Niewöhner',
                    'Edin Hasanović']
    # action
    actual = get_unique_sorted_values_from_list(initial_list)
    # assert
    expected = ['Edin Hasanović', 'Jannis Niewöhner',
                'Luna Wedler', 'Milan Peschel']
    assert expected == actual


@pytest.mark.parametrize("initial_list,expected",
                         [
                             (['Luna Wedler, Milan Peschel',
                               'Jannis Niewöhner', 'Edin Hasanović'],
                                 ['Edin Hasanović', 'Jannis Niewöhner',
                                  'Luna Wedler', 'Milan Peschel']),
                             (['Luna Wedler, Milan Peschel, Jannis Niewöhner, Edin Hasanović'],
                                 ['Edin Hasanović', 'Jannis Niewöhner',
                                  'Luna Wedler', 'Milan Peschel'])])
def test_flat_simple_list_of_strings_items5(initial_list: List, expected: List):
    # arrange
    initial_list = ['Luna Wedler',
                    'Milan Peschel',
                    'Jannis Niewöhner',
                    'Edin Hasanović']
    # action
    actual = get_unique_sorted_values_from_list(initial_list)
    # assert
    expected = ['Edin Hasanović', 'Jannis Niewöhner',
                'Luna Wedler', 'Milan Peschel']
    assert expected == actual
