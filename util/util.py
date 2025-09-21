# server/utils.py
from datetime import datetime

def safe_timestamp():
    """Return a short timestamp string for logs."""
    return datetime.now().strftime("[%H:%M:%S]")
