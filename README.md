# link_sun_to_sky
A blender script to set up drivers for a sky texture.

# Usage
 - open the Python script in Blender's text editor
 - check what it will do and modify parameters by hand (a proper interface is in the TODO list)
 - run the script either by pressing alp+p or clicking on run
 - it will search the active scene for a sun lamp
  - the active and selected objects are checked first
 - then it adds a sky texture and normal node to the world shader
  - this can be modified: the script can instead search for an existing node and use that
  - pre-existing drivers are overwritten without questions, when using an existing node instead of creating a new one

# License
Do whatever you want with it, but it'd be nice if you gave credit.
I claim no responsibility for any damage this software might cause.
