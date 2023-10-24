import boto3


def start_model(project_arn, model_arn, version_name, min_inference_units):
    client = boto3.client('rekognition')

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response = client.start_project_version(ProjectVersionArn=model_arn,
                                                MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter(
            'project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn,
                                            VersionNames=[ve3rsion_name])

        # Get the running status
        describe_response = client.describe_project_versions(
            ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage'])
    except Exception as e:
        print(e)

    print('Done...')


def main():
    project_arn = 'arn:aws:rekognition:us-east-2:531632897126:project/DLNR_Trial2/1691530789007'
    model_arn = 'arn:aws:rekognition:us-east-2:531632897126:project/DLNR_Trial2/version/DLNR_Trial2.2023-08-08T11.42.06/1691530927087'
    min_inference_units = 1
    version_name = 'DLNR_Trial2.2023-08-08T11.42.06'
    start_model(project_arn, model_arn, version_name, min_inference_units)


if __name__ == "__main__":
    main()
