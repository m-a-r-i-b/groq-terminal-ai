from setuptools import setup, find_packages

setup(
    name='terminal-ai',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ai=terminal_ai.cli:main',
        ],
    },
    install_requires=[
        'pyautogui',
        'langchain-openai',
    ],
)
