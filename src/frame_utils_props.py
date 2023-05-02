import bpy
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

class PG_FrameUtils(bpy.types.PropertyGroup):
    # Define properties
    reference: bpy.props.PointerProperty(type=bpy.types.Object)
    target: bpy.props.PointerProperty(type=bpy.types.Object)
    coordinate_system: bpy.props.PointerProperty(type=bpy.types.Object)

def register():
    register_class(PG_FrameUtils)
    bpy.types.Scene.FrameUtilsData = PointerProperty(type=PG_FrameUtils)

def unregister():
    unregister_class(PG_FrameUtils)
    del bpy.types.Scene.FrameUtilsData