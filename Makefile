.PHONY: all deploy_local

all:
	echo "Targets: deploy_local"

deploy_local:
	ansible-playbook plays/playbook.yml
