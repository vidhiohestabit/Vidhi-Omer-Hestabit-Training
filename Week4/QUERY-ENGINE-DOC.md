# Query Engine Documentation

## Supported Filters

- search → regex search on name & description
- minPrice / maxPrice → price range filtering
- sort=field:asc|desc
- tags=tag1,tag2
- page & limit for pagination
- includeDeleted=true to include soft-deleted records

## Soft Delete Strategy

Products are not permanently removed.
DELETE /products/:id sets deletedAt timestamp.

By default:
GET /products excludes deleted records.

## Error Contract

{
  success: false,
  message: string,
  code: string,
  timestamp: ISOString,
  path: request URL
}