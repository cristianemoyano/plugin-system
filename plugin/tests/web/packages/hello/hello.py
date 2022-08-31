from dataclasses import dataclass
from typing import Protocol


@dataclass
class HelloPlugin:

    class Meta:
        plugin_name: str = 'hello'
        plugin_uri: str = 'N/A'
        plugin_description: str = 'Hello World Plugin'
        version: str = '1.0.0'
        author: str = 'cmoyano'
        license: str = 'N/A'

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
