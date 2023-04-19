from bpy.types import Panel
from bpy.utils import register_class, unregister_class

class FrameUtilsPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "FrameUtils"

class PT_FrameUtilsPanel(FrameUtilsPanel, Panel):
    bl_idname = "PT_FrameUtilsPanel"
    bl_label = "Frame Utils Panel"

    def draw(self, context):
        layout = self.layout
        frame_utils_data = context.scene.FrameUtilsData # <- set in standoff_props.register()
        # layout.prop(frame_utils_data, "obj") # Add a pointer property to the panel
        layout.prop(frame_utils_data, "obj1")
        layout.prop(frame_utils_data, "obj2")
        text = ""
        if frame_utils_data.obj1 and frame_utils_data.obj2:
            _1_T_2 = frame_utils_data.obj1.matrix_world.inverted() @ frame_utils_data.obj2.matrix_world
            text = f"{frame_utils_data.obj2.name} wrt {frame_utils_data.obj1.name}" + "\n"
            text += f"Position: {_1_T_2.translation}" + "\n"
            text += f"Orientation: {_1_T_2.to_quaternion()}" + "\n"
        layout.label(text=text)
        # layout.operator("scene.add_new_standoff") # <- registered in standoff_operator.py
        # layout.prop(standoff_data, "metric_diameter")
        # layout.prop(standoff_data, "height")

def register():
    register_class(PT_FrameUtilsPanel)

def unregister():
    unregister_class(PT_FrameUtilsPanel)