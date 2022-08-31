from dataclasses import dataclass
from typing import Any, Protocol
import logging

logger: logging.Logger = logging.getLogger(__name__)


@dataclass
class PrinterPlugin:

    class Meta:
        plugin_name: str = 'printer'
        plugin_uri: str = 'The home page of the plugin, which should be a unique URL, preferably on your own website.'
        plugin_description: str = 'A short description of the plugin'
        version: str = 'The current version number of the plugin, such as 1.0 or 1.0.3'
        author: str = 'The name of the plugin author. Multiple authors may be listed using commas.'
        license: str = 'The short name (slug) of the plugin’s license (e.g. GPLv2)'

    @staticmethod
    def register_activation_hook() -> None:
        logger.debug(f"register_activation_hook: {PrinterPlugin.Meta.plugin_name}")

    @staticmethod
    def register_deactivation_hook() -> None:
        logger.debug(f"register_deactivation_hook: {PrinterPlugin.Meta.plugin_name}")

    @staticmethod
    def register_uninstall_hook() -> None:
        logger.debug(f"register_uninstall_hook: {PrinterPlugin.Meta.plugin_name}")


def register() -> Protocol:
    return PrinterPlugin


def printer_callback() -> None:
    logger.info(f'I am a printer!')



def add_actions() -> list[dict[str, Any]]:
    return [
        {
            'hook_name': 'init',
            'callback': printer_callback,
            'priority': 10,
        },
    ]
