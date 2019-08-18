# Configuration files in Python

Most applications need some configuration parameters. There is different ways to store and use configuration data in software. It is recommended to separate the code an logic modules from the configuration data. This way users will be able to modify or update configuration parameters with no need to modify the application. A simple way to store configuration info is a file with an easy structure that the user can manage. We can take advantage of the package "configparser" in python to read a config file. This is simple cheatsheet to give an example of use.


### 1. Install the required module "configparser"

pip install configparser

### 2. Define the config file. You can get more info about the config INI file structure in the python documentation. Here an example:

[GLOBAL] <br>
unsername = user <br>
password = pass <br>
prn = 124

[PRN120] <br>
ip = 192.168.1.120 <br>
port = 1237

[PRN124] <br>
ip = 192.168.1.124 <br>
port = port = 1238

[PRN126] <br>
ip = 192.168.1.126 <br>
port = port = 1239


### 3. Example of use for the python module "configparser"

```python
import configparser

congif_file = "config.ini"
config = configparser.ConfigParser()
config.read(config_file)

username = config['GLOBAL']['username']
password = config['GLOBAL']['password']
prn = config['GLOBAL']['prn']
ip = config['PRN%s' % prn]['ip']
port = int(config['PRN%s' % prn]['port'])
```

### 4. Thanks !

I hope you find this info useful. <br>

Enjoy !
