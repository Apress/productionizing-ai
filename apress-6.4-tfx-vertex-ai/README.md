# apress-6.4-tfx-vertex-ai
source code for Productionizing AI - Chapter 6 Section 4 AutoAI Tools &amp; Platforms

TFX Pipeline for Vertex AI Pipelines: Hands-on Practise

AUTODL WITH TFX, KERAS AND VERTEX AI

This lab is based on the TensorFlow tutorial https://www.tensorflow.org/tfx/tutorials/tfx/gcp/vertex_pipelines_simple - the goal is to use Google Cloud Vertex Pipelines to automate a TFX pipeline to optimally train a deep learning model

1.	Activate your free trial on GCP by pressing the blue ACTIVATE button in the top right if you have not already done so. You will need to enter credit card details to activate the $300 of free GCP credit over 3 months – take care to monitor usage in your Google Cloud Portal  although Google claim they won’t auto-charge when credit limits are exhausted. 

2.	After activating your free trial, go back to the Create a Vertex AI dashboard https://console.cloud.google.com/vertex-ai and create a project. Make note of your project ID.

3.	Create a Cloud Storage bucket in the region closest to your location by following the four steps here: https://cloud.google.com/storage/docs/creating-buckets 
Make note of your bucket name and region for step 6b below

4.	Enable Vertex AI and Cloud Storage APIs by confirming your project, then enabling at the link below:
https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com,storage-component.googleapis.com  

5.	Download the notebook from the GitHub repo below and run it in Colab:
https://github.com/bw-cetech/apress-6.4-tfx-vertex-ai.git 

6.	Run through the notebook steps making sure to restart the runtime after installing the dependencies at the start

  a.	Log into your google account from the notebook
  b.	Set up your variables (project, region and bucket name)
  c.	Prepare the example data from the Palmer Penguins sample dataset
  d.	Create the TFX Pipeline
  e.	Run the pipeline on Vertex AI Pipelines
  
7.	The TFX pipeline at the end is orchestrated using Vertex Pipelines and Kubeflow V2 dag runner. Make sure to click on the link shown in the last cells output to see the pipeline job progress in Vertex AI on GCP, or visit the Google Cloud Console: https://console.cloud.google.com/ to see the API requests.

NB make sure to delete resources on GCP after finishing the lab, namely your pipeline run, Colab notebook, Cloud Storage bucket and project
