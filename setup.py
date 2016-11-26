from distutils.core import setup


DESCRIPTION = 'macOS cleaning utility'
LONG_DESCRIPTION = 'Command-line program help find 3rd party software running on macOS'


setup(
    name='Scourgify',
    version='0.1dev',
    packages=['scourgify',],
    package_data={'scourgify': ['wl.txt']},
    install_requires=[
          'psutil',
      ],
    scripts=['bin/scourgify'],
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
)
