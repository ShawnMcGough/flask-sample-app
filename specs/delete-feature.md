# New Feature: Delete Item
- Endpoint: DELETE /items/<item_id>
- Remove item by ID from the in-memory list
- Return 204 No Content on success
- Return 404 if item not found
- Add proper error message in JSON for 404
- Update unit tests to cover happy path + 404 case