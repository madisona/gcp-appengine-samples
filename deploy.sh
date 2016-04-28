
gcloud config set project "imtapps-testing-stuff"

gcloud preview app deploy -q app.yaml --no-promote

gcloud config unset project
