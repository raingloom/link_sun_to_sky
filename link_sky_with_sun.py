import bpy
C=bpy.context

'''#TODO: make it into a proper add-on
bl_info = {
    'name': "Link Sky to Sun",
    'author': "Eugenio Pignataro Oscurart, Greg Zaal, Peter Pronai",
    'version': (0, 5),
}
'''

def get_sun():
    # search in this order(active, selected, all in scene)
    for o_list in ([C.active_object]+C.selected_objects,C.scene.objects):
        for o in o_list:
            if o is not None and o.type=='LAMP':
                return o
    return False

# return: ( node, was_created )
def get_node( node_bl_idname, create_if_missing=True ):
    nodes = C.scene.world.node_tree.nodes
    for n in nodes:
        if n.bl_idname == node_bl_idname:
            return n
    if create_if_missing:
        return nodes.new( node_bl_idname )
    return False


node_types = ('ShaderNodeTexSky', 'ShaderNodeNormal')

def setup_stuff():
    sun = get_sun()
    if not sun:
        return False
    n_sky = get_node( node_types[0] )
    n_nrm = get_node( node_types[1] )
    for driver in (n_sky.driver_add( 'sun_direction' ),n_nrm.outputs['Normal'].driver_add( 'default_value' )):
        for i in range(3):
            vname = "r"+"xyz"[i]
            var = driver[i].driver.variables.new()
            var.name = vname
            driver[i].driver.expression = vname
            var.type = 'SINGLE_PROP'
            var.targets[0].id = sun
            var.targets[0].data_path = 'matrix_world[2][%d]'%(i)
    return True

setup_stuff()