from person import Person
from unittest.mock import patch
import pytest

@pytest.mark.xfail(strict=True)
def test_name_with_patch_context_manager_failure():
    """We are patching the method within the module.
    But this isn't exactly what's used by Person.
    Since person.py had `from data_source import get_name`
    if person.py had `import data_source` instead, this test would pass.
    """
    the_person = Person()
    with patch("data_source.get_name", return_value="Bob"):
        name = the_person.name()
    assert name == "Bob"

def test_name_with_patch_context_manager():
    """We are patching the method within the module"""
    the_person = Person()
    with patch("person.get_name", return_value="Bob"):
        name = the_person.name()
    assert name == "Bob"

@patch("person.get_name")
def test_name_with_patch_decorator(mock_get_name):
    """We are patching the method within the module"""
    mock_get_name.return_value="Bob"
    the_person = Person()
    assert the_person.name() == "Bob"

def test_name_with_patch_object_context_manager():
    """We are patching the instance we created."""
    the_person = Person()
    with patch.object(the_person, "name", return_value="Bob"):
        name = the_person.name()
    assert name == "Bob"

def test_name_with_monkeypatch(monkeypatch):
    """We are patching the instance we created."""
    the_person = Person()
    monkeypatch.setattr(the_person, "name", lambda: "Bob")
    assert the_person.name() == "Bob"