import time

import autoit

# without using Script
autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
autoit.control_send("[CLASS:Notepad]", "Edit1", "Hello world..!")
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("[CLASS:#32770]", "Button2")

#With Script
time.sleep(3)
autoit.run("notepad.exe")
autoit.run("E://Software/Pyhton-Sel/Note.exe") #Script
time.sleep(3)
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("[CLASS:#32770]", "Button2")

