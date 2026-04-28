from setuptools import find_packages, setup

setup(
    name='calcule_node',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/calcule_node']),
        ('share/calcule_node', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'calcule_server = calcule_node.calcule_server:main',
        ],
    },
)
