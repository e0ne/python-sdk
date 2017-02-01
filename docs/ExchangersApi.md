# openfintech_sdk.ExchangersApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchangers_get**](ExchangersApi.md#exchangers_get) | **GET** /exchangers | List of exchangers
[**exchangers_id_get**](ExchangersApi.md#exchangers_id_get) | **GET** /exchangers/{id} | Exchanger by ID


# **exchangers_get**
> ExchangersResponse exchangers_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_status=filter_status, sort=sort)

List of exchangers

Returns all available exchangers.<br> Rates export standards is represented by:  * [estandards](http://estandards.info) * [jsons](http://jsons.info) * ratex - our internal standard 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.ExchangersApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_name = 'filter_name_example' # str | Filtering by name. (optional)
filter_status = ['filter_status_example'] # list[str] | Filtration by status. (optional)
sort = ['sort_example'] # list[str] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | status | -status | | wmid | -wmid | | rate_type | -rate_type | | rates_export_standard | <nobr>-rates_export_standard</nobr> |  (optional)

try: 
    # List of exchangers
    api_response = api_instance.exchangers_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_status=filter_status, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangersApi->exchangers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_name** | **str**| Filtering by name. | [optional] 
 **filter_status** | [**list[str]**](str.md)| Filtration by status. | [optional] 
 **sort** | [**list[str]**](str.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | status | -status | | wmid | -wmid | | rate_type | -rate_type | | rates_export_standard | &lt;nobr&gt;-rates_export_standard&lt;/nobr&gt; |  | [optional] 

### Return type

[**ExchangersResponse**](ExchangersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchangers_id_get**
> ExchangerResponse exchangers_id_get(id)

Exchanger by ID

Returns exchanger with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.ExchangersApi()
id = 'id_example' # str | Unique ID.

try: 
    # Exchanger by ID
    api_response = api_instance.exchangers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangersApi->exchangers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**ExchangerResponse**](ExchangerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

