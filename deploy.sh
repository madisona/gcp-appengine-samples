
gcloud config set project "imtapps-testing-stuff"

gcloud preview app deploy -q app.yaml --no-promote

gcloud config unset project


# https://cloud.google.com/python/django/flexible-environment
#
# Deploy the app to the App Engine flexible environment
#
# When the app is deployed to Cloud Platform, it uses the Gunicorn server. Gunicorn doesn't serve static content, so the app uses Google Cloud Storage to serve static content.
#
# Create a Cloud Storage bucket and make it publicly readable. Replace <your-gcs-bucket> with a bucket name of your choice. For example, you could use your project ID as a bucket name:
#
# $ gsutil mb gs://<your-gcs-bucket>
# $ gsutil defacl set public-read gs://<your-gcs-bucket>
# Gather all the static content locally into one folder:
#
# $ python manage.py collectstatic
# Upload the static content to CloudStorage:
#
# $ gsutil rsync -R static/ gs://<your-gcs-bucket>/static
# In mysite/settings.py, set the value of STATIC_URL to this URL:
#
# http://storage.googleapis.com/<your-gcs-bucket>/static/
# Enter this command to deploy the sample:
#
# $ gcloud preview app deploy
# Wait for the message that notifies you that the update has completed.
