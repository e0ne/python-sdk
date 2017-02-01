# openfintech_sdk.PaymentProcessorsApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_processors_get**](PaymentProcessorsApi.md#payment_processors_get) | **GET** /payment-processors | List of payment processors
[**payment_processors_id_get**](PaymentProcessorsApi.md#payment_processors_id_get) | **GET** /payment-processors/{id} | Payment processor by ID


# **payment_processors_get**
> PaymentProcessorsResponse payment_processors_get(page_number=page_number, page_size=page_size, filter_name=filter_name)

List of payment processors

Returns all available payment processors. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.PaymentProcessorsApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_name = 'filter_name_example' # str | Filtering by name. (optional)

try: 
    # List of payment processors
    api_response = api_instance.payment_processors_get(page_number=page_number, page_size=page_size, filter_name=filter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentProcessorsApi->payment_processors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_name** | **str**| Filtering by name. | [optional] 

### Return type

[**PaymentProcessorsResponse**](PaymentProcessorsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_processors_id_get**
> PaymentProcessorResponse payment_processors_id_get(id)

Payment processor by ID

Returns payment processor with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.PaymentProcessorsApi()
id = 'id_example' # str | Unique ID.

try: 
    # Payment processor by ID
    api_response = api_instance.payment_processors_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentProcessorsApi->payment_processors_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**PaymentProcessorResponse**](PaymentProcessorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

