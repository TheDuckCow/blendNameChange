########
"""
This code is open source under the MIT license.

It tries to change the name of all attributes of an object
that match an input format, for example if an object is
formatted with the name 'steve', such that it consists of
objects 'steve_arm' or 'steve.eye.L' or 'steve.materialMain'
and so forth.

Currently works for objects, materials, groups

"""

########
bl_info = {
	"name": "Rename Attributes",
	"category": "Object",
	"version": (1, 0),
	"blender": (2, 71, 0),
	"location": "3D window toolshelf",
	"description": "Help rename several assets of a common format",
	"wiki_url": "https://github.com/TheDuckCow/blendNameChange",
	"author": "Patrick W. Crawford, TheDuckCow"
}



#change name systematically
# currently works for: objects, materials (first slot..), groups
# >> need to support MESH names (indp of objects)
# and textures under the materials

# bugged if "replace" already exists in the "key", because of dataloops


def matList(objList):
    matList = []
    for obj in objList:
        #ignore non mesh selected objects
        if obj.type != 'MESH': continue
        
        #check that operation has not already been done to material:
        #mat = obj.material_slots
        
        for mat in obj.material_slots:
            if not mat.material.name in matList: matList.append(mat.material)
    return matList


def texList(materials):
    texList = []
    for mat in materials:
        for slot in mat.texture_slots:
            try:
                if not slot.texture in texList: texList.append(slot.texture)
            except: continue
    
    return texList

#######
# the main function
def nameChange():
	
	key = "steve"
	replace = "guyBlue"
	
	context = bpy.context
	nameList = context.selected_objects
	materials = matList(nameList)
	nameList += materials
	nameList += texList(materials)

	#iteration for object names
	for name in nameList:
	    tmp = name.name.split(key)
	    print(tmp)
	    newName = tmp[0]
	    
	    if (len(tmp) != 1):
	        for a in tmp[1:]:
	            print(newName)
	            newName = newName + replace + a
	            
	        print(newName)
	        #assign new name
	    name.name = newName
	
	for group in bpy.data.groups:
	    # to be consistent, should only check groups part of current selection...
	    if (group.name == key):
	        group.name = replace
	        print("group renamed: "+replace)


#######
# Class for updating the duplicated proxy spawn files
class attChange(bpy.types.Operator):
	"""Renames attributes of a consistent base name to a new base name"""
	bl_idname = "object.attChange"
	bl_label = "Rename Attribute"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		nameChange()
		
		return {'FINISHED'}


#######
# panel for these declared tools
class attChange_panel(bpy.types.Panel):
	"""renameAttributes"""
	bl_label = "Raname Attributes Panel"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'

	def draw(self, context):
		
		layout = self.layout

		split = layout.split()
		col = split.column(align=True)



#######
# un/registration to run addon
def register():
	bpy.utils.register_class(attChange)
	bpy.utils.register_class(attChange_panel)
	
	#properties
	bpy.types.Scene.attChange_find = bpy.props.StringProperty(
		name="Starting name key, like 'find'",
		description="This is the name that is searched for within the full name of any attribute, and then replaced with a new name",
		default="startingName")
	bpy.types.Scene.attChange_replace = bpy.props.StringProperty(
		name="Replacing name key, like 'replace'",
		description="Attributes with the starting key substring will have that substring changed to this name",
		default="replaceName")


def unregister():
	bpy.utils.unregister_class(attChange)
	bpy.utils.unregister_class(attChange_panel)
	
	#properties
	del bpy.types.Scene.attChange_find
	del bpy.types.Scene.attChange_replace


if __name__ == "__main__":
	register()