@echo off
echo setting up system to build the MS-DOS 4.01 SOURCE BAK...
set CL=
set LINK=
set MASM=
set COUNTRY=usa-ms
set BAKROOT=d:
rem BAKROOT points to the home drive/directory of the sources.


set LIB=%BAKROOT%\src\tools\bld\lib
set INIT=%BAKROOT%\src\tools
set INCLUDE=%BAKROOT%\src\tools\bld\inc
set PATH=%BAKROOT%\src\tools;%BAKROOT%\src\tools\bld;%BAKROOT%\src\messages;%BAKROOT%\src\mapper;%BAKROOT%\src\memm;%BAKROOT%\src\inc;%BAKROOT%\src\lib;%BAKROOT%\src\dos;%BAKROOT%\src\dev;%BAKROOT%\src\select;%BAKROOT%\src\bios;%BAKROOT%\src\boot;%BAKROOT%\src\h;%BAKROOT%\src\cmd;%PATH%
