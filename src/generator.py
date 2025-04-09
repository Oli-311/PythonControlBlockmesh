from geometry.blocks import blocks
from geometry.boundary import boundary
from geometry.edges import edges
from geometry.vertices import vertices
from matplotlib import pyplot as plt
from tools import *

class mesh_generator:
    def __init__(self):
        self.ver = vertices()
        self.edg = edges()
        self.blk = blocks()
        self.bon = boundary()

    def check_geometry(self):
        pass

    def generate_file(self):
        pass

    def make_box(self):
        pass

    def add_point(self, x, y, z):
        if [x, y, z] in self.ver.list:
            print(f"Point {x, y, z} already in mesh!")
            return False
        self.ver.list.append([x,y,z])
        print(f"Add a new vertice: {self.ver.list[-1]}")

    def make_edge(self, pt1, pt2):
        ver_num = len(self.ver.list)
        if pt1 < ver_num and pt2 < ver_num:
            self.edg.list.append([pt1, pt2])
            print(f"Add a new edge: {self.edg.list[-1]}")
        else:
            print(f"Add edge failed, please check vertices number!")

    def make_face_from_vertices(self, pt1, pt2, pt3, pt4):
        ver_num = len(self.ver.list)
        pt_list = [pt1, pt2, pt3, pt4]
        pt_list_coor = [self.ver.list[pt1], self.ver.list[pt2], self.ver.list[pt3], self.ver.list[pt4]]
        if max(pt_list) < ver_num and self.check_face(pt_list_coor):
            self.bon.list.append(pt_list)
            print(f"Add a new face: {self.bon.list[-1]}")
        else:
            print(f"Add face failed, please check vertices number or intersections!")
            return
        
    def check_face(self, face):
        if len(face) <= 2:
            print("This is not a legal face!")
            return False
        if len(face) > 4:
            print(f"This face has too many edges: {len(face)}")
            return False
        if len(face) == 4:
            A, B, C, D = [0], face[1], face[2], face[3],
            if check_quadrilateral_intersections(A, B, C, D):
                print(f"Face {face} has intersections!")
                return False
        return True
            

if __name__ == "__main__":
    mesh = mesh_generator()
    mesh.add_point(0, 0, 0)
    mesh.add_point(0, 0, 1)
    mesh.add_point(0, 1, 0)
    mesh.add_point(0, 1, 1)
    mesh.make_edge(0,1)
    mesh.make_face_from_vertices(0,1,3,2)


