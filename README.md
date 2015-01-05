ts3versions
===========

This little tool generates a JSON-Object listing all available versions for the TeamSpeak3-Server.

Usage:
------
Simply add a cronjob like this:
```
@daily www-data /path/to/ts3versions.py >/path/to/webroot/ts3versions.json
```
