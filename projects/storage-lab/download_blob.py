from azure.storage.blob import BlobServiceClient

connection_string = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey="
    "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq"
    "/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

container_name = "lab-files"

blob_service_client = BlobServiceClient.from_connection_string(
    connection_string
)

blob_client = blob_service_client.get_blob_client(
    container=container_name,
    blob="test.txt"
)

with open("downloaded_test.txt", "wb") as file:

    data = blob_client.download_blob()

    file.write(data.readall())

print("Archivo descargado correctamente")