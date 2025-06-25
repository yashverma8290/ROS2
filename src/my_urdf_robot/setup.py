from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_urdf_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yash-verma',
    maintainer_email='vermayash3205@gmail.com',
    description='Minimal URDF robot for ROS 2 Jazzy',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

