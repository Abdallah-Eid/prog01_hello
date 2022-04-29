import vtk


def main():
    # This creates a polygonal cylinder model with eight circumferential facets
    # (i.e, in practice an octagonal prism).
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)

    # The mapper is responsible for pushing the geometry into the graphics library.
    # It may also do color mapping, if scalars or other attributes are defined.
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it around the X and Y axes.
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor([1.000, 0.3882, 0.2784])
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)

    # The renderer generates the image
    # which is then displayed on the render window.
    # It can be thought of as a scene to which the actor is added
    renderer = vtk.vtkRenderer()
    renderer.AddActor(cylinderActor)
    renderer.SetBackground([0.1, 0.2, 0.4])
    # Zoom in a little by accessing the camera and invoking its "Zoom" method.
    renderer.ResetCamera()
    renderer.GetActiveCamera().Zoom(1.5)

    # The render window is the actual GUI window
    # that appears on the computer screen
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(200, 200)
    renderWindow.AddRenderer(renderer)

    # The render window interactor captures mouse events
    # and will perform appropriate camera or actor manipulation
    # depending on the nature of the events.
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # enter the rendering loop
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == "__main__":
    main()
