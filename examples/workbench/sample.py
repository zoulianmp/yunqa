#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
""" A simple example plugin application.

This example serves to demostrates the concepts described the accompanying
developer crash source document.

"""
from enaml.workbench.ui.api import UIWorkbench


if __name__ == '__main__':
    import enaml
    with enaml.imports():
        from sample_plugin import SampleManifest
        from enaml.workbench.core.core_manifest import CoreManifest
        from enaml.workbench.ui.ui_manifest import UIManifest

    workbench = UIWorkbench()
    workbench.register(CoreManifest())
    workbench.register(UIManifest())


    
    workbench.get_extension_points()
    
    brand = workbench.get_extension_point('branding')
    print brand.id
    
    workbench.get_plugin('enaml.workbench.ui')
    
    workbench.register(SampleManifest())
   # workbench.run()
