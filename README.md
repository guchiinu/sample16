# sample16

A simple Blender add-on that shows the current Blender version in the N panel.

## Installation

1. Open Blender and go to **Edit > Preferences > Add-ons**.
2. Click **Install** and select `blender_version_panel.py` from this repository.
3. Enable the add-on from the list.
4. Open the 3D Viewport and press **N** to open the Sidebar. A new tab named **Version** will display the current Blender version.


## Packaging on Windows

If you need a ZIP file for installation, run `package_addon.bat` from this
directory. The script creates `blender_version_panel.zip` containing a folder
named `blender_version_panel` with `__init__.py` inside. Install the ZIP via
Blender's add-on preferences.
