
gcloud config set project "imtapps-testing-stuff"

gcloud preview app deploy -q app.yaml

gcloud config unset project
