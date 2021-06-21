from setuptools import setup

APP = ['config.py']
DATA_FILES = ["Textify_logo.png"]
OPTIONS = {
        'argv_emulation': True,
        "iconfile": "Textify_logo.icns"
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)