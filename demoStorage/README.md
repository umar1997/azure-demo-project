# Azure Blob Storage

### Goal
> The goal of the project is to create a Blob Storage and upload some files onto it

> Azure Blob Storage is a service provided by Microsoft Azure that allows you to store and manage large amounts of unstructured data, such as text and binary data. It is part of the Azure Storage suite and is designed to handle a variety of storage scenarios.

### Set Up
1. Create a Azure Blob Storage on Azure Portal
<br>
[https://portal.azure.com/#create/Microsoft.StorageAccount-ARM](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)

2. Set up the Blob Storage
![CreateStorage](./../Images/demoStorage/create-storage.png)

3. After Deploment is complete
![ViewStorage](./../Images/demoStorage/view-storage.png)


4. Create a container
![CreateContainer](./../Images/demoStorage/create-container.png)


5. Upload content through 3 different ways
    1. Using the upload button on the portal
    ![UploadContent](./../Images/demoStorage/upload-content.png)

    2. Using Azure Blob Storage Python Client
    
    ```python
      from azure.identity import DefaultAzureCredential
      from azure.storage.blob import BlobServiceClient

      def upload_sample_data(credential: DefaultAzureCredential):
        # Connect to Blob Storage
        account_url = os.environ["AZURE_STORAGE_ACCOUNT_BLOB_URL"]
        blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
        container_client = blob_service_client.get_container_client(sample_container_name)
        if not container_client.exists():
            container_client.create_container()

        sample_data_directory_name = os.path.join("data", "documents")
        sample_data_directory = os.path.join(os.getcwd(), sample_data_directory_name)
        for filename in os.listdir(sample_data_directory):
            with open(os.path.join(sample_data_directory, filename), "rb") as f:
                blob_client = container_client.get_blob_client(filename)
                if not blob_client.exists():
                    print(f"Uploading {filename}...")
                    blob_client.upload_blob(data=f)
                    print(f"Completed {filename}!")
    ```
    How to get `AZURE_STORAGE_ACCOUNT_BLOB_URL`
    ```shell
        export AZURE_STORAGE_ACCOUNT=<storage_account_name>
        export AZURE_STORAGE_ACCOUNT_BLOB_URL=https://$AZURE_STORAGE_ACCOUNT.blob.core.windows.net/
        echo $AZURE_STORAGE_ACCOUNT_BLOB_URL
        
        # https://readinggroupstorage.blob.core.windows.net/
    ```


    3. Using AzCopy ([Documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=dnf))
      - Download AzCopy Portable Binary ([Download Link](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=dnf#download-the-azcopy-portable-binary))
      - Extract the file 
        ```shell
        tar -xzvf azcopy_linux_amd64_10.25.1.tar.gz
        ```
      - Generate the Blob SAS URL

        (Remember to give both `Read` and `Write` permissions whie generating the SAS URL)
       ![AccessToken](./../Images/demoStorage/access-token.png)

      - Copy the folder contents into the Storage
      ```shell
      # cd to the folder which has the azcopy executable
      ./azcopy copy "/nfs/users/ext_tr_muhammad_salman/Azure_AI/azure-demo-project/demoStorage/Data/*" "https://readinggroupstorage.blob.core.windows.net/sample-container?sp=rw&st=2024-08-12T17:20:19Z&se=2024-08-31T01:20:19Z&sv=2022-11-02&sr=c&sig=Hak6U7cPBDlqvYM1jYh%2Fvpz5gNtpIUYVtGE6yTpBj58%3D" --recursive=true
      ```