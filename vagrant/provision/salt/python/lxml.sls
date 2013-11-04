include:
  - common.build

lxml-libs-packages:
  pkg.installed:
    - names:
      - libxml2-dev
      - libxslt1-dev
    - require:
      - pkg: build-packages
