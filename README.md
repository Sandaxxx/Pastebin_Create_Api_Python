# The Tool its for create pastebin, logging account and read content pastebin link.

![background](https://cdn.discordapp.com/attachments/1026388619126124554/1055780727247085588/image.png)

# INSTALLATION 
#> ```pip install pastebinapi```


```py
# EXEMPLE PASTEBIN API 

import pastebinapi
   
username = "<Your Username>"
password = "<Your Passwword>"
api_key = "<Your API Key>"
pastebinapi.check(username, password, api_key)

content = "text"
privacity = "1" # 0 = public / 1 = unlisted
title = "text 1"
pastebinapi.paste(username, password, api_key, privacity, title, content)

```
