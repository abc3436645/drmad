from setuptools import setup

setup(
      name='funkyyak',
      version='1.1.3',
      description='Efficiently computes derivatives of numpy code.',
      author='Dougal Maclaurin and David Duvenaud and Matthew Johnson',
      author_email="maclaurin@physics.harvard.edu, dduvenaud@seas.harvard.edu, mattjj@csail.mit.edu",
      packages=['funkyyak'],
      install_requires=['numpy>=1.9', 'future'],
      setup_requires=['numpy>=1.9'],
      keywords=['Automatic differentiation', 'backpropagation', 'gradients',
                'machine learning', 'optimization', 'neural networks',
                'Python', 'Numpy', 'Scipy'],
      url='https://github.com/HIPS/autograd',
      license='MIT',
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4'],
)
