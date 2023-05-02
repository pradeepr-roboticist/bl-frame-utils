from bpy.types import Panel
from bpy.utils import register_class, unregister_class
import mathutils
import textwrap
 
def _label_multiline(context, text, parent):
    chars = int(context.region.width / 7)   # 7 pix on 1 character
    wrapper = textwrap.TextWrapper(width=chars)
    text_lines = wrapper.wrap(text=text)
    for text_line in text_lines:
        parent.label(text=text_line)

class FrameUtilsPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "FrameUtils"

class PT_FrameUtilsPanel(FrameUtilsPanel, Panel):
    bl_idname = "PT_FrameUtilsPanel"
    bl_label = "Frame Utils Panel"

    def draw(self, context):
        layout = self.layout
        frame_utils_data = context.scene.FrameUtilsData
        layout.prop(frame_utils_data, "reference", text="Reference")
        layout.prop(frame_utils_data, "target", text="Target")
        layout.prop(frame_utils_data, "coordinate_system", text="Expressed In")
        text = ""
        reference = frame_utils_data.reference
        target = frame_utils_data.target
        coordinate_system = frame_utils_data.coordinate_system
        if coordinate_system is None:
            coordinate_system = reference
        if reference and target:
            _1_T_2 = reference.matrix_world.inverted() @ target.matrix_world
            layout.label(text=f"{target.name} wrt {reference.name} (R)")
            pos = _1_T_2.translation
            quat = _1_T_2.to_quaternion()
            layout.label(text=f"R_X = {pos.x}")
            layout.label(text=f"R_Y = {pos.y}")
            layout.label(text=f"R_Z = {pos.z}")
            layout.label(text=f"R_QX = {quat.x}")
            layout.label(text=f"R_QY = {quat.y}")
            layout.label(text=f"R_QZ = {quat.z}")
            layout.label(text=f"R_QW = {quat.w}")
            layout.label(text="-"*20)
            layout.label(text=f"Expressed in {coordinate_system.name}, (R_X, R_Y, R_Z) is:")
            pos2 = mathutils.Vector((pos.x, pos.y, pos.z, 0))
            rep = coordinate_system.matrix_world.inverted() @ reference.matrix_world @ pos2
            layout.label(text=f"C_X = {rep.x}")
            layout.label(text=f"C_Y = {rep.y}")
            layout.label(text=f"C_Z = {rep.z}")
        # layout.label(text=text)
        # _label_multiline(context=context, text=text, parent=layout)
        # layout.operator("scene.add_new_standoff") # <- registered in standoff_operator.py
        # layout.prop(standoff_data, "metric_diameter")
        # layout.prop(standoff_data, "height")

def register():
    register_class(PT_FrameUtilsPanel)

def unregister():
    unregister_class(PT_FrameUtilsPanel)