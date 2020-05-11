#################################################################
################# Copyright (c) 2020 Eric Olson #################
########################## MIT LICENSE ##########################
#################################################################
# Welcome! This is Palette Redux. It is a simple palette addon
# for Blender 3d. Feel free to use/modify in whatever way you'd 
# like according to the license. 

#################################################################
############################# Usage #############################
#################################################################
# 1) Add this script to Blender, whether as an addon or a custom
#    script.
# 2) Navigate to the 'Scene' tab inside Blender. 
# 3) Start picking colors.

#################################################################
############################# TODOs #############################
#################################################################
# 1) Implement import/export of palettes
# 2) Ensure that saving a .blend file also saves the palette
# 3) Add in ability to change the palette_sqrt value

# Maybes:
# 1) Add ability to automatically update nodes/other colors that
#    are populated from the palette when it changes

import bpy
import json

palette_sqrt = 16
palette_size = palette_sqrt * palette_sqrt

class PaletteColor(bpy.types.PropertyGroup):
    bl_idname = "OBJECT_PT_palattcolorredux"
    color: bpy.props.FloatVectorProperty(
            subtype="COLOR",
            size=4,
            min=0.0,
            max=1.0,
            default=(1.0, 1.0, 1.0, 1.0)
        )

class ResetReduxpaletteButton(bpy.types.Operator):
    bl_idname = "object.resetredux"
    bl_label = "Reset"

    def execute(self, context):
        resetRedux()
        return {'FINISHED'}
    
class RegisterReduxpaletteButton(bpy.types.Operator):
    bl_idname = "object.registerredux"
    bl_label = "Register"

    def execute(self, context):
        register()
        return {'FINISHED'}


class LoadReduxpaletteButton(bpy.types.Operator):
    bl_idname = "object.loadredux"
    bl_label = "Load palette"

    def execute(self, context):
        print("TODO: load pallate")
        return {'FINISHED'}
    

class SaveReduxpaletteButton(bpy.types.Operator):
    bl_idname = "object.saveredux"
    bl_label = "Export palette"

    def execute(self, context):
        print("TODO: export pallate")
        palette = bpy.context.scene.get("redux_palette")
        if palette is not None:
            color_palette = []
            for color in bpy.context.scene.redux_palette:                            
                c = []               
                
                for color_val in color.color:
                    c.append(color_val)
                
                color_palette.append(c)
                
            print(color_palette)
            
        return {'FINISHED'}



class palettePanelRedux(bpy.types.Panel):
    bl_idname = "OBJECT_PT_palettepanelredux"
    bl_label = "palettePanelREDUX"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    @classmethod
    def poll(self, context):
        return True

    def draw(self, context):        
        layout = self.layout
        box_a = layout.box()
        box_b = layout.box()
        icon_layout = box_a.grid_flow()
        color_layout = box_b

        # Draw the menu
        icon_layout.operator("object.resetredux", text='reset palette', icon="TRASH")
        icon_layout.operator("object.registerredux", text='DEBUG: register redux', icon="IMPORT")
        icon_layout.operator("object.loadredux", text='Import palette', icon="IMPORT")
        icon_layout.operator("object.saveredux", text='Export palette', icon="EXPORT")
        draw_color_grid(color_layout)

def draw_color_grid(layout):
#    grid = layout.grid_flow(columns=palette_sqrt, even_columns=True, even_rows=True, align=True)
    l = layout.column_flow(columns=palette_sqrt,align=True)
    palette = bpy.context.scene.get("redux_palette")
    if palette is not None:
        for color in bpy.context.scene.redux_palette:
            l.prop(color, "color", icon_only=True)
            


                
class PaletteColorRamp(bpy.types.ColorRamp):
    pass


def resetRedux():
#    if bpy.context.scene.get("redux_palette") is None:
    bpy.types.Scene.redux_palette = bpy.props.CollectionProperty(type=paletteColor)
    
    bpy.context.scene.redux_palette.clear()
    
    for i in range(0, palette_size):
        bpy.context.scene.redux_palette.add()
        
 
            

def register():    
    try:    
        bpy.utils.register_class(ResetReduxpaletteButton)
    except ValueError:
        pass
    
    try:
        bpy.utils.register_class(LoadReduxpaletteButton)
    except ValueError:
        pass
    
    try:
        bpy.utils.register_class(SaveReduxpaletteButton)
    except ValueError:
        pass
        
    try:
        bpy.utils.register_class(RegisterReduxpaletteButton)
    except ValueError:
        pass

    try:    
        bpy.utils.register_class(PaletteColor)
    except ValueError:
        pass
    try:    
        bpy.utils.register_class(PalettePanelRedux)
    except ValueError:
        pass

   
# Final stuff
if __name__ == '__main__':
    register()