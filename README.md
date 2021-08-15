# Python unit testing: How to monkeypatch and mock methods

Tutorial based on this blog post [https://alexmarandon.com/articles/python_mock_gotchas/](https://alexmarandon.com/articles/python_mock_gotchas/)

## Problem statement
Monkeypatching and mocking can be somewhat confusing in python. There is a lack of clear documentation on the topic.

The tests provided should give a complete view of what can and cannot be done.

## How to run the tests.
Setup the environmnet
```
python3 -m venv .venv
```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
```

How to run the tests e.g
```
pytest test_method_call.py
```
