# Import Rollout SDK
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag
from rox.server.flags.rox_variant import RoxVariant


# Create Roxflags in the Flags container class
class Flags:
    def __init__(self):
        #Define the feature flags
        self.enableTutorial = RoxFlag(False)
        self.titleColors = RoxVariant('White', ['White', 'Blue', 'Green', 'Yellow'])
        self.myName = RoxVariant('Michelle', ['Michelle', 'Summer', 'Ryan'])
        #self.skoFlag = RoxVariant('SKO', ['SKO', 'Jenkins World', 'DevOps World'])

flags = Flags()

# Register the flags container with Rollout
Rox.register("default", flags)

# Setup the Rollout environment key
cancel_event = Rox.setup("5e4ed14eff09bf3a750ddf20").result();

# Boolean flag example
print('enableTutorial is %s' % flags.enableTutorial.is_enabled())

# Multivariate flag example
print('color is %s' % flags.titleColors.get_value())

# Multivariate name flag example
print('This was made by %s' % flags.myName.get_value())

# sko flag example
# print('My favorite CloudBees event is %s' % flags.skoFlag.get_value())
