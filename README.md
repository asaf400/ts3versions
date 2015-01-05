ts3versions
===========

This little tool generates a JSON-Object listing all available versions for the TeamSpeak3-Server.

Usage:
------

Simply add a cronjob like this:
```
@daily www-data /path/to/ts3versions.py >/path/to/webroot/ts3versions.json
```

Example-Output:
---------------
```json
{
  "latest": "3.0.11.2", 
  "versions": [
    "3.0.0", 
    "3.0.1", 
    "3.0.2", 
    "3.0.3", 
    "3.0.5", 
    "3.0.6", 
    "3.0.6.1", 
    "3.0.7", 
    "3.0.7.1", 
    "3.0.7.2", 
    "3.0.8", 
    "3.0.9", 
    "3.0.10", 
    "3.0.10.1", 
    "3.0.10.2", 
    "3.0.10.3", 
    "3.0.11", 
    "3.0.11.1", 
    "3.0.11.2"
  ]
}
```
