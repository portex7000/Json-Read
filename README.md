# [JsonRead](https://portex7000.github.io/Json-Read/)
A python executable app, that can read json files directly from the command prompt

# How to use
## Windows
1. Download the latest windows version of `JsonRead.exe`
2. Open cmd (or put in your batch file): `C:\Path\To\JsonRead.exe (the path to the exe) "C:\Path\To\The\JsonFile.json" "WhatToReadInTheJsonFile" (uses python syntax)`
3. You get the output
4. To put output into variable (modify the command first too), execute `for /f "tokens=*" %%A in ('C:\Path\To\JsonRead.exe "C:\Path\To\The\JsonFile.json" "WhatToReadInTheJsonFile"') do set VAR=%%A`

## Linux
1. Download the latest linux version of `JsonRead`
2. Open terminal (or put in your bash file): `/Path/To/JsonRead (the path to JsonRead) "/Path/To/The/JsonFile.json" "WhatToReadInTheJsonFile" (uses python syntax)`
3. You get the output
4. To put output into variable (modify the command first too), execute `VARIABLE=$(/Path/To/JsonRead (the path to JsonRead) "/Path/To/The/JsonFile.json" "WhatToReadInTheJsonFile" (uses python syntax))`
