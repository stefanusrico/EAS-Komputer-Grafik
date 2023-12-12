import bpy
import math

class Plane:
    def __init__(self, size=1, location=(0, 0, 0), scale=(1, 1, 1)):
        self.size = size
        self.location = location
        self.scale = scale
        self.mesh_object = None

    def create_plane(self):
        bpy.ops.mesh.primitive_plane_add(
            size=self.size,
            enter_editmode=False,
            align='WORLD',
            location=self.location,
            scale=self.scale
        )
        self.mesh_object = bpy.context.active_object

class Cube:
    def __init__(self):
        self.verts = [
            (-1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (1.0, 1.0, -1.0),
            (1.0, -1.0, -1.0),
            (-1.0, -1.0, 1.0),
            (-1.0, 1.0, 1.0),
            (1.0, 1.0, 1.0),
            (1.0, -1.0, 1.0),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("cube_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("cube_object", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
#            self.mesh_object.scale= scale
        else:
            print("Warning: can't add mesh object because it is already added into the scene")

class SquareFaceCube(Cube):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (7, 4, 0, 3),
            (6, 7, 3, 2),
            (5, 6, 2, 1),
        ]

class CuboidSatu:
    def __init__(self):
        self.verts = [
            (-0.6, -0.6, -1.0),
            (-0.6, 0.6, -1.0),
            (0.6, 0.6, -1.0),
            (0.6, -0.6, -1.0),
            (-0.6, -0.6, 8.0),
            (-0.6, 0.6, 8.0),
            (0.6, 0.6, 8.0),
            (0.6, -0.6, 8.0),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("cuboid_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("cuboid_satu", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.scale = scale
        else:
            print("Warning: can't add mesh object because it is already added into the scene")

class CuboidDua:
    def __init__(self):
        self.verts = [
            (-1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (1.0, 1.0, -1.0),
            (1.0, -1.0, -1.0),
            (-1.0, -1.0, 4.0),
            (-1.0, 1.0, 4.0),
            (1.0, 1.0, 4.0),
            (1.0, -1.0, 4.0),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("cuboid_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("cuboid_object", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.scale = scale
        else:
            print("Warning: can't add mesh object because it is already added into the scene")

class CuboidFaceSatu(CuboidSatu):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (7, 4, 0, 3),
            (6, 7, 3, 2),
            (5, 6, 2, 1),
        ]

class CuboidFaceDua(CuboidDua):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (7, 4, 0, 3),
            (6, 7, 3, 2),
            (5, 6, 2, 1),
        ]

class BentukAneh:
    def __init__(self):
        self.verts = [
            (-1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (1.0, 1.0, -1.0),
            (1.0, -1.0, -1.0),
            (-1.0, -1.0, 4.0),
            (-1.0, 1.0, 4.0),
            (1.0, 1.0, 3.3),
            (1.0, -1.0, 3.3),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("bentuk_aneh_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("bentuk_aneh", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale, rotation):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.rotation_euler = rotation
            self.mesh_object.scale = scale
        else:
            print("Warning: can't add mesh object because it is already added into the scene")
            

class FacesBentukAneh(BentukAneh):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (7, 4, 0, 3),
            (6, 7, 3, 2),
            (5, 6, 2, 1),
        ]
        
class AtapSegitiga:
    def __init__(self):
        self.verts = [
            (5.0, -5.0, 0.0),
            (5.0, 5.0, 0.0),
            (5.0, 5.0, 1.0),
            (5.0, -5.0, 1.0),
            (0.0, -5.0, 5.0),
            (0.0, 5.0, 5.0),
            (0.0, -5.0, 4.0),
            (0.0, 5.0, 4.0),
            (-5.0, -5.0, 1.0),
            (-5.0, 5.0, 1.0),
            (-5.0, 5.0, 0.0),
            (-5.0, -5.0, 0.0),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("atap_segitiga_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("atap_segitiga", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.scale = scale
        else:
            print("Warning: can't add mesh object because it is already added into the scene")
            
class FacesAtapSegitiga(AtapSegitiga):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (2, 5, 4, 3),
            (0, 6, 7, 1),
            (4, 3, 0, 6),
            (1, 2, 5, 7),
            (5, 4, 8, 9),
            (7, 6, 11, 10),
            (7, 5, 9, 10),
            (6, 4, 8, 11),
            (8, 9, 10, 11)    
            ]

class AtapRadaLurus:
    def __init__(self):
        self.verts = [
            (-1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (1.0, 1.0, -0.75),
            (1.0, -1.0, -0.75),
            (-1.0, -1.0, -0.50),
            (-1.0, 1.0, -0.50),
            (1.0, 1.0, -0.25),
            (1.0, -1.0, -0.25),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("atap_lurus_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("atap_rada_lurus", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale, rotation):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.scale = scale
            self.mesh_object.rotation_euler = rotation
        else:
            print("Warning: can't add mesh object because it is already added into the scene")
            
class FacesAtapRadaLurus(AtapRadaLurus):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (7, 4, 0, 3),
            (6, 7, 3, 2),
            (5, 6, 2, 1), 
            ]
            
class PapanNama:
    def __init__(self):
        self.verts = [
            (-5.0, -1.0, -1.0),
            (-5.0, 1.0, -1.0),
            (5.0, 1.0, -1.0),
            (5.0, -1.0, -1.0),
            (-5.0, -1.0, 1.0),
            (-5.0, 1.0, 1.0),
            (5.0, 1.0, 1.0),
            (5.0, -1.0, 1.0),
            (0.0, -1.0, 2.5),
            (0.0, 1.0, 2.5),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("cuboid_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("cuboid_object", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.scale = scale
        else:
            print("Warning: can't add mesh object because it is already added into the scene")
            
class FacesPapanNama(PapanNama):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (4, 5, 1, 0),
            (6, 7, 3, 2),
            (8, 9, 6, 7),
            (4, 5, 9, 8),
            (1, 5, 9, 6, 2),
            (0, 4, 8, 7, 3),
            ]
            
class HiasanTembok:
    def __init__(self):
        self.verts = [
           (-1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (1.0, 1.0, -1.0),
            (1.0, -1.0, -1.0),
            (-1.0, -1.0, 1.0),
            (-1.0, 1.0, 1.0),
            (1.0, 1.0, 1.0),
            (1.0, -1.0, 1.0),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("cuboid_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("cuboid_object", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.scale = scale
        else:
            print("Warning: can't add mesh object because it is already added into the scene")
            
class FacesHiasanTembok(HiasanTembok):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (7, 4, 0, 3),
            (6, 7, 3, 2),
            (5, 6, 2, 1),
            ]
            
class HiasanTembok:
    def __init__(self):
        self.verts = [
            (-1.0, -1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (1.0, 1.0, -1.0),
            (1.0, -1.0, -1.0),
            (-1.0, -1.0, 1.0),
            (-1.0, 1.0, 1.0),
            (1.0, 1.0, 1.0),
            (1.0, -1.0, 1.0),
        ]

        self.faces = []
        self.mesh_data = None
        self.mesh_object = None

    def create_mesh_data(self):
        self.mesh_data = bpy.data.meshes.new("hiasan_tembok_data")
        self.mesh_data.from_pydata(self.verts, [], self.faces)

    def create_mesh_object_from_data(self):
        self.mesh_object = bpy.data.objects.new("hiasan_tembok", self.mesh_data)

    def add_mesh_object_into_scene(self):
        bpy.context.collection.objects.link(self.mesh_object)

    def create_mesh_object(self):
        self.create_mesh_data()
        self.create_mesh_object_from_data()
        self.add_mesh_object_into_scene()

    def add_into_scene(self, location, scale, rotation):
        if self.mesh_object is None:
            self.create_mesh_object()
            self.mesh_object.location = location
            self.mesh_object.scale = scale
            self.mesh_object.rotation_euler = rotation
        else:
            print("Warning: can't add mesh object because it is already added into the scene")
            
class FacesHiasanTembok(HiasanTembok):
    def __init__(self):
        super().__init__()
        self.faces = [
            (0, 1, 2, 3),
            (7, 6, 5, 4),
            (4, 5, 1, 0),
            (7, 4, 0, 3),
            (6, 7, 3, 2),
            (5, 6, 2, 1), 
            ]
            
class TextObject:
    def __init__(self, name, content, location=(0, 0, 0), rotation=(0,0,0), extrude=0.2, size=2.0):
        bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=location)
        self.text_object = bpy.context.active_object
        self.text_object.name = name
        self.text_object.data.body = content
        self.text_object.data.extrude = extrude
        self.text_object.data.size = size
        self.text_object.rotation_euler = rotation

def create_fence(scene, x, y, z, z_scale, rotation):
    fence = FacesBentukAneh()
    fence.add_into_scene(location=(x, y, z), scale=(1, 0.15, z_scale), rotation=rotation)

plane = Plane(size=50, location=(0, 0, 0), scale=(1, 1, 1))
plane.create_plane()

#set kamera

bpy.ops.object.add(type='EMPTY', location=(0, 0, 0))
empty = bpy.context.active_object
empty.name = 'MyEmpty'

bpy.ops.object.camera_add(location=(35, 100, 70), rotation=(math.radians(60), 0, math.radians(160)))
camera = bpy.context.active_object
camera.name = 'MyCamera'
bpy.context.scene.camera = camera

bpy.context.view_layer.objects.active = empty
empty.select_set(True)
camera.select_set(True)

bpy.ops.object.parent_set(type='OBJECT')

def rotate_empty(scene):
    empty.rotation_euler.z += math.radians(1)

bpy.app.handlers.frame_change_pre.append(rotate_empty)



####################################################################################################

#Kiri

face_cuboid_satu = CuboidFaceSatu()
face_cuboid_satu.add_into_scene(location=(20, 0, 3), scale=(2,2.5,3))
#add_random_color_material(face_cuboid_satu.mesh_object)

face_cuboid_dua = CuboidFaceDua()
face_cuboid_dua.add_into_scene(location=(15, 0, 3), scale=(2,2,3))

face_bentuk_aneh = FacesBentukAneh()
face_bentuk_aneh.add_into_scene(location=(15,0,18.5), scale=(2,1.5,3.5), rotation=(math.radians(0), math.radians(0), math.radians(0)))

face_atap_rada_lurus = FacesAtapRadaLurus()
face_atap_rada_lurus.add_into_scene(location=(17,0,24), scale=(8,3,1), rotation=(math.radians(0), math.radians(0), math.radians(180)))

face_hiasan_tembok= FacesHiasanTembok()
face_hiasan_tembok.add_into_scene(location=(20, 0, 19), scale=(2.0,2.3,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))

face_hiasan_tembok2= FacesHiasanTembok()
face_hiasan_tembok2.add_into_scene(location=(20, 0, 18), scale=(2,2.3,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))

#bolongin atap rada lurus dengan cuboid face satu
bpy.context.view_layer.objects.active = bpy.data.objects.get("atap_rada_lurus")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("cuboid_satu")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin atap rada lurus dengan bentuk aneh
bpy.context.view_layer.objects.active = bpy.data.objects.get("atap_rada_lurus")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("bentuk_aneh")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin hiasan tembok dengan cuboid satu
bpy.context.view_layer.objects.active = bpy.data.objects.get("hiasan_tembok")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("cuboid_satu")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin hiasan tembok dengan cuboid satu
bpy.context.view_layer.objects.active = bpy.data.objects.get("hiasan_tembok.001")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("cuboid_satu")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#face_hiasan_putih = FacesHiasanTembok()
#face_hiasan_putih.add_into_scene(location=(-15, 0, 3), scale=(2,2,3))

####################################################################################################

#Kanan

face_cuboid_satu = CuboidFaceSatu()
face_cuboid_satu.add_into_scene(location=(-20, 0, 3), scale=(2,2.5,3))
#add_random_color_material(face_cuboid_satu.mesh_object)

face_cuboid_dua = CuboidFaceDua()
face_cuboid_dua.add_into_scene(location=(-15, 0, 3), scale=(2,2,3))

face_bentuk_aneh = FacesBentukAneh()
face_bentuk_aneh.add_into_scene(location=(-15,0,18.5), scale=(2,1.5,3.5), rotation=(math.radians(0), math.radians(0), math.radians(180)))

face_atap_rada_lurus = FacesAtapRadaLurus()
face_atap_rada_lurus.add_into_scene(location=(-17,0,24), scale=(8,3,1), rotation=(math.radians(0), math.radians(0), math.radians(0)))

face_hiasan_tembok3= FacesHiasanTembok()
face_hiasan_tembok3.add_into_scene(location=(-20, 0, 19), scale=(2.0,2.3,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))

face_hiasan_tembok4= FacesHiasanTembok()
face_hiasan_tembok4.add_into_scene(location=(-20, 0, 18), scale=(2,2.3,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))

face_hiasan_tembok5= FacesHiasanTembok()
face_hiasan_tembok5.add_into_scene(location=(0, 0, 7.5), scale=(1.25,5,3), rotation=(math.radians(180), math.radians(0), math.radians(0)))

face_hiasan_tembok6= FacesHiasanTembok()
face_hiasan_tembok6.add_into_scene(location=(0, 0, 7.5), scale=(0.9,5,2.5), rotation=(math.radians(180), math.radians(0), math.radians(0)))

#hiasan tembok antara bentuk aneh dan cuboid dua disebelah kiri
face_hiasan_tembok7= FacesHiasanTembok()
face_hiasan_tembok7.add_into_scene(location=(15, 0, 16), scale=(3,3,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))

face_hiasan_tembok8= FacesHiasanTembok()
face_hiasan_tembok8.add_into_scene(location=(15, 0, 15.5), scale=(2.75,2.75,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))
#end hiasan tembok antara bentuk aneh dan cuboid dua disebelah kiri

#hiasan tembok antara bentuk aneh dan cuboid dua disebelah kanan
face_hiasan_tembok9= FacesHiasanTembok()
face_hiasan_tembok9.add_into_scene(location=(-15, 0, 16), scale=(3,3,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))

face_hiasan_tembok10= FacesHiasanTembok()
face_hiasan_tembok10.add_into_scene(location=(-15, 0, 15.5), scale=(2.75,2.75,0.3), rotation=(math.radians(0), math.radians(0), math.radians(0)))
#end hiasan tembok antara bentuk aneh dan cuboid dua disebelah kanan

#bolongin atap rada lurus dengan cuboid face dua
bpy.context.view_layer.objects.active = bpy.data.objects.get("atap_rada_lurus.001")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("cuboid_satu.001")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin atap rada lurus dengan bentuk aneh dua
bpy.context.view_layer.objects.active = bpy.data.objects.get("atap_rada_lurus.001")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("bentuk_aneh.001")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin hiasan tembok dengan cuboid satu
bpy.context.view_layer.objects.active = bpy.data.objects.get("hiasan_tembok.002")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("cuboid_satu.001")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin hiasan tembok dengan cuboid satu
bpy.context.view_layer.objects.active = bpy.data.objects.get("hiasan_tembok.003")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("cuboid_satu.001")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin hiasan tembok dengan cuboid satu
bpy.context.view_layer.objects.active = bpy.data.objects.get("hiasan_tembok.004")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("hiasan_tembok.005")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")
bpy.data.objects.remove(bpy.data.objects.get("hiasan_tembok.005"), do_unlink=True) #menghapus objek yg digunakan untuk memoton hiasan_tembok_3


face_hiasan_tembok5.mesh_object.scale = (1.25, 2.5, 5)
face_hiasan_tembok5.mesh_object.location = (-15,0,7)

#Duplikasi dari face_hiasan_tembok5 (hiasan cuboid dua kiri)
duplicated_object = face_hiasan_tembok5.mesh_object.copy()
bpy.context.collection.objects.link(duplicated_object)
duplicated_object.location = (15,0,7)
duplicated_object.scale = (1.25, 2.5, 5)

####################################################################################################

#tengah

face_papan_nama = FacesPapanNama()
face_papan_nama.add_into_scene(location=(0,0,25.6), scale=(2.6,1.15,2))

face_atap_segitiga = FacesAtapSegitiga()
face_atap_segitiga.add_into_scene(location=(0, 0, 26), scale=(5.0,1,1))

#bolongin atap segitiga dengan bentuk aneh
bpy.context.view_layer.objects.active = bpy.data.objects.get("atap_segitiga")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("bentuk_aneh")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")

#bolongin atap segitiga dengan bentuk aneh dua
bpy.context.view_layer.objects.active = bpy.data.objects.get("atap_segitiga")
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].use_self = True
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects.get("bentuk_aneh.001")
bpy.ops.object.modifier_apply({"object": face_atap_rada_lurus}, modifier="Boolean")


#pagar kanan

# Pagar kanan depan
y_position = 3.15
z_position = 1.45
rotation=(math.radians(0), math.radians(0), math.radians(90))
for i in range(5):
    z_scaling = 1.5 - i * 0.2 
    create_fence(face_bentuk_aneh, -16.75, y_position, z_position, z_scaling, rotation)
    y_position += 2
    z_position -= 0.2
# End pagar kanan depan

# Pagar kanan belakang
y_position = -3.15
z_position = 1.45
rotation = (math.radians(0), math.radians(0), math.radians(-90))
for i in range(5):
    z_scaling = 1.5 - i * 0.2 
    create_fence(face_bentuk_aneh, -16.75, y_position, z_position, z_scaling, rotation)
    y_position -= 2
    z_position -= 0.2
# End pagar kanan belakang


#pagar kiri

#Pagar kiri depan
y_position = 3.15
z_position = 1.45
rotation=(math.radians(0), math.radians(0), math.radians(90))
for i in range(5):
    z_scaling = 1.5 - i * 0.2 
    create_fence(face_bentuk_aneh, 16.75, y_position, z_position, z_scaling, rotation)
    y_position += 2
    z_position -= 0.2
    
#End pagar kiri depan

#Pagar kiri belakang
y_position = -3.15
z_position = 1.45
rotation = (math.radians(0), math.radians(0), math.radians(-90))
for i in range(5):
    z_scaling = 1.5 - i * 0.2 
    create_fence(face_bentuk_aneh, 16.75, y_position, z_position, z_scaling, rotation)
    y_position -= 2
    z_position -= 0.2
#End pagar kiri belakang

#Teks papan nama

#teks depan
teks_depan = TextObject(name="teks_depan", content="SELAMAT DATANG", location=(11, 1.5, 25), rotation=(math.radians(90), math.radians(0), math.radians(180)), extrude=0.2, size=2.5)
teks_belakang = TextObject(name="teks_depan", content="SELAMAT TINGGAL", location=(-11, -1.5, 25), rotation=(math.radians(90), math.radians(0), math.radians(0)), extrude=0.2, size=2.5)