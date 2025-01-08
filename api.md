# Shared Types

```python
from evrim.types import CreatedFieldsToProfile, Profile, ProfileToCollection, Report, Snapshot
```

# Prod

Types:

```python
from evrim.types import ProdSchemaResponse
```

Methods:

- <code title="get /prod/schema/">client.prod.<a href="./src/evrim/resources/prod.py">schema</a>(\*\*<a href="src/evrim/types/prod_schema_params.py">params</a>) -> <a href="./src/evrim/types/prod_schema_response.py">ProdSchemaResponse</a></code>

# Blank

## Profiles

Types:

```python
from evrim.types.blank import BlankProfile
```

Methods:

- <code title="post /prod/v0/blank/profile/">client.blank.profiles.<a href="./src/evrim/resources/blank/profiles.py">create</a>() -> <a href="./src/evrim/types/blank/blank_profile.py">BlankProfile</a></code>

## Templates

Types:

```python
from evrim.types.blank import BlankTemplate
```

Methods:

- <code title="post /prod/v0/blank/template/">client.blank.templates.<a href="./src/evrim/resources/blank/templates.py">create</a>() -> <a href="./src/evrim/types/blank/blank_template.py">BlankTemplate</a></code>

# Bulk

## Collections

### Profiles

Types:

```python
from evrim.types.bulk.collections import BulkProfilesToCollection
```

Methods:

- <code title="post /prod/v0/bulk/collections/profiles/">client.bulk.collections.profiles.<a href="./src/evrim/resources/bulk/collections/profiles.py">create</a>(\*\*<a href="src/evrim/types/bulk/collections/profile_create_params.py">params</a>) -> <a href="./src/evrim/types/bulk/collections/bulk_profiles_to_collection.py">BulkProfilesToCollection</a></code>

## CreatedFields

Types:

```python
from evrim.types.bulk import BulkCreatedField, CreatedFieldListResponse
```

Methods:

- <code title="post /prod/v0/bulk/created-fields/">client.bulk.created_fields.<a href="./src/evrim/resources/bulk/created_fields.py">create</a>(\*\*<a href="src/evrim/types/bulk/created_field_create_params.py">params</a>) -> <a href="./src/evrim/types/bulk/bulk_created_field.py">BulkCreatedField</a></code>
- <code title="get /prod/v0/bulk/created-fields/{id}/">client.bulk.created_fields.<a href="./src/evrim/resources/bulk/created_fields.py">retrieve</a>(id) -> <a href="./src/evrim/types/bulk/bulk_created_field.py">BulkCreatedField</a></code>
- <code title="get /prod/v0/bulk/created-fields/">client.bulk.created_fields.<a href="./src/evrim/resources/bulk/created_fields.py">list</a>() -> <a href="./src/evrim/types/bulk/created_field_list_response.py">CreatedFieldListResponse</a></code>

## Templates

### Profiles

Types:

```python
from evrim.types.bulk.templates import BulkJob, ProfileListResponse
```

Methods:

- <code title="post /prod/v0/bulk/templates/profiles/">client.bulk.templates.profiles.<a href="./src/evrim/resources/bulk/templates/profiles.py">create</a>(\*\*<a href="src/evrim/types/bulk/templates/profile_create_params.py">params</a>) -> <a href="./src/evrim/types/bulk/templates/bulk_job.py">BulkJob</a></code>
- <code title="get /prod/v0/bulk/templates/profiles/{id}/">client.bulk.templates.profiles.<a href="./src/evrim/resources/bulk/templates/profiles.py">retrieve</a>(id) -> <a href="./src/evrim/types/bulk/templates/bulk_job.py">BulkJob</a></code>
- <code title="get /prod/v0/bulk/templates/profiles/">client.bulk.templates.profiles.<a href="./src/evrim/resources/bulk/templates/profiles.py">list</a>() -> <a href="./src/evrim/types/bulk/templates/profile_list_response.py">ProfileListResponse</a></code>

# Collections

Types:

```python
from evrim.types import Collection, CollectionListResponse
```

Methods:

