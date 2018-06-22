;RequireAdmin
WinActive("打开");

ControlFocus("打开","","Edit1")

WinWait("打开","[CLASS:#32770]",10)

ControlSetText("打开","","Edit1","D:\123456.png")

Sleep(2000)

ControlClick("打开", "","Button1");