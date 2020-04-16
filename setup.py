from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='cbt',
      version='0.1',
      description='Pace Compatible Packaging of Cichlid Bower Tracker',
      long_description=readme(),
      url='http://github.com/tlancaster6/cbt',
      author='Tucker Lancaster',
      author_email='tlancaster6@gatech.edu',
      license='MIT',
      packages=['cbt'],
      install_requires=['pandas', 'numpy', 'fabric', 'matplotlib', 'seaborn'],
      include_package_data=True,
      zip_safe=False
      )

