"""
Personal AI System
Settings Core v0.3

Central configuration
"""


SYSTEM_CONFIG = {

    "name": "Personal AI",

    "version": "0.3",

    "language": "fa",

    "mode": "development",

    "memory_enabled": True,

    "learning_enabled": True,

    "web_access": False,

    "telegram_enabled": False

}



AI_LIMITS = {

    "max_memory_items": 10000,

    "max_response_length": 4000

}



SECURITY = {

    "allow_external_tools": False,

    "require_confirmation": True

}



def get_setting(key, default=None):

    return SYSTEM_CONFIG.get(
        key,
        default
    )



def update_setting(key, value):

    SYSTEM_CONFIG[key] = value

    return True
