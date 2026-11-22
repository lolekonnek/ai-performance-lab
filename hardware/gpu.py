
import vulkan as vk


def get_gpu_info():
    gpu_info_list = []

    app = vk.VkApplicationInfo(
        sType=vk.VK_STRUCTURE_TYPE_APPLICATION_INFO,
        pApplicationName="GPU Scanner",
        applicationVersion=vk.VK_MAKE_VERSION(1, 0, 0),
        pEngineName="None",
        engineVersion=vk.VK_MAKE_VERSION(1, 0, 0),
        apiVersion=vk.VK_API_VERSION_1_0
    )

    instance_info = vk.VkInstanceCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
        pApplicationInfo=app
    )

    instance = vk.vkCreateInstance(instance_info, None)

    try:
        devices = vk.vkEnumeratePhysicalDevices(instance)

        for device in devices:
            props = vk.vkGetPhysicalDeviceProperties(device)

            name = props.deviceName
            if isinstance(name, bytes):
                name = name.decode("utf-8", errors="replace")

            gpu_info = {
                "name": name,
                "vendor_id": hex(props.vendorID),
                "device_id": hex(props.deviceID),
                "driver_version": props.driverVersion,
                "vulkan_api_version": props.apiVersion
            }

            gpu_info_list.append(gpu_info)

    finally:
        vk.vkDestroyInstance(instance, None)

    return gpu_info_list
