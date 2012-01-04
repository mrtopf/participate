from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='participate',
      version=version,
      description="a tool for fostering citizen partizipation in the political process",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='COM.lounge GmbH',
      author_email='info@comlounge.net',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "userbase",
        "starflyer",
        "colander",
        "wtforms",
      ],
      entry_points="""
        [starflyer.config]
        default = participate.setup:setup
        userbase = participate.setup:um_setup
        [paste.app_factory]
        main = starflyer:run
      """,
      )