- <code title="post /prod/v0/collections/">client.collections.<a href="./src/evrim/resources/collections.py">create</a>(\*\*<a href="src/evrim/types/collection_create_params.py">params</a>) -> <a href="./src/evrim/types/collection.py">Collection</a></code>
- <code title="get /prod/v0/collections/{id}/">client.collections.<a href="./src/evrim/resources/collections.py">retrieve</a>(id) -> <a href="./src/evrim/types/collection.py">Collection</a></code>
- <code title="patch /prod/v0/collections/{id}/">client.collections.<a href="./src/evrim/resources/collections.py">update</a>(id, \*\*<a href="src/evrim/types/collection_update_params.py">params</a>) -> <a href="./src/evrim/types/collection.py">Collection</a></code>
- <code title="get /prod/v0/collections/">client.collections.<a href="./src/evrim/resources/collections.py">list</a>() -> <a href="./src/evrim/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /prod/v0/collections/{id}/">client.collections.<a href="./src/evrim/resources/collections.py">delete</a>(id) -> None</code>

# CreatedFields

Types:

```python
from evrim.types import CreatedField, CreatedFieldListResponse
```

Methods:

- <code title="post /prod/v0/created-fields/">client.created_fields.<a href="./src/evrim/resources/created_fields.py">create</a>(\*\*<a href="src/evrim/types/created_field_create_params.py">params</a>) -> <a href="./src/evrim/types/created_field.py">CreatedField</a></code>
- <code title="get /prod/v0/created-fields/{id}/">client.created_fields.<a href="./src/evrim/resources/created_fields.py">retrieve</a>(id) -> <a href="./src/evrim/types/created_field.py">CreatedField</a></code>
- <code title="patch /prod/v0/created-fields/{id}/">client.created_fields.<a href="./src/evrim/resources/created_fields.py">update</a>(id, \*\*<a href="src/evrim/types/created_field_update_params.py">params</a>) -> <a href="./src/evrim/types/created_field.py">CreatedField</a></code>
- <code title="get /prod/v0/created-fields/">client.created_fields.<a href="./src/evrim/resources/created_fields.py">list</a>() -> <a href="./src/evrim/types/created_field_list_response.py">CreatedFieldListResponse</a></code>
- <code title="delete /prod/v0/created-fields/{id}/">client.created_fields.<a href="./src/evrim/resources/created_fields.py">delete</a>(id) -> None</code>
- <code title="post /prod/v0/created-fields/{field_id}/profile/">client.created_fields.<a href="./src/evrim/resources/created_fields.py">profile</a>(field_id, \*\*<a href="src/evrim/types/created_field_profile_params.py">params</a>) -> None</code>

# Fields

Types:

```python
from evrim.types import Field, FieldToTemplate, FieldListResponse
```

Methods:

- <code title="post /prod/v0/fields/">client.fields.<a href="./src/evrim/resources/fields.py">create</a>(\*\*<a href="src/evrim/types/field_create_params.py">params</a>) -> <a href="./src/evrim/types/field.py">Field</a></code>
- <code title="get /prod/v0/fields/{id}/">client.fields.<a href="./src/evrim/resources/fields.py">retrieve</a>(id) -> <a href="./src/evrim/types/field.py">Field</a></code>
- <code title="patch /prod/v0/fields/{id}/">client.fields.<a href="./src/evrim/resources/fields.py">update</a>(\*, path_id, \*\*<a href="src/evrim/types/field_update_params.py">params</a>) -> <a href="./src/evrim/types/field.py">Field</a></code>
- <code title="get /prod/v0/fields/">client.fields.<a href="./src/evrim/resources/fields.py">list</a>() -> <a href="./src/evrim/types/field_list_response.py">FieldListResponse</a></code>
- <code title="delete /prod/v0/fields/{id}/">client.fields.<a href="./src/evrim/resources/fields.py">delete</a>(id) -> None</code>
- <code title="post /prod/v0/fields/{field_id}/template/">client.fields.<a href="./src/evrim/resources/fields.py">template</a>(field_id, \*\*<a href="src/evrim/types/field_template_params.py">params</a>) -> <a href="./src/evrim/types/field_to_template.py">FieldToTemplate</a></code>

