import gmic

carlo_filename = "carlo-acutis-isolated-face-for-warhol.jpg"
carlo_gmic_images = []
gmic.run("{} resize2dx 1000 display".format(carlo_filename), carlo_gmic_images)
carlo_w, carlo_h = carlo_gmic_images[0]._width, carlo_gmic_images[0]._height

warhol_cmd = "warhol 5,5,0.47,37.92 display output carlo-warhol.png"
gmic.run(warhol_cmd, carlo_gmic_images)
