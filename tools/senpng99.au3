;RequireAdmin
WinActive("��");

ControlFocus("��","","Edit1")

WinWait("��","[CLASS:#32770]",10)

ControlSetText("��","","Edit1","D:\123456.png")

Sleep(2000)

ControlClick("��", "","Button1");