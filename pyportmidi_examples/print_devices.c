#include <portmidi.h>
#include <stdio.h>

// cc -lportmidi print_devices.c -o print_devices
int main() { 
    Pm_Initialize();
    int num_devices = Pm_CountDevices();
    int i; 

    for(i = 0; i < num_devices; i++) {
        PmDeviceInfo const *info = Pm_GetDeviceInfo(i);
        char *io = (info->input) ? "InputStream" : "OutputStream";
        printf("%s, %s, %d\n", info->name, io, i);
    }

    Pm_Terminate();
    return 0;
}
