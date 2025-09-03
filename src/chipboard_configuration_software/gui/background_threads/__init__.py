"""
This package houses the modules that contain the background GUI QThread
classes and associated helpers for background GUI threads.

NOTE: Because of Python's GIL nothing is really multithreaded for simultaneous execution. Any major blocking calls or
true CPU bound simultaneous work is done using calls to complied C functions that exist outside the GIL.
"""



