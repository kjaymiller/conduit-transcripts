#!/bin/sh

services=$(avn service list --project devrel-jay --json | jq 'map({service_name, state, service_type, tags})')

getTagList() {
	echo $services | jq -r "map(select(.tags.application == \"$1\"))| .[].service_name"
}

poweronServices() {
	# Get the services that are not tagged
	for service in $(getTagList $1); do
		echo "Powering On $service"
		avn service update --power-on $service
	done
}

poweroffServices() {
	# Get the services that are not tagged
	for service in $(getTagList $1); do
		echo "Powering Off $service"
		avn service update --power-off $service
	done
}

if [[ "$1" -eq 1 ]]; then
	poweronServices "conduit-fastapi"
elif [[ "$1" -eq 0 ]]; then
	poweroffServices "conduit-fastapi"
else
	echo "Invalid Option"
fi
