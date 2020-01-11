import os
import channels.asgi
from hiregarrett import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiregarrett.settings")
channel_layer = channels.asgi.get_channel_layer()