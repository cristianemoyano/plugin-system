from dataclasses import dataclass
from typing import Any, Protocol
import logging

logger: logging.Logger = logging.getLogger(__name__)


@dataclass
class PrinterPlugin:

    class Meta:
        plugin_name: str = 'printer'
        plugin_uri: str = 'N/A'
        plugin_description: str = 'Printer Plugin'
        version: str = '1.0.0'
        author: str = 'cmoyano'
        license: str = 'N/A'

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
