"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- head (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
head_width = 4
head_height = 6
head_depth = 4
head_x = 0
head_z = 0

head = cmds.polyCube(
    name="head_01",
    width=head_width,
    height=head_height,
    depth=head_depth,
)[0]
#  Raise the head so its base sits on the ground plane at the origin
cmds.move(head_x, head_height / 2.0, head_z, head)

# ---------------------------------------------------------------------------
# TODO: Add Object 2 - bottom of hat (cone)
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
bottom_of_hat_radius = 5
bottom_of_hat_height = 3
#size of the bottom of hat
bottom_of_hat_x = head_x
bottom_of_hat_y = head_height + bottom_of_hat_height / 2.0
bottom_of_hat_z = head_z
#make the bottom of hat match the house 

bottom_of_hat = cmds.polyCone(
    name="bottom_of_hat_02",
    height=bottom_of_hat_height,
    radius=bottom_of_hat_radius,
)[0]

cmds.move(bottom_of_hat_x, bottom_of_hat_y, bottom_of_hat_z, bottom_of_hat)
# ---------------------------------------------------------------------------
# TODO: Add Object 3 - eye/left eye (sphere) 
# ---------------------------------------------------------------------------
eyes_radius = 0.3
#tells us the size of the eyes
eye_y = head_height = 6
eye_z_offset = head_depth / 2 + 0.01 
# Left eye
left_eye_x = head_width/ 5
#make the eye match the head
left_eye = cmds.polySphere(
    name="left_eye_04",
     #renaming the cone as left eye_04
     radius=eyes_radius
    #show how tall the left eye is 
)[0]
cmds.move(left_eye_x, head_height/2, head_z + eye_z_offset, left_eye)
 #makes sure the right eye is postioned correctly on the head 
# ---------------------------------------------------------------------------
# TODO: Add Object 4 - right eye (sphere) 
# ---------------------------------------------------------------------------
# Right eye
right_eye_x = -head_width / 5 
#make the eye match the head
right_eye = cmds.polySphere(
    name="right_eye_05",
     #renaming the cone as right eye_05
     radius=eyes_radius
    #show how tall the left eye is 
)[0]
cmds.move(right_eye_x, head_height/2, head_z + eye_z_offset, right_eye)
  #makes sure the left eye is postioned correctly on the head 
# ---------------------------------------------------------------------------
# TODO: Add Object 5 - top of hat (cone)
# ---------------------------------------------------------------------------
top_of_hat_radius = 2
top_of_hat_height = 10
#tells us the size of the top of hat
top_of_hat_x = head_x
top_of_hat_y = bottom_of_hat_height + bottom_of_hat_height + top_of_hat_height / 2
top_of_hat_z = head_z
#make the top of hat match the head

top_of_hat = cmds.polyCone(
    name="top_of_hat_03",
     #renaming the cone as roof 
   height=top_of_hat_height,
    radius=top_of_hat_radius
    #how tall the top of hat is
)[0]
cmds.move(top_of_hat_x, top_of_hat_y, top_of_hat_z, top_of_hat)
  #makes sure the parts of the hat are placed correctly on top of tha head
# ---------------------------------------------------------------------------
# TODO (Optional): - mouth (cube) Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------
mouth_width = 2
mouth_height = 0.5
mouth_depth = 0.2
#tells us the size of the mouth
mouth_x = head_x
mouth_y = head_height = 1
mouth_z = head_z = 2
#make the mouth match the head

mouth = cmds.polyCube(
    name="mouth_06",
     #renaming the cube as the mouth
   width=mouth_width,
    height=mouth_height,
    depth=mouth_depth
    #how tall the mouth is
)[0] 
cmds.move(mouth_x, mouth_y, mouth_z, mouth)
  #makes sure the mouth is plced correctly on the head
# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
