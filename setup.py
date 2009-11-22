try:
    from distribute_setup import use_setuptools
except ImportError:
    pass
else:
    use_setuptools()

from setuptools import setup, find_packages

setup(name="rtutor",
        packages=find_packages(),
        install_requires=[
            'django',
        ],
        extras_require={
            'FastCGI': ['flup'],
        },
)

