# swagger_client.PaymentProvidersApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_providers_get**](PaymentProvidersApi.md#payment_providers_get) | **GET** /payment-providers | List of payment providers
[**payment_providers_id_get**](PaymentProvidersApi.md#payment_providers_id_get) | **GET** /payment-providers/{id} | Payment provider by ID


# **payment_providers_get**
> PaymentProvidersResponse payment_providers_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_alias=filter_alias, filter_types=filter_types, filter_sales_channels=filter_sales_channels, filter_features=filter_features, sort=sort)

List of payment providers

Returns all available payment providers. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentProvidersApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_name = 'filter_name_example' # str | Filtering by name. (optional)
filter_alias = 'filter_alias_example' # str | Filtering by alias. (optional)
filter_types = ['filter_types_example'] # list[str] | Filtering by types. (optional)
filter_sales_channels = ['filter_sales_channels_example'] # list[str] | Filtering by sales channels. (optional)
filter_features = ['filter_features_example'] # list[str] | Filtering by features. (optional)
sort = ['sort_example'] # list[str] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | alias | -alias |  (optional)

try: 
    # List of payment providers
    api_response = api_instance.payment_providers_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_alias=filter_alias, filter_types=filter_types, filter_sales_channels=filter_sales_channels, filter_features=filter_features, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentProvidersApi->payment_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_name** | **str**| Filtering by name. | [optional] 
 **filter_alias** | **str**| Filtering by alias. | [optional] 
 **filter_types** | [**list[str]**](str.md)| Filtering by types. | [optional] 
 **filter_sales_channels** | [**list[str]**](str.md)| Filtering by sales channels. | [optional] 
 **filter_features** | [**list[str]**](str.md)| Filtering by features. | [optional] 
 **sort** | [**list[str]**](str.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | alias | -alias |  | [optional] 

### Return type

[**PaymentProvidersResponse**](PaymentProvidersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_providers_id_get**
> PaymentProviderResponse payment_providers_id_get(id)

Payment provider by ID

Returns payment provider with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentProvidersApi()
id = 'id_example' # str | Unique ID.

try: 
    # Payment provider by ID
    api_response = api_instance.payment_providers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentProvidersApi->payment_providers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**PaymentProviderResponse**](PaymentProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

