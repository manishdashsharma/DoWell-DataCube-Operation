# DoWell-DataCube-Operation
Repository showcasing the implementation of the DoWell DataCube API service as a class-based code.

Absolutely, here's the content in Markdown format suitable for GitHub documentation:

---

## DataCubeServices Usage Guide

### Setup

#### Requirements
Make sure you have the required packages installed.
```bash
pip install -r requirements.txt
```

#### Environment Variables
1. Create a `.env` file in your project directory.
2. Define the following variables inside `.env`:
    ```dotenv
    API_KEY=your_api_key_here
    DATABASE_NAME=your_database_name_here
    COLLECTION_NAME=your_collection_name_here
    ```

### Using DataCubeServices

1. **Insert Operation**
   This operation adds new data to your database collection.

    ```python
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
    ```

2. **Fetch Operation**
   Retrieve data from your database based on specified criteria.

    ```python
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
    ```

3. **Update Operation**
   Modify existing data in your database collection.

    ```python
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
    ```

4. **Delete Operation**
   Remove specific data from your database collection.

    ```python
    # Delete operation example
    delete_response = data_cube_services.delete_data(
        collection_name, 
        query={
            "_id": "6572ced931188f54bdc88a89"  # Replace with appropriate filter criteria
        }
    )
    print("Delete response:", delete_response)
    ```

5. **Add Collection Operation**
   Add a new collection to your database.

    ```python
    # Add collection operation example
    add_collection_response = data_cube_services.add_collection("Collection_4")
    print("Add collection response:", add_collection_response)
    ```

---

Customize these examples to suit your specific use case and database structure. Update placeholders like `collection_name`, `query` criteria, and specific data fields with your actual database details and requirements.

--- 

This guide provides examples and instructions for utilizing `DataCubeServices` to interact with your database. Adjust the code snippets to suit your use case.