# Outlines

Types:

```python
from evrim.types import Outline, OutlineListResponse
```

Methods:

- <code title="post /prod/v0/outlines/">client.outlines.<a href="./src/evrim/resources/outlines.py">create</a>(\*\*<a href="src/evrim/types/outline_create_params.py">params</a>) -> <a href="./src/evrim/types/outline.py">Outline</a></code>
- <code title="get /prod/v0/outlines/{id}/">client.outlines.<a href="./src/evrim/resources/outlines.py">retrieve</a>(id) -> <a href="./src/evrim/types/outline.py">Outline</a></code>
- <code title="patch /prod/v0/outlines/{id}/">client.outlines.<a href="./src/evrim/resources/outlines.py">update</a>(id, \*\*<a href="src/evrim/types/outline_update_params.py">params</a>) -> <a href="./src/evrim/types/outline.py">Outline</a></code>
- <code title="get /prod/v0/outlines/">client.outlines.<a href="./src/evrim/resources/outlines.py">list</a>() -> <a href="./src/evrim/types/outline_list_response.py">OutlineListResponse</a></code>
- <code title="delete /prod/v0/outlines/{id}/">client.outlines.<a href="./src/evrim/resources/outlines.py">delete</a>(id) -> None</code>

# Profiles

Types:

```python
from evrim.types import TagProfile, ProfileListResponse
```

Methods:

- <code title="post /prod/v0/profiles/">client.profiles.<a href="./src/evrim/resources/profiles/profiles.py">create</a>(\*\*<a href="src/evrim/types/profile_create_params.py">params</a>) -> <a href="./src/evrim/types/shared/profile.py">Profile</a></code>
- <code title="get /prod/v0/profiles/{id}/">client.profiles.<a href="./src/evrim/resources/profiles/profiles.py">retrieve</a>(id) -> <a href="./src/evrim/types/shared/profile.py">Profile</a></code>
- <code title="patch /prod/v0/profiles/{id}/">client.profiles.<a href="./src/evrim/resources/profiles/profiles.py">update</a>(id, \*\*<a href="src/evrim/types/profile_update_params.py">params</a>) -> <a href="./src/evrim/types/shared/profile.py">Profile</a></code>
- <code title="get /prod/v0/profiles/">client.profiles.<a href="./src/evrim/resources/profiles/profiles.py">list</a>() -> <a href="./src/evrim/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /prod/v0/profiles/{id}/">client.profiles.<a href="./src/evrim/resources/profiles/profiles.py">delete</a>(id) -> None</code>
- <code title="post /prod/v0/profiles/{profile_id}/tag/">client.profiles.<a href="./src/evrim/resources/profiles/profiles.py">tag</a>(profile_id, \*\*<a href="src/evrim/types/profile_tag_params.py">params</a>) -> <a href="./src/evrim/types/tag_profile.py">TagProfile</a></code>

## Collections

Methods:

- <code title="post /prod/v0/profiles/{profile_id}/collections/">client.profiles.collections.<a href="./src/evrim/resources/profiles/collections.py">create</a>(profile_id, \*\*<a href="src/evrim/types/profiles/collection_create_params.py">params</a>) -> <a href="./src/evrim/types/shared/profile_to_collection.py">ProfileToCollection</a></code>

## CreatedFields

Methods:

- <code title="post /prod/v0/profiles/{profile_id}/created-fields/">client.profiles.created_fields.<a href="./src/evrim/resources/profiles/created_fields.py">create</a>(profile_id, \*\*<a href="src/evrim/types/profiles/created_field_create_params.py">params</a>) -> <a href="./src/evrim/types/shared/created_fields_to_profile.py">CreatedFieldsToProfile</a></code>

## Latest

Types:

```python
from evrim.types.profiles import LatestRetrieveResponse
```

Methods:

- <code title="get /prod/v0/profiles/{profile_id}/latest/">client.profiles.latest.<a href="./src/evrim/resources/profiles/latest.py">retrieve</a>(profile_id) -> <a href="./src/evrim/types/profiles/latest_retrieve_response.py">LatestRetrieveResponse</a></code>

