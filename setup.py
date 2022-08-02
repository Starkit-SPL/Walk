from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nao',
    maintainer_email='nao@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'talker = py_pubsub.publisher_member_function:main',
             'listener = py_pubsub.subscriber_member_function:main',
             'action = py_pubsub.action:main',
             'stiffness_to_zero = py_pubsub.stiffness_to_zero:main',
             'walk_forward = py_pubsub.walk_forward:main'
        ],
    },
)
