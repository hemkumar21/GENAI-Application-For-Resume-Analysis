from setuptools import setup, find_packages

setup(
    name='resume_summarizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'PyPDF2',
        'python-decouple',
    ],
    entry_points={
        'console_scripts': [
            'summarize-resume=resume_summarizer.main:main',
        ],
    },
)
