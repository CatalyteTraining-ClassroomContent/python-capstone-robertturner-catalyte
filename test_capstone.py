import pytest
from capstone import filter_by_date, filter_by_student_id, find_unsubmitted, get_average_score, get_average_score_by_module
from sample_data import submissions



def test_filter_by_date():
    assert len(filter_by_date("2025-09-11", submissions)) == 2


def test_filter_by_student_id():
    result = filter_by_student_id(1, submissions)
    assert len(result) == 3

def test_find_unsubmitted():
    assert find_unsubmitted("2025-09-12",["Blake Kim", "Kim Jake"], submissions) == ["Kim Jake"]

from capstone import get_average_score

def test_get_average_score_multiple_submissions():
    result = get_average_score(submissions)
    assert result == 81.5

def test_get_average_score_empty_list():
    assert get_average_score([]) == 0.0

def test_get_average_score_by_module_empty_list():
    assert get_average_score_by_module([]) == {}

def test_get_average_score_by_module_normal_case():
    result = get_average_score_by_module(submissions)
    expected = {"Algebra": 78.8, "Statistics": 81.0, "History": 85.7}
    assert result == expected
    assert result == pytest.approx(expected)

    
