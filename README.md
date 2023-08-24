# Campus Study Spaces

This is a scalable web application for listing campus study spaces at Portland State University. The application supports the submission and viewership of application entries that are provided via a web form. 
Submission of entries supports fields that can hold attributes typically related to the application and are stored in a backend database in Google Cloud Platform. 

This application follows Python/Flask MVP web application using Cloud DataStore as a database backend supporting create and read operations.
The Containerized version of this application is uploaded to Docker Hub with Cloud Datastore database backend deployed on Cloud Run.

This application supports the following routes/views:

Route that implements the default landing page with links to other routes.
Route that allows one to view all entries previously submitted.
Route for creating/inserting a new entries via an HTML form.

# Code Base

Model.py : An abstract model class that supports individual fields with varying data types to support the application and that is documented via Docstrings including parameters and return values with their types.

model_datastore.py : A derived data model class that supports creation and reading of entries via a Cloud datastore database.

app.py :  listens on port 5000 when called directly from Python.

requirements.txt:  contains all packages required to run program
