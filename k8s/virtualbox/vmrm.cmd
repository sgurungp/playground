@ECHO OFF
SET PATH=%PATH%;c:\Program Files\Oracle\VirtualBox;

SET /P VM="Enter a name for your VM, e.g. 'node34': "
ECHO "About to DESTROY %VM%"
PAUSE

REM Triggering an ACPI shutdown is the "clean" way to get the guest OS
REM to shutdown, but since we are deleting the VM anyway, a hard
REM "poweroff" instead of an "acpipowerbutton" is acceptable.
VBoxManage controlvm %VM% poweroff
VBoxManage unregistervm %VM% --delete
