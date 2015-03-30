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
from workflow.api import WorkflowWorkbench


if __name__ == '__main__':
    

    
    from workflow.api import update_iconpath
    
    #Set the workflow icons path
    update_iconpath(__file__)
    
    
    import enaml
    with enaml.imports():
        from sample_plugin import SampleManifest
#        from enaml.workbench.core.core_manifest import CoreManifest
#        from workflow.workflow_manifest import WorkflowManifest

    workbench = WorkflowWorkbench()
    workbench.register(SampleManifest())
    
#    workbench.register(CoreManifest())
#    
#    workbench.register(WorkflowManifest())
#    
#    
    
    
    
#    af = get_worknodes_naviagate_parameters(workbench)
    
    
    
    
    workbench.run()
