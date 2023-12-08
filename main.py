from dotenv import load_dotenv
import os
from datacubeservices import DataCubeServices 

# Load environment variables from .env file or use existing environment variables
if os.getenv("API_KEY"):
    api_key = str(os.getenv("API_KEY"))
    database_name = str(os.getenv("DATABASE_NAME"))
    collection_name = str(os.getenv("COLLECTION_NAME"))
else:
    load_dotenv(f"{os.getcwd()}/.env")
    api_key = str(os.getenv("API_KEY"))
    database_name = str(os.getenv("DATABASE_NAME"))
    collection_name = str(os.getenv("COLLECTION_NAME"))

# Initialize the DataCubeServices for database operations
data_cube_services = DataCubeServices(api_key, database_name)

# Insert operation example
inserted_data = data_cube_services.insert_data(collection_name, {
    "info": {
        'name': "Manish",
        'email': "mdashsharma95@gmail.com",
    },
    "records": [{
        "record": "1",
        "type": "overall"
    }]
})
print("Inserted data:", inserted_data)

# Fetch operation example
fetch_response = data_cube_services.fetch_data(
    collection_name, 
    filters={
        "_id": "6572ced931188f54bdc88a89"  # Replace with appropriate filter criteria
    }, 
    limit=1, 
    offset=0
)
print("Fetch response:", fetch_response)

# Update operation example
update_response = data_cube_services.update_data(
    collection_name,  
    query={
        "_id": "6572ced931188f54bdc88a89"  # Replace with appropriate filter criteria
    }, 
    update_data={
        "info": {
            'name': "Manish Dash",
            'email': "mdashsharma95@gmail.com",
        },
        "records": [{
            "record": "1",
            "type": "overall_updated"
        }]
    }
)
print("Update response:", update_response)

# Delete operation example
delete_response = data_cube_services.delete_data(
    collection_name, 
    query={
        "_id": "6572ced931188f54bdc88a89"  # Replace with appropriate filter criteria
    }
)
print("Delete response:", delete_response)

# Add collection operation example
add_collection_response = data_cube_services.add_collection("Collection_4")
print("Add collection response:", add_collection_response)
