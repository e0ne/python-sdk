# openfintech_sdk.IndustriesApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_industries_get**](IndustriesApi.md#organization_industries_get) | **GET** /organization-industries | List of organization industries
[**organization_industries_id_get**](IndustriesApi.md#organization_industries_id_get) | **GET** /organization-industries/{id} | Industry by ID


# **organization_industries_get**
> IndustriesResponse organization_industries_get(page_number=page_number, page_size=page_size)

List of organization industries

Returns all available organization industries. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.IndustriesApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)

try: 
    # List of organization industries
    api_response = api_instance.organization_industries_get(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustriesApi->organization_industries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 

### Return type

[**IndustriesResponse**](IndustriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_industries_id_get**
> IndustryResponse organization_industries_id_get(id)

Industry by ID

Returns industry with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.IndustriesApi()
id = 'id_example' # str | Unique ID.

try: 
    # Industry by ID
    api_response = api_instance.organization_industries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustriesApi->organization_industries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**IndustryResponse**](IndustryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

