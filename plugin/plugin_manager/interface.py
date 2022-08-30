from typing import Protocol


class PluginInterface(Protocol):
    """Basic representation of a plugin."""

    class Meta:
        # Required
        plugin_name: str = 'The name of your plugin'
        # Optional
        plugin_uri: str = 'The home page of the plugin, which should be a unique URL, preferably on your own website.'
        plugin_description: str = 'A short description of the plugin'
        version: str = 'The current version number of the plugin, such as 1.0 or 1.0.3'
        author: str = 'The name of the plugin author. Multiple authors may be listed using commas.'
        license: str = 'The short name (slug) of the plugin’s license (e.g. GPLv2)'

    @staticmethod
    def register_activation_hook() -> None:
        """
        On activation, plugins can run a custom routine.
        """
        pass

    @staticmethod
    def register_deactivation_hook() -> None:
        """
        On deactivation, plugins can run a routine to remove temporary data such as cache and temp files and directories.
        """
        pass

    @staticmethod
    def register_uninstall_hook() -> None:
        pass
