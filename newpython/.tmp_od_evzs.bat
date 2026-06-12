@ECHO OFF
@SET PYTHONIOENCODING=utf-8
@SET PYTHONUTF8=1
@FOR /F "tokens=2 delims=:." %%A in ('chcp') do for %%B in (%%A) do set "_CONDA_OLD_CHCP=%%B"
@chcp 65001 > NUL
@CALL "C:\Users\91951\anaconda3\condabin\conda.bat" activate "c:\Users\91951\OneDrive\Desktop\pythonProject\leetcode\python\newpython"
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@c:\Users\91951\OneDrive\Desktop\pythonProject\leetcode\python\newpython\python.exe -Wi -m compileall -q -l -i C:\Users\91951\AppData\Local\Temp\tmp_tqwcz0m -j 0
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@chcp %_CONDA_OLD_CHCP%>NUL
