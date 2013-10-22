Asia/Taipei:
  timezone.system:
    - utc: True
    - order: 1

create-user:
  user.present:
    - name: {{ pillar['system']['user'] }}
    - home: {{ pillar['system']['home_path'] }}
    - shell: /bin/bash
    - order: 2

sudoer-file:
  file.managed:
    - template: jinja
    - name: "/etc/sudoers.d/{{ pillar['system']['user'] }}"
    - source: salt://common/sudoers.template
    - user: root
    - group: root
    - mode: 0440

en_US.UTF-8:
  locale.system
