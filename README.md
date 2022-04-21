# blink-detection-test

## Build opencv for GStreamer usage:
https://developer.ridgerun.com/wiki/index.php?title=Compiling_OpenCV_from_Source

`export PYTHONPATH=/usr/lib/python3/dist-packages/:$PYTHONPATH`

## Sources

`BlinkDetection.py` -- получения изображения с CSI-камеры. Детекция лица и моргания на нем. ML без GPU  
`display_nano.py` -- вывод изображения на I2C OLED дисплей
