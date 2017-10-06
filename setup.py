'''
Copyright (c) 2017-2027 Dayong Gu
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from setuptools import setup, find_packages
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()
setup(
    name = "pyDataAnalyzer",
    version = "1.0.0",
    author = "Dayong Gu",
    author_email="gudayong@gmail.com",
    maintainer = "Dayong Gu",
    maintainer_email = "gudayong@gmail.com",
    description = ("Python tool for data analysis over csv as raw data source"),
    long_description = long_description,
    license = "GPLv3",
    keywords = "python data analyzer pyDataAnalyzer report visualization",
    url = "https://github.com/Dayonggu/pyDataAnalyzer",
    #packages=['pydataanalyzer'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    #package_dir={'pydataanalyzer'},
    #package_data = {'pydataanalyzer': ['test.nmon']},
    entry_points={
        "console_scripts": [
            "pyDataAnalyzer=pydataanalyzer:main",
        ]}
)
