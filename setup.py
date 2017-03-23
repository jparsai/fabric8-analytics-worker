#!/usr/bin/env python3
from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt') as fd:
        return fd.read().splitlines()


setup(
    name='cucoslib',
    version='0.2',
    scripts=[
        'hack/env.sh',
        'hack/workers.sh',
        'hack/worker-liveness.sh',
        'hack/worker-readiness.sh'
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=get_requirements(),
    author='Pavel Odvody',
    author_email='podvody@redhat.com',
    description='Bayesian workers & utilities',
    license='MIT',
    keywords='bayesian analysis worker',
    url='https://gitlab.cee.redhat.com/bayesian/worker'
)
