#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from enaml.workbench.workbench import Workbench


WORKFLOW_PLUGIN = u'enaml.workbench.workflow'


class WorkflowWorkbench(Workbench):
    """ A class for creating workbench UI applications.

    The UIWorkbench class is a subclass of Workbench which loads the
    builtin ui plugin and provides an entry point to start the main
    application event loop.

    """
    def run(self):
        """ Run the UI workbench application.

        This method will load the core and ui plugins and start the
        main application event loop. This is a blocking call which
        will return when the application event loop exits.

        """
        import enaml
        with enaml.imports():
            from enaml.workbench.core.core_manifest import CoreManifest
            from workflow.workflow_manifest import WorkflowManifest

        self.register(CoreManifest())
        self.register(WorkflowManifest())

        workflow = self.get_plugin(WORKFLOW_PLUGIN)
        workflow.show_window()
        workflow.start_application()

        # TODO stop all plugins on app exit?

        self.unregister(WORKFLOW_PLUGIN)
