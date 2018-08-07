# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    #'sphinx.ext.intersphinx',
    'openstackdocstheme',
    'yasfb',
]

html_theme = 'openstackdocs'

# openstackdocstheme options
repository_name = 'openstack/self-healing-sig'
bug_project = '917'
bug_tag = ''

# Feed configuration for yasfb
feed_base_url = 'http://specs.openstack.org/openstack/self-healing-sig'
feed_author = 'OpenStack Self-healing SIG'

exclude_patterns = [
    'specs/template.rst',
    'use-cases/template.rst',
]

# Optionally allow the use of sphinxcontrib.spelling to verify the
# spelling of the documents.
try:
    import sphinxcontrib.spelling
    extensions.append('sphinxcontrib.spelling')
except ImportError:
    pass

# autodoc generation is a bit aggressive and a nuisance when doing heavy
# text edit cycles.
# execute "export SPHINX_DEBUG=1" in your terminal to disable

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Self-healing SIG'
copyright = u'%s, OpenStack Foundation' % datetime.date.today().year

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://docs.python.org/': None}
