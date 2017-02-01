# swagger_client.OrganizationsApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_get**](OrganizationsApi.md#organizations_get) | **GET** /organizations | List of organizations
[**organizations_id_get**](OrganizationsApi.md#organizations_id_get) | **GET** /organizations/{id} | Organization by ID


# **organizations_get**
> OrganizationsResponse organizations_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_alias=filter_alias, filter_status=filter_status, filter_industries=filter_industries, sort=sort)

List of organizations

Returns all available organizations. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_name = 'filter_name_example' # str | Filtering by name. (optional)
filter_alias = 'filter_alias_example' # str | Filtering by alias. (optional)
filter_status = ['filter_status_example'] # list[str] | Filtration by status. (optional)
filter_industries = 'filter_industries_example' # str | Filtering by industries. (optional)
sort = ['sort_example'] # list[str] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | alias | -alias | | status | -status | | description | -description |  (optional)

try: 
    # List of organizations
    api_response = api_instance.organizations_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_alias=filter_alias, filter_status=filter_status, filter_industries=filter_industries, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_name** | **str**| Filtering by name. | [optional] 
 **filter_alias** | **str**| Filtering by alias. | [optional] 
 **filter_status** | [**list[str]**](str.md)| Filtration by status. | [optional] 
 **filter_industries** | **str**| Filtering by industries. | [optional] 
 **sort** | [**list[str]**](str.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | alias | -alias | | status | -status | | description | -description |  | [optional] 

### Return type

[**OrganizationsResponse**](OrganizationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_get**
> OrganizationResponse organizations_id_get(id)

Organization by ID

Returns organization with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
id = 'id_example' # str | Unique ID.

try: 
    # Organization by ID
    api_response = api_instance.organizations_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

