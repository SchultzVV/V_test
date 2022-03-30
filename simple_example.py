import mlflow
#mlflow.set_tracking_uri('s3://sagemaker-studio-230284766115-x05esh0id9/Test_MlFlow/')
#mlflow.set_tracking_uri('http://ec2-54-158-221-75.compute-1.amazonaws.com:5000/')
mlflow.set_tracking_uri('http://0.0.0.0:5000/')
mlflow.set_experiment(experiment_name='last')
with mlflow.start_run(run_name='experiment_png'):
    mlflow.log_param('B',2)
    for z in range(10):
        mlflow.log_metric('A',z)
    mlflow.log_artifact('1.png')
