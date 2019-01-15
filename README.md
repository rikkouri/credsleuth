# Credential Sleuth
[![PyPI version](https://badge.fury.io/py/credsleuth.svg)](https://badge.fury.io/py/credsleuth)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Generic badge](https://img.shields.io/badge/version-0.0.1_(use_at_risk)-red.svg)](https://shields.io/)

A rule driven library for detecting secrets and credentials within files and strings.

## Installation
```bash
pip install --user credsleuth
```


## Simple Usage
### Finding secrets in a string:
```python
import credsleuth

data = """
Hello, world
Password=123
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
Goodbye
"""
print(credsleuth.check_string(data))
```


### Finding secrets in a file:
```python
import credsleuth

print(credsleuth.check_file("filename.txt"))
```

### Command line usage
```bash
credsleuth filename.txt
```

## Advanced Usage

### Customizing configuration
```python
import credsleuth

config = credsleuth.ConfigEngine()
config.verbose = True
config.rules_file = 'custom_rules.json'

credsleuth.check_file('filename.txt', config)
```

## Writing Rules
See `rules.json` for an example in extending rules definitions. 

## Todo
- Improve basic ruleset to be less noisy.
- Probably add some comments to codebase
- Add pretty output options for command line execution.
- Write a proper read me.
- Build model to detect credentials based upon entropy
- Search multiple files from CLI - Done
- Write some proper examples
