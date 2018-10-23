# Credential Sleuth
A rule driven library for detecting secrets and credentials within files and strings.

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

## Installation
`pip install --user credsleuth`

## Writing Rules
See `rules.json` for an example in extending rules definitions. 

## Todo
- Add some comments to codebase
- Add pretty output options for command line execution.
- Write a proper read me.
- Build model to detect credentials based upon entropy
- Search multiple files