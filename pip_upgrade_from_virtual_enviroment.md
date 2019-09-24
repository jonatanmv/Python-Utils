# pip... upgrade all
To upgrade all current packages on a virtual enviroment...

Save all packages to file:

```console
$ pip freeze > requirements.txt
```

Upgrade the packages from file:

```console
$ pip install -r requirements.txt --upgrade
```


