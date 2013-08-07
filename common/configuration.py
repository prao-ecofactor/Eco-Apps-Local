# This module will read and merge the appropriate configuration files.
# It expects a default.conf to exist in the same directory as the main script.
# Optionally, there can be an environment.conf file, which can overwrite various values as required by specific deployment environments
# By default, defaults.conf will contain values pertinent to a DEVELOPER'S environment.

import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('/usr/local/opt/conf/default.conf'))
config.read('/usr/local/opt/environment.conf')
config.read('/usr/local/opt/message.properties')
