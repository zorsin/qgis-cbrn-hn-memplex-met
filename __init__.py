# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CBRNHNMemplexMET
                                 A QGIS plugin
 This plugin add the Memplex MET as layers
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-06-10
        copyright            : (C) 2022 by Sören Wirries
        email                : soeren@swirries.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CBRNHNMemplexMET class from file CBRNHNMemplexMET.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cbrn_hn_memplex_met import CBRNHNMemplexMET
    return CBRNHNMemplexMET(iface)
