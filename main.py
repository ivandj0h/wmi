# Windows Management Instrumentation
# To get System Information

import wmi

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacture: {my_system.Manufacture}")
