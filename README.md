
# Project 2: Operationalizing Machine Learning

## Project Overview
The goal of the project was to build, deploy and consume a classifier that will predict whether a bank customer will suscribe to a product or not. In the process, I learnt about deploying models, consuming endpoints and building pipelines.

## Architectural Diagram
![Architectural diagram](project2_architecture.png)

## How to improve the project in the future
The project can be improved by advanced feature engineering, such as creating new features and dropping some columns.

## Screenshots

### 1. Registered Datasets
![registered datasets](screenshots/registered_datasets.png)
Creating the dataset using the provided URI.

### 2. Complete Experiment
![Completed Experiment](screenshots/Completed Experiment.png)
The finished automl run of the experiment we created. You can  see details such as duration and best model.

### 3. Best Model
![Best Model](screenshots/best model.png)
More details on the best model. You can click on view other metrics to explore the model

### 4. Application Insights Enabled
![insights enabled](screenshots/enable_insights_portal.png)
One can click on the url to view insights on the endpoint

### 5. Enabling insights using logs.py
![Logs.py output](screenshots/enabling_insights_cmd.png)

Here we are enabling insights from local machine usig azure sdk and outputting the logs so we see what is going on.
### 6. Swagger runs on local host
![Swagger UI](screenshots/swagger_ui.png)
Swagger allows us to see the http methods, sample inputs and expected outputs

### 7. Consuming the endpoint using endpoint.py
![Consume](screenshots/consuming_endpoints.png)
The model predicted no for both observations. The output is as we expected it meaning the api is healthy.

### 8. Running a benchmark
![Benchmark](screenshots/benchmark.png) 
We get some insights(response time, etc.) from Apache about our endpoint.

### 9. Pipeline created
![created pipeline](screenshots/pipeline_created.png)

### 10. Pipeline Endpoint
![pipeline endpoint](screenshots/pipeline_section.png)

### 11. Bank Marketing Dataset with Automl 
![dataset and automl](screenshots/dataset_and_aml_module.png) Design showing the full pipeline.

### 12. Published Pipeline Overview
![published pipeline](screenshots/published_pipeline_overview.png) It shows the  REST endpoint and the active status.

### 13. RunDetails Widget
![Run details](screenshots/run_details_nb.png) It indicates that the run is complete

### 14. Scheduled Run in ML Studio 
![Scheduled Run](screenshots/scheduled_run.png) You can see the top-most run of the pipeline-rest-endpoint is still running right from the home page of Azure ML Studio.


## ScreenCast: [YouTube link](https://youtu.be/Q0trirdPpRA)
