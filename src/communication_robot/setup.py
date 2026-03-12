from setuptools import setup

package_name = 'mon_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=['communication_robot'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ines Zani',
    maintainer_email='ines@email.com',
    description='Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_node = mon_package.hello_node:main',
            'temperature_node = mon_package.temp_node:main',  # <- ton nouveau node
        ],
    },
)
