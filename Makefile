.PHONY: all deploy_local deploy_remote adduser_cadizm_remote

all:
	@echo "Targets:\n\tdeploy_local\n\tdeploy_remote\n\tadduser_cadizm_remote\n\tletsencrypt_remote"

deploy_local:
	ansible-playbook --limit=local plays/playbook.yml

deploy_remote:
	ansible-playbook --user=cadizm --limit=remote plays/playbook.yml

# note: requires python on remote host and will disable root login
adduser_cadizm_remote:
	ansible-playbook --user=root --limit=remote lib/ansible-provision/adduser-cadizm.yml

letsencrypt_remote:
	ansible-playbook --user=cadizm --limit=remote plays/enable-ssl.yml
