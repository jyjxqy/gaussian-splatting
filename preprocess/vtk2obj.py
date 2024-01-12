import pyvista as pv

def vtk2obj(file_path, output_path):
    mesh = pv.read(file_path)
    p = pv.Plotter()
    p.add_mesh(mesh)
    p.export_obj(output_path)
