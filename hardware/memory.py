import psutil

svmem = psutil.virtual_memory()

def bytes_to_human(value, suffix="B"):
    if value is None:
        return "N/A"
    value = float(value)
    for unit in ("", "K", "M", "G", "T", "P"):
        if abs(value) < 1024:
            return f"{value:.2f}{unit}{suffix}"
        value /= 1024
    return f"{value:.2f}EB"

def get_memory_info():
    memory_info = {
        "total ram": bytes_to_human(svmem.total),
        "used ram": bytes_to_human(svmem.used),
        "available ram": bytes_to_human(svmem.available)
    }
    return memory_info