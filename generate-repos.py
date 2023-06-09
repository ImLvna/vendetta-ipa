import json
from datetime import datetime
import os

altsource = {
    "name": "Vendetta",
    "identifier": "dev.beefers.vendetta",
    "description": "A mod for Discord",
    "iconURL": "https://avatars.githubusercontent.com/u/112445065?s=500",
    "website": "https://discord.gg/n9QQ4XhhJP",
    "tintColor": "#3ab8ba",
    "featuredApps": [
        "dev.beefers.vendetta"
    ],
    "apps": [
        {
            "name": "Vendetta",
            "bundleIdentifier": "dev.beefers.vendetta",
            "developerName": "Beef",
            "subtitle": "WARNING: ALTSTORE DOES NOT WORK WITH VENDETTA",
            "localizedDescription": "WARNING: ALTSTORE DOES NOT WORK WITH VENDETTA\n\n\nA mod for Discord",
            "iconURL": "https://avatars.githubusercontent.com/u/112445065?s=500",
            "tintColor": "#3ab8ba",
            "version": f"0.0.{os.environ.get('NUMBER')}",
            "versionDate": datetime.now().isoformat(),
            "size": os.path.getsize("pages/Vendetta.ipa"),
            "versionDescription": f"{os.environ.get('DESCRIPTION')} - {os.environ.get('COMMIT')[:7]}",
            "downloadURL": "https://imlvna.github.io/vendetta-ipa/Vendetta.ipa",
            "beta": False,

            "appPermissions": {
                "entitlements": [
                    {'name': 'com.apple.security.application-groups'},
                    {'name': 'com.apple.developer.associated-domains'},
                    {'name': 'beta-reports-active'},
                    {'name': 'com.apple.developer.storekit.request-data'},
                    {'name': 'get-task-allow'},
                    {'name': 'aps-environment'}
                ],
                "privacy": [
                    {'name': 'BluetoothAlways', 'usageDescription': 'Discord uses Bluetooth to connect to other devices.'},
                    {'name': 'BluetoothPeripheral', 'usageDescription': 'Discord uses Bluetooth to connect to other devices.'},
                    {'name': 'Camera', 'usageDescription': 'You can take photos and videos inside Discord.'},
                    {'name': 'Contacts', 'usageDescription': 'Discord can access your contacts to help you find friends.'},
                    {'name': 'LocalNetwork', 'usageDescription': 'Discord uses your local network to connect to other devices.'},
                    {'name': 'LocationAlwaysAndWhenInUse', 'usageDescription': 'Discord uses your location to help you find friends.'},
                    {'name': 'LocationWhenInUse', 'usageDescription': 'Discord uses your location to help you find friends.'},
                    {'name': 'LocationAlways', 'usageDescription': 'Discord uses your location to help you find friends.'},
                    {'name': 'Microphone', 'usageDescription': 'You can record audio messages inside Discord.'},
                    {'name': 'PhotoLibraryAdd', 'usageDescription': 'You can save photos and videos inside Discord.'},
                    {'name': 'PhotoLibrary', 'usageDescription': 'You can send photos and videos inside Discord.'}
                ]
            }
        }
    ]
}

with open("pages/altstore.json", "w", encoding='utf-8') as source_file:
    json.dump(altsource, source_file, indent=4)


scarletrepo = {
    "META": {
        "repoName": "Vendetta",
        "repoIcon": "https://avatars.githubusercontent.com/u/112445065?s=500"
    },
    "Tweaked": [
        {
            "name": "Vendetta",
            "version": os.environ.get('COMMIT')[:7],
            "changelog": os.environ.get('DESCRIPTION'),
            "down": "https://imlvna.github.io/vendetta-ipa/Vendetta.ipa",
            "category": "Tweaked Apps",
            "description": "A mod for Discord",
            "bundleID": "dev.beefers.vendetta",
            "appstore": "com.hammerandchisel.discord",
            "icon": "https://avatars.githubusercontent.com/u/112445065?s=500",
            "contact": {
                "discord": "https://discord.gg/n9QQ4XhhJP",
            }
        }
    ]
}

with open("pages/scarlet.json", "w", encoding='utf-8') as source_file:
    json.dump(scarletrepo, source_file, indent=4)