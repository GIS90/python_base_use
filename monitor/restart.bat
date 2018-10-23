taskkill /f  /im  fcdb_.exe
start /b "" "C:\Program Files\TSNav\fcdb_.exe"
taskkill /f  /im  monitor.py
start /b python monitor.py monitor.ini