@ECHO OFF
REM ==========================================================================
REM CLI script to create a NAT Network in VirtualBox
REM ==========================================================================

SET PATH=%PATH%;c:\Program Files\Oracle\VirtualBox;
SET NETWORKNAME=cloudnet01
SET NETWORKSUBNET=10.1.1.0/24

REM Create a private network, with a subnet allocated and DHCP enabled.
REM Later on, VMs that you create can be attached to this network and speak directly 
REM to other VMs on the network and be NATted by VirtualBox to the outside world.
VBoxManage natnetwork add --netname %NETWORKNAME% --network %NETWORKSUBNET% --enable --dhcp on --ipv6 off
