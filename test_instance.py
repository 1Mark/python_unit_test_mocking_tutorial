from unittest.mock import patch
from person import Person
import pytest

@pytest.mark.xfail
@patch('person.Pet')
def test_dog_noise_failure_to_mock(mock_pet):
    """Trying to patch the instance
    We cannot do this. Since the class definition of `person.Pet` was defined
    at import time, any modifications to it will not reflect on class instances."""
    mock_pet.noise.return_value = "Meoow"
    person = Person()
    assert person.pet.noise() == "Meoow"

def test_dog_noise_with_patch_context_manager():
    """We patch the module.
    To get the instance we must call `mock_pet.return_value`.
    ---------> This is why they came up with patch.object
    """
    with patch('person.Pet') as mock_pet:
        # If `person` is defined outside the context manager this wont work.
        person = Person()
        mock_pet.return_value.noise.return_value = "Meoow"
        assert person.pet.noise() == "Meoow"

@patch('person.Pet')
def test_dog_noise_with_patch_decorator(mock_pet):
    """We patch the module.
    To get the instance we must call `mock_pet.return_value`.
    ---------> This is why they came up with patch.object
    """
    person = Person()
    mock_pet.return_value.noise.return_value = "Meoow"
    assert person.pet.noise() == "Meoow"

def test_dog_noise_with_patch_object_context_manager():
    """We patch the instance."""
    person = Person()
    with patch.object(person.pet, "noise", return_value="Meoow"):
        assert person.pet.noise() == "Meoow"

def test_dog_noise_with_monkeypatch(monkeypatch):
    """We patch the instance."""
    person = Person()
    monkeypatch.setattr(person.pet, "noise", lambda: "Meoow")
    assert person.pet.noise() == "Meoow"