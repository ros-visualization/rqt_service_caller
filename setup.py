from setuptools import setup

package_name = 'rqt_service_caller'

setup(
    name=package_name,
    version='1.2.1',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource',
            ['resource/ServiceCaller.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dorian Scholz',
    maintainer='Brandon Ong',
    maintainer_email='brandon@openrobotics.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'rqt_service_caller provides a GUI plugin for calling arbitrary services.'
    ),
    license='BSD',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'rqt_service_caller = ' + package_name + '.main:main',
        ],
    },
)
