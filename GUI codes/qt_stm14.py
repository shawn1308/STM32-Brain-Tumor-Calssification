import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.Qt3DCore import QEntity, QTransform
from PyQt5.Qt3DExtras import Qt3DWindow, QFirstPersonCameraController, QDiffuseSpecularMaterial, QCuboidMesh

app = QApplication(sys.argv)

# Create a Qt3DWindow
view = Qt3DWindow()
view.defaultFrameGraph().setClearColor(Qt.white)
container = QWidget.createWindowContainer(view)
container.setMinimumSize(800, 600)

# Set up the 3D environment
scene = QEntity()
view.setRootEntity(scene)

# Add a camera
camera_entity = view.camera()
camera_entity.lens().setPerspectiveProjection(45.0, 16.0 / 9.0, 0.1, 1000.0)
camera_entity.setPosition(QVector3D(0, 0, 40))
camera_controller = QFirstPersonCameraController(scene)
camera_controller.setCamera(camera_entity)

# Add a cube
cube_entity = QEntity(scene)
cube_transform = QTransform()
cube_transform.setScale(2.0)
cube_entity.addComponent(cube_transform)
cube_mesh = QCuboidMesh()
cube_material = QDiffuseSpecularMaterial()
cube_entity.addComponent(cube_mesh)
cube_entity.addComponent(cube_material)

# Set up the layout
layout = QVBoxLayout()
layout.addWidget(container)

# Show the window
window = QWidget()
window.setLayout(layout)
window.show()

sys.exit(app.exec_())
