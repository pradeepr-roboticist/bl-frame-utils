bl_info = {
    "name": "FrameUtils",
    "description": "Common operations on transform frames",
    "author": "Pradeep Rajendran <pradeepr.roboticist@gmail.com>",
    "version": (0, 0, 1),
    "blender": (2, 90, 1),
    "category": "3D View"
}

module_names = [
    'frame_utils_props',
    'frame_utils_operator',
    'frame_utils_panel'
    ]

import sys
import importlib

module_full_names = [ f"{__name__}.{module}" for module in module_names ]

for module in module_full_names:
    if module in sys.modules:
        importlib.reload(sys.modules[module])
    else:
        locals()[module] = importlib.import_module(module)
        setattr(locals()[module], 'module_names', module_full_names)

def register():
    for module in module_full_names:
        if module in sys.modules:
            if hasattr(sys.modules[module], 'register'):
                sys.modules[module].register()

def unregister():
    for module in module_full_names:
        if module in sys.modules:
            if hasattr(sys.modules[module], 'unregister'):
                sys.modules[module].unregister()