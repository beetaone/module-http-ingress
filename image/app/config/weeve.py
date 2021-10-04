"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "HTTP-Ingress"),
    "MODULE_TYPE": env("MODULE_TYPE", "INGRESS"),
    "EGRESS_SCHEMA": env("EGRESS_SCHEME", "http"),
    "EGRESS_HOST": env("EGRESS_HOST", "localhost"),
    "EGRESS_PORT": env("EGRESS_PORT", "80"),
    "EGRESS_PATH": env("EGRESS_PATH", ""),
    "EGRESS_URL": env("EGRESS_URL", "")
}
