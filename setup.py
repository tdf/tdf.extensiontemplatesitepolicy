from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='tdf.extensiontemplatesitepolicy',
      version=version,
      description="The policy package for the new LibreOffice extensions and templates website",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone Policy LibreOffice Extensions Templates Website',
      author='Andreas Mantke',
      author_email='maand@gmx.de',
      url='http://github.com/tdf/tdf.extensiontemplatesitepolicy',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['tdf', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.ATClamAV',
          'tdf.templateuploadcenter',
          'tdf.extensionsuploadcenter',
          'tdf.siteaccountrequest',
          'plone.api',
          'plone.app.dexterity [grok, relations]',
          'plone.multilingualbehavior',
          'plone.app.multilingual [archetypes]',
          'plone.app.multilingual [dexterity]',
      
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["templer.localcommands"],
      )