## Reports

Types:

```python
from evrim.types.profiles import ReportListResponse
```

Methods:

- <code title="get /prod/v0/profiles/{profile_id}/reports/">client.profiles.reports.<a href="./src/evrim/resources/profiles/reports.py">list</a>(profile_id) -> <a href="./src/evrim/types/profiles/report_list_response.py">ReportListResponse</a></code>

## Snapshots

Types:

```python
from evrim.types.profiles import CreateProfileSnapshot, SnapshotListResponse
```

Methods:

- <code title="post /prod/v0/profiles/{profile_id}/snapshots/">client.profiles.snapshots.<a href="./src/evrim/resources/profiles/snapshots.py">create</a>(profile_id) -> <a href="./src/evrim/types/profiles/create_profile_snapshot.py">CreateProfileSnapshot</a></code>
- <code title="get /prod/v0/profiles/{profile_id}/snapshots/{snapshot_id}/">client.profiles.snapshots.<a href="./src/evrim/resources/profiles/snapshots.py">retrieve</a>(snapshot_id, \*, profile_id) -> <a href="./src/evrim/types/profiles/create_profile_snapshot.py">CreateProfileSnapshot</a></code>
- <code title="get /prod/v0/profiles/{profile_id}/snapshots/">client.profiles.snapshots.<a href="./src/evrim/resources/profiles/snapshots.py">list</a>(profile_id) -> <a href="./src/evrim/types/profiles/snapshot_list_response.py">SnapshotListResponse</a></code>

# PromptTemplates

Types:

```python
from evrim.types import PromptTemplate, PromptTemplateListResponse
```

Methods:

- <code title="post /prod/v0/prompt-templates/">client.prompt_templates.<a href="./src/evrim/resources/prompt_templates.py">create</a>(\*\*<a href="src/evrim/types/prompt_template_create_params.py">params</a>) -> <a href="./src/evrim/types/prompt_template.py">PromptTemplate</a></code>
- <code title="get /prod/v0/prompt-templates/{id}/">client.prompt_templates.<a href="./src/evrim/resources/prompt_templates.py">retrieve</a>(id) -> <a href="./src/evrim/types/prompt_template.py">PromptTemplate</a></code>
- <code title="get /prod/v0/prompt-templates/">client.prompt_templates.<a href="./src/evrim/resources/prompt_templates.py">list</a>() -> <a href="./src/evrim/types/prompt_template_list_response.py">PromptTemplateListResponse</a></code>

# ReportsV3

Types:

```python
from evrim.types import ReportsV3ListResponse
```

Methods:

- <code title="post /prod/v0/reports-v3/">client.reports_v3.<a href="./src/evrim/resources/reports_v3.py">create</a>(\*\*<a href="src/evrim/types/reports_v3_create_params.py">params</a>) -> <a href="./src/evrim/types/shared/report.py">Report</a></code>
- <code title="get /prod/v0/reports-v3/{id}/">client.reports_v3.<a href="./src/evrim/resources/reports_v3.py">retrieve</a>(id) -> <a href="./src/evrim/types/shared/report.py">Report</a></code>
- <code title="patch /prod/v0/reports-v3/{id}/">client.reports_v3.<a href="./src/evrim/resources/reports_v3.py">update</a>(id, \*\*<a href="src/evrim/types/reports_v3_update_params.py">params</a>) -> <a href="./src/evrim/types/shared/report.py">Report</a></code>
- <code title="get /prod/v0/reports-v3/">client.reports_v3.<a href="./src/evrim/resources/reports_v3.py">list</a>() -> <a href="./src/evrim/types/reports_v3_list_response.py">ReportsV3ListResponse</a></code>
- <code title="delete /prod/v0/reports-v3/{id}/">client.reports_v3.<a href="./src/evrim/resources/reports_v3.py">delete</a>(id) -> None</code>

# Snapshots

Types:

```python
from evrim.types import SnapshotListResponse
```

Methods:

