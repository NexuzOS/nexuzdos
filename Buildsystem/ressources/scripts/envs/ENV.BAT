@echo off
echo setting up system to build the MS-DOS 4.01 SOURCE BAK...
set CL=
set LINK=
set MASM=%BAKROOT%\tools
set COUNTRY=usa-ms
set BAKROOT=d:
rem BAKROOT points to the home drive/directory of the sources.


set LIB=%BAKROOT%\tools\bld\lib
set INIT=%BAKROOT%\tools
set INCLUDE=%BAKROOT%\tools\bld\inc
set PATH=%BAKROOT%\TOOLS;%BAKROOT%\TOOLS\BLD;%BAKROOT%\MESSAGES;%BAKROOT%\MAPPER;%BAKROOT%\MEMM;%BAKROOT%\INC;%BAKROOT%\LIB;%BAKROOT%\DOS;%BAKROOT%\DEV;%BAKROOT%\SELECT;%BAKROOT%\BIOS;%BAKROOT%\BOOT;%BAKROOT%\H;CMD;%PATH%
