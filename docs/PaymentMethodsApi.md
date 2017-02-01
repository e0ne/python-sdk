# openfintech_sdk.PaymentMethodsApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_methods_get**](PaymentMethodsApi.md#payment_methods_get) | **GET** /payment-methods | List of payment methods
[**payment_methods_id_get**](PaymentMethodsApi.md#payment_methods_id_get) | **GET** /payment-methods/{id} | Payment method by ID


# **payment_methods_get**
> PaymentMethodsResponse payment_methods_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_alias=filter_alias, filter_processor_name=filter_processor_name, filter_category=filter_category, sort=sort)

List of payment methods

Returns all available payment methods. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.PaymentMethodsApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_name = 'filter_name_example' # str | Filtering by name. (optional)
filter_alias = 'filter_alias_example' # str | Filtering by alias. (optional)
filter_processor_name = 'filter_processor_name_example' # str | Filtering by processor_name. (optional)
filter_category = ['filter_category_example'] # list[str] | Filtering by category. (optional)
sort = ['sort_example'] # list[str] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | alias | -alias | | processor_name | -processor_name | | category | -category |  (optional)

try: 
    # List of payment methods
    api_response = api_instance.payment_methods_get(page_number=page_number, page_size=page_size, filter_name=filter_name, filter_alias=filter_alias, filter_processor_name=filter_processor_name, filter_category=filter_category, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->payment_methods_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_name** | **str**| Filtering by name. | [optional] 
 **filter_alias** | **str**| Filtering by alias. | [optional] 
 **filter_processor_name** | **str**| Filtering by processor_name. | [optional] 
 **filter_category** | [**list[str]**](str.md)| Filtering by category. | [optional] 
 **sort** | [**list[str]**](str.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | alias | -alias | | processor_name | -processor_name | | category | -category |  | [optional] 

### Return type

[**PaymentMethodsResponse**](PaymentMethodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_methods_id_get**
> PaymentMethodResponse payment_methods_id_get(id)

Payment method by ID

Returns payment method with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.PaymentMethodsApi()
id = 'id_example' # str | Unique ID.

try: 
    # Payment method by ID
    api_response = api_instance.payment_methods_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->payment_methods_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

