import pastebinapi
   
username = "<Your Username>"
password = "<Your Passwword>"
api_key = "<Your API Key>"
pastebinapi.check(username, password, api_key)

content = "text"
privacity = "1" # 0 = public / 1 = unlisted
title = "text 1"
pastebinapi.paste(username, password, api_key, privacity, title, content)