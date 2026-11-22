from . import gpu, cpu, memory, system, storage, network


def scan_hardware():
    return {
        "system": system.get_system_info(),
        "storage": storage.get_storage_info(),
        "network": network.get_network_info(),
        "gpu": gpu.get_gpu_info(),
        "cpu": cpu.get_cpu_info(),
        "memory": memory.get_memory_info()
    }

print(scan_hardware())