#!/usr/bin/python
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )
import ast
import os

from setuptools import setup, find_packages


class VersionFinder(ast.NodeVisitor):
    def __init__(self):
        self.version = None

    def visit_Assign(self, node):
        if getattr(node.targets[0], 'id', None) == '__version__':
            self.version = node.value.s


with open(os.path.join('suds', '__init__.py')) as open_file:
    finder = VersionFinder()
    finder.visit(ast.parse(open_file.read()))


setup(
    name="suds-ng",
    version=finder.version,
    description="Lightweight SOAP client - fork of suds",
    author="Felix Yan",
    author_email="felixonmars@gmail.com",
    maintainer="Felix Yan",
    maintainer_email="felixonmars@gmail.com",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        "six"
    ],
    url="https://github.com/felixonmars/suds-ng",
)
