from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials.json"
# Initialize Firestore client
db = firestore.Client(database="fruit-fruit")

def add_data(collection, document, data):
    print(db)
    doc_ref = db.collection(collection).document(document)
    doc_ref.set(data)
    print("Document {} added successfully!".format(document))

def delete_data(collection, document):
    doc_ref = db.collection(collection).document(document)
    doc_ref.delete()
    print("Document {} deleted successfully!".format(document))

def update_data(collection, document, data):
    doc_ref = db.collection(collection).document(document)
    doc_ref.update(data)
    print("Document {} updated successfully!".format(document))

if __name__ == "__main__":
    # Example usage
    collection_name = "users"
    document_name = "user1"
    user_data = {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com"
    }

    # Add data
    add_data(collection_name, document_name, user_data)

    # Update data
    updated_data = {"age": 31}
    update_data(collection_name, document_name, updated_data)

    # Delete data
    delete_data(collection_name, document_name)
