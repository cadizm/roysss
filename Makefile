.PHONY: all deploy_local

all:
	echo "Targets: deploy_local"

deploy_local:
	ansible-playbook --limit=local plays/playbook.yml

deploy_remote:
	ansible-playbook --user=cadizm --limit=remote plays/playbook.yml

# note: requires python on remote host and will disable root login
adduser_cadizm_remote:
	ansible-playbook --user=root --limit=remote lib/ansible-provision/adduser-cadizm.yml
