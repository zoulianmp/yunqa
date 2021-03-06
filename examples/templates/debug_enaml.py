#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
import enaml
from enaml.qt.qt_application import QtApplication


def main():
    with enaml.imports():
        from buttons import Main

    app = QtApplication()

    view = Main()
    view.show() 

    # Start the application event loop
    app.start()


if __name__ == "__main__":
   

    
    
    
    
    main()
