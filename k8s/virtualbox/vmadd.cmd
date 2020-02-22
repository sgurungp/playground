@ECHO OFF
REM ==========================================================================
REM CLI script to boot up a VM and automatically install the guest OS (CentOS).
REM ==========================================================================

SET PATH=%PATH%;c:\Program Files\Oracle\VirtualBox;
SET USERID=sg
SET NETWORKNAME="cloudnet01"

REM Virtualbox 5.2+ supports unattended installs of the guest OS.  We exploit
REM this and the RedHat Kickstart mechanism, in particular using former
REM to boot a hands-free installer and the latter to supply a richer set of
REM installation capabilities than would otherwise be available natively in
REM VirtualBox. 

SET ISO="C:\Users\%USERID%\VirtualBox\ISOs\CentOS-7-x86_64-Minimal-1908.iso"
SET KS="C:\Users\%USERID%\Documents\kickstart.vbox.cfg"

SET VM=mynode.k8s
SET /P VM="Enter a name for your VM, e.g. 'node34': "

REM Create disk, 8Gb
SET VDI="C:\Users\%USERID%\VirtualBox\VM\%VM%\%VM%.vdi"
VBoxManage createmedium --filename %VDI% --size 8192 --format VDI

REM Create VM of type RedHat, 64-bit, register it with VirtualBox and then 
REM create the storage controller on this guest to the disk we just made. 
VBoxManage createvm --name %VM% --ostype "RedHat_64" --register
VBoxManage storagectl %VM% --name "SATA Controller" --add sata --controller IntelAhci
VBoxManage storageattach %VM% --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "%VDI%"

REM Add an IDE controller with a DVD drive attached.  No need to have the install ISO inserted into the drive.
VBoxManage storagectl %VM% --name "IDE Controller" --add ide
VBoxManage storageattach %VM% --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium emptydrive

VBoxManage modifyvm %VM% --boot1 dvd 
VBoxManage modifyvm %VM% --boot2 disk 
VBoxManage modifyvm %VM% --boot3 none 
VBoxManage modifyvm %VM% --boot4 none

REM These are my favorite options, change to suit.
REM These options correspond to thoe ones presented in the Settings panel for a VM in the GUI.
REM I like 2Gb or RAM, 2 CPUs, SVGA video, basic mouse and USB, a UTC clock and I don't care about audio
VBoxManage modifyvm %VM% --memory 2048 --vram 16
VBoxManage modifyvm %VM% --rtcuseutc on
VBoxManage modifyvm %VM% --ioapic on --chipset piix3 --mouse ps2
VBoxManage modifyvm %VM% --cpus 2
VBoxManage modifyvm %VM% --hwvirtex on
VBoxManage modifyvm %VM% --graphicscontroller vboxsvga
VBoxManage modifyvm %VM% --usb on
VBoxManage modifyvm %VM% --audio none

REM VirtualBox networking is powerful/complex, so again, pick to suit
REM after reviewing the documentation.  Here we have the VM attaching to a 
REM previously created NAT network, with a port forwarding rule.   
VBoxManage modifyvm %VM% --nic1 natnetwork --nictype1 virtio --cableconnected1 on --nat-network1 %NETWORKNAME% --natpf1 "guestssh,tcp,,8022,,22"

REM Connect the VM to the install image and script, and boot it. 
VBoxManage unattended install %VM% --iso="%ISO%" --hostname=%VM% --script-template="%KS%"
VBoxManage startvm %VM%
