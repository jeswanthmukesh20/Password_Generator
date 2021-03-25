# Password Generator


## Return password with the default random length 4 < length < 23

```python
password = Password()
```
## Print the information about the generated password

```python
password = Password(print_info=True)
```
## Print and return password with the default random length
```python
password = Password(default=True, print_info=True)
```

## Specify the length of the password
```python
password = Password(Lenght=23, print_info=True)
```

## Asks for length if the given length is greater than 23 or lesser than 4

```python
password = Password(Lenght=100, print_info=True)
```
## Output:
``` bash
user@user:~/Path_to_the_script$ python password.py

[*]Enter The Length of the Password:
```