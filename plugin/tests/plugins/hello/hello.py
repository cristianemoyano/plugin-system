from dataclasses import dataclass
from typing import Protocol


@dataclass
class HelloPlugin:

    class Meta:
        plugin_name: str = 'hello'
        plugin_uri: str = 'The home page of the plugin, which should be a unique URL, preferably on your own website.'
        plugin_description: str = 'A short description of the plugin'
        version: str = 'The current version number of the plugin, such as 1.0 or 1.0.3'
        author: str = 'The name of the plugin author. Multiple authors may be listed using commas.'
        license: str = 'The short name (slug) of the plugin’s license (e.g. GPLv2)'

    @staticmethod
    def register_activation_hook() -> None:
        print(f"register_activation_hook: {HelloPlugin.Meta.plugin_name}")

    @staticmethod
    def register_deactivation_hook() -> None:
        print(f"register_deactivation_hook: {HelloPlugin.Meta.plugin_name}")

    @staticmethod
    def register_uninstall_hook() -> None:
        print(f"register_uninstall_hook: {HelloPlugin.Meta.plugin_name}")

def register() -> Protocol:
    return HelloPlugin


def hello_callback(first_name, last_name) -> None:
    print(f'Hello, {first_name} {last_name}!')


def hello_callback_number_two() -> None:
    print('No arguments for this callback :(')


def hello_callback_number_three(**kwargs) -> None:
    print(f'New callback passing arguments kwargs: {kwargs}')


def add_actions():
    return [
        {
            'hook_name': 'init',
            'callback': hello_callback,
            'args': ['john', 'doe'],
            'priority': 10,
        },
        {
            'hook_name': 'init',
            'callback': hello_callback_number_two,
            'priority': 10,
        },
        {
            'hook_name': 'init',
            'callback': hello_callback_number_three,
            'args': {
                'arg1': 1,
                'arg2': 2,
                'arg3': 3,
            },
            'priority': 10,
        }
    ]
