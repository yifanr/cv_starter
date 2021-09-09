import numpy as np
import trimesh
import random
import pyglet
import h5py

def save_h5(h5_filename, data, label, data_dtype='uint8', label_dtype='uint8'):
    h5_fout = h5py.File(h5_filename)
    h5_fout.create_dataset(
            'data', data=data,
            compression='gzip', compression_opts=4,
            dtype=data_dtype)
    h5_fout.create_dataset(
            'label', data=label,
            compression='gzip', compression_opts=1,
            dtype=label_dtype)
    h5_fout.close()
for i in range(32):
    data = 1
    labels = np.array([0,1,2,3]*16)
    isFirst = True
    for j in range(16):
        rand = random.random()*10+1
        distort = rand * (random.random()*2 + .2)
        cylinder = trimesh.creation.cylinder(rand, height=distort, sections=320, segment=None, transform=None)
        cone = trimesh.creation.cone(rand, height=distort, sections=640, transform=None)
        annulus = trimesh.creation.annulus(rand, rand*(1.1+random.random()), height=distort, sections=160, transform=None, segment=None)
        sphere = trimesh.creation.icosphere(subdivisions=3, radius=1.0, color=None)
        cylinder.show()
        cone.show()
        annulus.show()
        sphere.show()
        if(isFirst):
            isFirst = False
            data = np.array([cylinder.sample(512), cone.sample(512), annulus.sample(512), sphere.sample(512)])
        else:
            data = np.concatenate((data,np.array([cylinder.sample(512), cone.sample(512), annulus.sample(512), sphere.sample(512)])),axis=0)
    #save_h5('data/file'+str(i)+'.hdf5', data, labels)
for i in range(16):
    data = 1
    labels = np.array([0,1,2,3]*16)
    isFirst = True
    for j in range(16):
        rand = random.random()*10+1
        distort = rand * (random.random()*2 + .2)
        cylinder = trimesh.creation.cylinder(rand, height=distort, sections=320, segment=None, transform=None)
        cone = trimesh.creation.cone(rand, height=distort, sections=640, transform=None)
        annulus = trimesh.creation.annulus(rand, rand*(1.1+random.random()), height=distort, sections=160, transform=None, segment=None)
        sphere = trimesh.creation.icosphere(subdivisions=3, radius=1.0, color=None)
        if(isFirst):
            isFirst = False
            data = np.array([cylinder.sample(512), cone.sample(512), annulus.sample(512), sphere.sample(512)])
        else:
            data = np.concatenate((data,[cylinder.sample(512), cone.sample(512), annulus.sample(512), sphere.sample(512)]),axis=0)
    #save_h5('test/file'+str(i)+'.hdf5', data, labels)
