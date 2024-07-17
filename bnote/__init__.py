"""
 bnote project
 Author : Eurobraille
 Date : 2024-07-16
 Licence : Ce fichier est libre de droit. Vous pouvez le modifier et le redistribuer à votre guise.
"""
'''
 Major version. Minor version. Fix version
 Developper version is allways followed by the stage : -bn, -an, -rcn (0 <= n <= 99)
 All release version lost the developper version's extension
 Example : 1.0.0a0 < 1.0.0a1 < 1.0.0a8 < 1.0.0b1 < 1.0.0b2 < 1.0.0b11 < 1.0.0rc1 < 1.0.0
 Version in anothers forms are not tolerate !
 '''

from bnote.tools.yaupdater import YAUpdater

__version__ = YAUpdater.get_version_from_running_project("pyproject.toml")
