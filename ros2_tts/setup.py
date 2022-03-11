from setuptools import setup

package_name = 'ros2_tts'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'pyttsx3'
        ],
    zip_safe=True,
    maintainer='andy',
    maintainer_email='Andrew@Ealovega.dev',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tts_service_node = ros2_tts:main'
        ],
    },
)
