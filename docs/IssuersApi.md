# swagger_client.IssuersApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_issuers_get**](IssuersApi.md#currency_issuers_get) | **GET** /currency-issuers | List of currency issuers
[**currency_issuers_id_get**](IssuersApi.md#currency_issuers_id_get) | **GET** /currency-issuers/{id} | Issuer by ID


# **currency_issuers_get**
> IssuersResponse currency_issuers_get(page_number=page_number, page_size=page_size)

List of currency issuers

Returns all available currency issuers. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuersApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)

try: 
    # List of currency issuers
    api_response = api_instance.currency_issuers_get(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuersApi->currency_issuers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 

### Return type

[**IssuersResponse**](IssuersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_issuers_id_get**
> IssuerResponse currency_issuers_id_get(id)

Issuer by ID

Returns issuer with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuersApi()
id = 'id_example' # str | Unique ID.

try: 
    # Issuer by ID
    api_response = api_instance.currency_issuers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuersApi->currency_issuers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**IssuerResponse**](IssuerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

