postgresql
==========

Add Postgresql official Apt repo, optionally install and configure
client and/or server. (Server not yet implemented.) By default, only
the repo is added; see _Role Variables_.

Requirements
------------

An installed Ubuntu server. 

Role Variables
--------------

Do or do not install the Postgresql client, server. Not that by
default we only add the apt.postgresql.org repo.

    postgresql_install_client: no
    postgresql_install_server: no

Version of Postgresql

    postgresql_version: 9.6

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: dbservers
      tasks:
        - import_role:
            name: postgresql
          vars:
            postgresql_install_client: yes
            postgresql_install_client: no
