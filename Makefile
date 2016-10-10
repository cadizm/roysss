
.PHONY: all setup_local setup_remote deploy_local deploy_remote adduser_cadizm_remote letsencrypt_remote

all:
	@echo "See this Makefile for targets"

setup_local:
	ansible-playbook --limit=local plays/setup.yml

setup_remote:
	ansible-playbook --user=cadizm --limit=remote plays/setup.yml

deploy_local:
	ansible-playbook --limit=local plays/deploy.yml

deploy_remote:
	ansible-playbook --user=cadizm --limit=remote plays/deploy.yml

## One-time targets that should only be used in production

# note: requires python on remote host and will disable root login
adduser_cadizm_remote:
	ansible-playbook --user=root --limit=remote lib/ansible-provision/adduser-cadizm.yml

letsencrypt_remote:
	ansible-playbook --user=cadizm --limit=remote plays/enable-ssl.yml
