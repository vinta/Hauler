include:
  - common.build

python-packages:
  pkg.installed:
    - names:
      - python
      - python-dev
      - python-setuptools
      - python-pip
      - python-virtualenv
      - virtualenvwrapper
    - require:
      - pkg: build-packages
