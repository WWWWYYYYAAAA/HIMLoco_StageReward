from mujoco.urdf import URDFModel
model = URDFModel.load_from_urdf("./urdf/DOG.urdf")
model.save("zsl1.xml")