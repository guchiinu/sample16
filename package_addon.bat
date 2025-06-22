@echo off
setlocal
set ADDON_NAME=blender_version_panel
set PACKAGE_FILE=%ADDON_NAME%.zip

echo Preparing add-on package...

if exist %PACKAGE_FILE% del /Q %PACKAGE_FILE%
if exist %ADDON_NAME% rmdir /S /Q %ADDON_NAME%
mkdir %ADDON_NAME%

copy /Y blender_version_panel.py %ADDON_NAME%\__init__.py >nul

powershell -NoLogo -NoProfile -Command "Compress-Archive -Path %ADDON_NAME%\* -DestinationPath %PACKAGE_FILE% -Force"

rmdir /S /Q %ADDON_NAME%

echo Package created: %PACKAGE_FILE%
endlocal
