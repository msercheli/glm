# -*- coding: utf-8 -*-

name = 'glm'

version = '0.9.9.4'

description = \
    """
    OpenGL Mathematics
    """
authors = ['Christophe Groouvonet']

def commands():
    #env.PYTHONPATH.append("{root}/python")
    #env.PATH.append("{root}/bin/{system.platform}")
    env.REZ_GLM_INCLUDE_PATH = "{root}/include"

uuid = 'repository.glm'
