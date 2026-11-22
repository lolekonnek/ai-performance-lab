import socket
import psutil


def get_network_info():
    network_info = []

    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    counters = psutil.net_io_counters(pernic=True)

    for interface, addrs in interfaces.items():
        interface_info = {
            "interface": interface,
            "is_up": stats[interface].isup if interface in stats else None,
            "speed_mbps": stats[interface].speed if interface in stats else None,
            "addresses": [],
            "statistics": {}
        }

        for addr in addrs:
            if addr.family == socket.AF_INET:
                interface_info["addresses"].append({
                    "type": "IPv4",
                    "ip_address": addr.address,
                    "netmask": addr.netmask,
                    "broadcast": addr.broadcast
                })

            elif addr.family == socket.AF_INET6:
                interface_info["addresses"].append({
                    "type": "IPv6",
                    "ip_address": addr.address,
                    "netmask": addr.netmask
                })

            elif getattr(psutil, "AF_LINK", None) == addr.family:
                interface_info["addresses"].append({
                    "type": "MAC",
                    "address": addr.address
                })

        if interface in counters:
            interface_info["statistics"] = {
                "bytes_sent": counters[interface].bytes_sent,
                "bytes_received": counters[interface].bytes_recv
            }

        network_info.append(interface_info)

    return network_info