# swagger_client.MerchantIndustriesApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_industries_get**](MerchantIndustriesApi.md#merchant_industries_get) | **GET** /merchant-industries | List of merchant industries
[**merchant_industries_id_get**](MerchantIndustriesApi.md#merchant_industries_id_get) | **GET** /merchant-industries/{id} | Merchant industry by ID


# **merchant_industries_get**
> MerchantIndustriesResponse merchant_industries_get(page_number=page_number, page_size=page_size, filter_name=filter_name)

List of merchant industries

Returns all available merchant industries. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantIndustriesApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_name = 'filter_name_example' # str | Filtering by name. (optional)

try: 
    # List of merchant industries
    api_response = api_instance.merchant_industries_get(page_number=page_number, page_size=page_size, filter_name=filter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantIndustriesApi->merchant_industries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_name** | **str**| Filtering by name. | [optional] 

### Return type

[**MerchantIndustriesResponse**](MerchantIndustriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchant_industries_id_get**
> MerchantIndustryResponse merchant_industries_id_get(id)

Merchant industry by ID

Returns merchant industry with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantIndustriesApi()
id = 'id_example' # str | Unique ID.

try: 
    # Merchant industry by ID
    api_response = api_instance.merchant_industries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantIndustriesApi->merchant_industries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**MerchantIndustryResponse**](MerchantIndustryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

