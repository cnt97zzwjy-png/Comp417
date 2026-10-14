#!/bin/bash
# Sets up a virtual Linux desktop you can see in the browser (port 6080)
sudo apt-get update
sudo apt-get install -y xvfb x11vnc fluxbox novnc websockify \
  libxcb-cursor0 libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
  libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 \
  libegl1 libgl1 libfontconfig1 libdbus-1-3
pip install PySide6
Xvfb :1 -screen 0 1280x800x24 >/dev/null 2>&1 &
sleep 2
fluxbox -display :1 >/dev/null 2>&1 &
x11vnc -display :1 -nopw -forever -shared -rfbport 5900 -bg -quiet
websockify --web /usr/share/novnc 6080 localhost:5900 >/dev/null 2>&1 &
sleep 1
echo ""
echo "DONE. Open the PORTS tab -> port 6080 -> open in browser -> vnc.html -> Connect"
echo "Then run:  DISPLAY=:1 python submit_request.py   (Question 2.2)"
echo "      or:  DISPLAY=:1 python layout_form.py      (Question 2.1)"
