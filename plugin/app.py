"""
Basic example showing how to create objects from data using a dynamic factory with
register/unregister methods.
"""

import json

from plugin_manager import functions, loader


def main() -> None:
    """example app"""

    # read data from a JSON file
    with open("./settings.json") as file:
        data = json.load(file)
        # load the plugins
        loader.load_plugins(data["plugins"])

    functions.activate('printer')
    functions.activate('printer')
    functions.activate('hello')

    functions.do_action(functions.AppHooks.INIT_APP)

    functions.desactivate('hello')
    functions.desactivate('hello')

    functions.do_action(functions.AppHooks.INIT_APP)

if __name__ == "__main__":
    main()
