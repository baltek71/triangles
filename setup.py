from setuptools import setup, find_packages


setup(
    name='triangles',
    version='0.0.9',
    py_modules=['triangles'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['triangles=triangles.triangles:main']
    },
)