- <code title="get /prod/v0/snapshots/{id}/">client.snapshots.<a href="./src/evrim/resources/snapshots.py">retrieve</a>(id) -> <a href="./src/evrim/types/shared/snapshot.py">Snapshot</a></code>
- <code title="get /prod/v0/snapshots/">client.snapshots.<a href="./src/evrim/resources/snapshots.py">list</a>() -> <a href="./src/evrim/types/snapshot_list_response.py">SnapshotListResponse</a></code>

# Tags

Types:

```python
from evrim.types import Tag, TagListResponse
```

Methods:

- <code title="post /prod/v0/tags/">client.tags.<a href="./src/evrim/resources/tags/tags.py">create</a>(\*\*<a href="src/evrim/types/tag_create_params.py">params</a>) -> <a href="./src/evrim/types/tag.py">Tag</a></code>
- <code title="get /prod/v0/tags/{id}/">client.tags.<a href="./src/evrim/resources/tags/tags.py">retrieve</a>(id) -> <a href="./src/evrim/types/tag.py">Tag</a></code>
- <code title="patch /prod/v0/tags/{id}/">client.tags.<a href="./src/evrim/resources/tags/tags.py">update</a>(id, \*\*<a href="src/evrim/types/tag_update_params.py">params</a>) -> <a href="./src/evrim/types/tag.py">Tag</a></code>
- <code title="get /prod/v0/tags/">client.tags.<a href="./src/evrim/resources/tags/tags.py">list</a>() -> <a href="./src/evrim/types/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /prod/v0/tags/{id}/">client.tags.<a href="./src/evrim/resources/tags/tags.py">delete</a>(id) -> None</code>

## Collections

Types:

```python
from evrim.types.tags import TagToCollection
```

Methods:

- <code title="post /prod/v0/tags/{tag_id}/collections/">client.tags.collections.<a href="./src/evrim/resources/tags/collections.py">tag</a>(tag_id, \*\*<a href="src/evrim/types/tags/collection_tag_params.py">params</a>) -> <a href="./src/evrim/types/tags/tag_to_collection.py">TagToCollection</a></code>

## Profiles

Types:

```python
from evrim.types.tags import ProfileListResponse
```

Methods:

- <code title="get /prod/v0/tags/{tag_id}/profiles/">client.tags.profiles.<a href="./src/evrim/resources/tags/profiles.py">list</a>(tag_id) -> <a href="./src/evrim/types/tags/profile_list_response.py">ProfileListResponse</a></code>
- <code title="post /prod/v0/tags/{tag_id}/profiles/">client.tags.profiles.<a href="./src/evrim/resources/tags/profiles.py">tag</a>(tag_id, \*\*<a href="src/evrim/types/tags/profile_tag_params.py">params</a>) -> None</code>

# Templates

Types:

```python
from evrim.types import Template, TemplateListResponse
```

Methods:

- <code title="post /prod/v0/templates/">client.templates.<a href="./src/evrim/resources/templates/templates.py">create</a>(\*\*<a href="src/evrim/types/template_create_params.py">params</a>) -> <a href="./src/evrim/types/template.py">Template</a></code>
- <code title="get /prod/v0/templates/{id}/">client.templates.<a href="./src/evrim/resources/templates/templates.py">retrieve</a>(id) -> <a href="./src/evrim/types/template.py">Template</a></code>
- <code title="patch /prod/v0/templates/{id}/">client.templates.<a href="./src/evrim/resources/templates/templates.py">update</a>(id, \*\*<a href="src/evrim/types/template_update_params.py">params</a>) -> <a href="./src/evrim/types/template.py">Template</a></code>
- <code title="get /prod/v0/templates/">client.templates.<a href="./src/evrim/resources/templates/templates.py">list</a>() -> <a href="./src/evrim/types/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /prod/v0/templates/{id}/">client.templates.<a href="./src/evrim/resources/templates/templates.py">delete</a>(id) -> None</code>

## Profiles

Types:

```python
from evrim.types.templates import ProfileListResponse
```

Methods:

- <code title="get /prod/v0/templates/{template_id}/profiles/">client.templates.profiles.<a href="./src/evrim/resources/templates/profiles.py">list</a>(template_id) -> <a href="./src/evrim/types/templates/profile_list_response.py">ProfileListResponse</a></code>
