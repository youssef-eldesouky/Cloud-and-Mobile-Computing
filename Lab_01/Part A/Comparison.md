## Startup Time Comparison

The container started almost instantly (within a few seconds)

while the VM took significantly longer to initialize.

***Conclusion: Containers have faster startup time because they do not require booting a full operating system.***
## Memory Usage Comparison

The VM shows higher memory usage because it runs a full OS with its own kernel.

The container uses significantly less memory because it shares the host OS kernel.

***Conclusion: Containers are more memory-efficient.***
## Process Count Comparison

The VM runs many system-level processes because it behaves like a full machine.

The container runs fewer processes since it only includes what is necessary for the application.

***Conclusion: Containers have lower process overhead.***