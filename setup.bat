@echo off
echo ========================================================
echo Instalando Dependencias de Sistema (Metrology Assistant)
echo ========================================================
echo.
echo Instalando MiKTeX (Compilador LaTeX)...
winget install -e --id MiKTeX.MiKTeX --accept-source-agreements --accept-package-agreements

echo.
echo Instalando Python 3.11...
winget install -e --id Python.Python.3.11 --accept-source-agreements --accept-package-agreements

echo.
echo Instalando Git...
winget install -e --id Git.Git --accept-source-agreements --accept-package-agreements

echo.
echo ========================================================
echo Instalando Dependencias de Python (Pip)
echo ========================================================
pip install -r requirements.txt

echo.
echo ========================================================
echo Instalacion completada con exito.
echo ========================================================
pause
