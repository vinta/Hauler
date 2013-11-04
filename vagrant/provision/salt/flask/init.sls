include:
  - python
  - python.lxml

project-virtualenv:
  virtualenv.manage:
    - name: {{ pillar['project']['virtualenv_path'] }}
    - system_site_packages: False
    - pip: True
    - runas: {{ pillar['system']['user'] }}
    - require:
      - pkg: python-packages

project-virtualenv-postactivate:
  file.managed:
    - template: jinja
    - name: {{ pillar['project']['virtualenv_path'] }}/bin/postactivate
    - source: salt://flask/postactivate
    - user: {{ pillar['system']['user'] }}
    - group: {{ pillar['system']['user'] }}
    - mode: 0775
    - require:
      - virtualenv: project-virtualenv

project-pip-requirements:
  pip.installed:
    - bin_env: {{ pillar['project']['virtualenv_path'] }}
    - requirements: {{ pillar['project']['repo_path'] }}/requirements.txt
    - user: {{ pillar['system']['user'] }}
    - require:
      - virtualenv: project-virtualenv
      - pkg: lxml-libs-packages
