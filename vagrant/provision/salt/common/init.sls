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

en_US.UTF-8:
  locale.system

terminal-packages:
  pkg.installed:
    - names:
      - curl
      - htop
      - mosh
      - screen
      - vim
