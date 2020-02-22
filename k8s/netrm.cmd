@ECHO OFF
REM ==========================================================================
REM CLI script to remove a NAT network from VirtualBox
REM ==========================================================================

SET PATH=%PATH%;c:\Program Files\Oracle\VirtualBox;
SET NETWORKNAME=cloudnet01

REM Switch off DHCP, then stop the network and delete it
ECHO %NETWORKNAME% will be REMOVED!
PAUSE

VBoxManage natnetwork modify --netname %NETWORKNAME% --dhcp off
VBoxManage natnetwork stop --netname %NETWORKNAME%
VBoxManage natnetwork remove --netname %NETWORKNAME%
