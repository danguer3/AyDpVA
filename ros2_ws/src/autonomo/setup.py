from setuptools import find_packages, setup

package_name = 'autonomo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ezechiel',
    maintainer_email='ezechiel@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = autonomo.publisher:main',
            'subscriber = autonomo.subscriber:main',
            'publisher1 = autonomo.publisher1:main',
            'subscriber1 = autonomo.subscriber1:main',
            'publisher_alarma = autonomo.publisher_alarma:main',
            'subscriber_alarma = autonomo.publisher_alarma:main'
        ],
    },
)
