bl_info = {
    "name": "Blender Version Panel",
    "author": "OpenAI Codex",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "description": "Display the current Blender version in the N panel",
    "category": "3D View"
}

import bpy

class VIEW3D_PT_blender_version(bpy.types.Panel):
    bl_label = "Blender Version"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Version"

    def draw(self, context):
        layout = self.layout
        layout.label(text=f"Blender version: {bpy.app.version_string}")


def register():
    bpy.utils.register_class(VIEW3D_PT_blender_version)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_blender_version)


if __name__ == "__main__":
    register()
