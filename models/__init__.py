<<<<<<< HEAD
"""Module for FileStorage autoinit."""
from models.engine.file_storage import FileStorage
=======
#!/usr/bin/python3
"""Module to create a unique FileStorage instance"""
from models.engine.file_storage import FileStorage

>>>>>>> 73a8d997822c80c5e1e76d5e5c115f236047c773
storage = FileStorage()
storage.reload()
