from setuptools import setup

package_name = 'temperature_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ines',
    maintainer_email='ines@example.com',
    description='Temperature publisher node',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_node = temperature_publisher.temperature_node:main',
        ],
    },
)
