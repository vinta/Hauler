include:
  - common.build

gevent-libs-packages:
  pkg.installed:
    - names:
      - libevent-dev
    - require:
      - pkg: build-packages
