# openfintech_sdk.BanksApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banks_get**](BanksApi.md#banks_get) | **GET** /banks | List of banks
[**banks_id_get**](BanksApi.md#banks_id_get) | **GET** /banks/{id} | Bank by ID


# **banks_get**
> BanksResponse banks_get(page_number=page_number, page_size=page_size, filter_sort_code=filter_sort_code, filter_alias=filter_alias, filter_status=filter_status, sort=sort)

List of banks

Returns all available banks 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.BanksApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_sort_code = 'filter_sort_code_example' # str | Filtering by banks code. (optional)
filter_alias = 'filter_alias_example' # str | Filtering by alias. (optional)
filter_status = ['filter_status_example'] # list[str] | Filtration by status. (optional)
sort = ['sort_example'] # list[str] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | alias | -alias | | status | -status | | sort_code | -sort_code |  (optional)

try: 
    # List of banks
    api_response = api_instance.banks_get(page_number=page_number, page_size=page_size, filter_sort_code=filter_sort_code, filter_alias=filter_alias, filter_status=filter_status, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BanksApi->banks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_sort_code** | **str**| Filtering by banks code. | [optional] 
 **filter_alias** | **str**| Filtering by alias. | [optional] 
 **filter_status** | [**list[str]**](str.md)| Filtration by status. | [optional] 
 **sort** | [**list[str]**](str.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | alias | -alias | | status | -status | | sort_code | -sort_code |  | [optional] 

### Return type

[**BanksResponse**](BanksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banks_id_get**
> BankResponse banks_id_get(id)

Bank by ID

Returns bank with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.BanksApi()
id = 'id_example' # str | Unique ID.

try: 
    # Bank by ID
    api_response = api_instance.banks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BanksApi->banks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**BankResponse**](BankResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

