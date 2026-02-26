# New Feature: Delete Item

## 1. Problem / User Need (Why)

Once created, items can never be removed. 

## 2. Goal / Success Criteria

User can delete old or accidental items.
API returns 204 No Content on success.
API returns 404 if item not found.
API returns proper error message in JSON for 404.
Unit tests are updated.

## 3. Technical Details
- Endpoint: DELETE /items/<item_id>
- Remove item by ID from the in-memory list
- Add proper error message in JSON for 404
- Update unit tests to cover happy path + 404 case
- Include unit tests for invalid <item_id> like alpha numeric 