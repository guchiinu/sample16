bl_info = {
    "name": "Test Plugin Panel",
    "author": "OpenAI Codex",
    "version": (1, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "description": "Show frame range controls in the N panel",
    "category": "3D View"
}

import bpy

class VIEW3D_PT_test_plugin(bpy.types.Panel):
    bl_label = "テストプラグイン"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "テストプラグイン"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        # Display the frame range with localized labels so that the start
        # frame appears on the left as "開始" and the end frame on the right
        # as "終了".
        row.prop(context.scene, "frame_start", text="開始")
        row.prop(context.scene, "frame_end", text="終了")

def register():
    bpy.utils.register_class(VIEW3D_PT_test_plugin)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_test_plugin)


if __name__ == "__main__":
    register()
