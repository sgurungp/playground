# Getting the MSI BE6500 USB Wi-Fi adapter working

Notes and tips on getting this adapter working on Linux (Mint).

## Background

Test laptop with an ancient on-board Wi-Fi system that only supports
2.4GHz 802.11n - i.e., slow Wi-Fi. I bought an MSI BE6500 USB adapter to see 
if I could improve things.

It uses a Realtek RTL8812 chipset. This is not supported out of the box in 
Mint 22.3/Zena with kernel 6.8.something. So, some assembly is required.

For deeper technical info, see [morrownr/USB-WiFi on GitHub](https://github.com/morrownr/USB-WiFi).

## Set up build environment

Set up the build env, clone the repo, and build the driver:

    sudo apt install build-essential git dkms linux-headers-$(uname -r)
    git clone https://github.com/morrownr/rtw89
    cd  rtw89/
    sudo make cleanup_target_system 
    sudo dkms install $PWD
    sudo make install_fw
    sudo cp -v rtw89.conf /etc/modprobe.d/

### Extra steps relating to Secure Boot
Verify if you have Secure Boot enabled or no. 

    sudo mokutil --sb-state

If you do, run the following command and feed it your Secure Boot pasword.

    sudo mokutil --import /var/lib/shim-signed/mok/MOK.der

## Clean up
The MSI can come up on the USB port looking like a storage device, which
messes with boot up (this is a side effect of how the adapter behaves in Windows,
where it appears as a USB flash drive containing the driver installer for that OS).
Disable these sorts of shenanigans.

    sudo cp usb_storage.conf /etc/modprobe.d/usb_storage.conf

Update the initfs:

    sudo update-initramfs -u -k all

## Reboot (1)

You could probably continue without rebooting and call `modprobe` and suchlike to
bring the new Wi-Fi interface to life. But rebooting is fine.

## Disable the built-in Wi-Fi

My laptop had a combined Wi-Fi and Bluetooth adapter built-in. Since I never use
Bluetooth, and I no longer need the old Wi-Fi, it was safe to disable it, by
ensuring the kernel modules never loaded.

    sudo vi /etc/modprobe.d/blacklist-ath-wifi.conf

Use these lines:
    
    # Disable the ath (atheros) wi-fi driver since  
    # we want to use the Realtek out of tree driver  
    # and our USB Wi-Fi adapter instead.
      
    blacklist ath  
    blacklist ath9k  
    blacklist ath9k_common  
    blacklist ath9k_hw  
      
    install ath          /bin/false  
    install ath9k        /bin/false  
    install ath9k_common /bin/false  
    install ath9k_hw     /bin/false  

## Reboot (2)

When you reboot here, you will lose your Wi-Fi since the old interface
will not come up and the new one hasn't been configured yet.

## Verify the new Wi-Fi is present
    lsmod | grep rtw

Look for references to `rtw89_<...>`

    iw list

This produces a lot of output, but you'll know all is well if you see things
that are never present in 2.4GHz, e.g., 80Mhz channels.

## Configure Wi-Fi

Mint offers `nm-connection-editor` to set up Wi-Fi. Fire it up and set up
the Wi-Fi to connect to the SSID.

You can verify status with, say

    ip link show
    ip addr show

...or the rather wonderful `nmcli` tool:

    nmcli device wifi

# Caveats/to-do
 - Wi-Fi 7 (investigate driver)
 - Running in different modes, e.g., monitor mode
 - Renaming the interface name to, e.g., wlan1
