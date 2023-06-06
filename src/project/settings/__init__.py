import os

print("Running with develop settings.")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.develop')
from .develop import *