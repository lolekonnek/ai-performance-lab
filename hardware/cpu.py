import cpuinfo

info = cpuinfo.get_cpu_info()

def get_cpu_info():
    cpu_info = {
        "model": info.get("brand_raw", "Unknown CPU"),
        "vendor": info.get("vendor_id_raw", "Unknown Vendor"),
        "architecture": info.get("arch", "Unknown Architecture"),
        "bits": info.get("bits", "Unknown Bits"),
        "family": info.get("family", "Unknown Family"),
        "model_number": info.get("model", "Unknown Model Number"),
        "stepping": info.get("stepping", "Unknown Stepping")
    }
    return cpu_info
