# sample16

A simple Blender add-on that exposes the scene's frame range in a sidebar tab.

## Installation

1. Open Blender and go to **Edit > Preferences > Add-ons**.
2. Click **Install** and select `blender_version_panel.py` from this repository.
3. Enable the add-on from the list.
4. Open the 3D Viewport and press **N** to open the Sidebar. A tab named **テストプラグイン** shows inputs for **Frame Start** and **Frame End**.


## Packaging on Windows

If you need a ZIP file for installation, run `package_addon.bat`. The script
creates `blender_version_panel.zip` that can be installed via Blender's add-on
preferences.
