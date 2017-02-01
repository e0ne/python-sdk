# openfintech_sdk.CurrenciesApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currencies_get**](CurrenciesApi.md#currencies_get) | **GET** /currencies | List of currencies
[**currencies_id_get**](CurrenciesApi.md#currencies_id_get) | **GET** /currencies/{id} | Currency by ID


# **currencies_get**
> CurrenciesResponse currencies_get(page_number=page_number, page_size=page_size, filter_code_iso_alpha3=filter_code_iso_alpha3, filter_code_iso_numeric3=filter_code_iso_numeric3, filter_code_estandards_alpha=filter_code_estandards_alpha, filter_currency_type=filter_currency_type, filter_category=filter_category, sort=sort)

List of currencies

Returns all available currencies. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.CurrenciesApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_code_iso_alpha3 = 'filter_code_iso_alpha3_example' # str | Filtering by ISO code. (optional)
filter_code_iso_numeric3 = 56 # int | Filtering by ISO number. (optional)
filter_code_estandards_alpha = 'filter_code_estandards_alpha_example' # str | Filtering by estandards code. (optional)
filter_currency_type = ['filter_currency_type_example'] # list[str] | Filtration by currency type. (optional)
filter_category = ['filter_category_example'] # list[str] | Filtration by category. (optional)
sort = ['sort_example'] # list[str] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  (optional)

try: 
    # List of currencies
    api_response = api_instance.currencies_get(page_number=page_number, page_size=page_size, filter_code_iso_alpha3=filter_code_iso_alpha3, filter_code_iso_numeric3=filter_code_iso_numeric3, filter_code_estandards_alpha=filter_code_estandards_alpha, filter_currency_type=filter_currency_type, filter_category=filter_category, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_code_iso_alpha3** | **str**| Filtering by ISO code. | [optional] 
 **filter_code_iso_numeric3** | **int**| Filtering by ISO number. | [optional] 
 **filter_code_estandards_alpha** | **str**| Filtering by estandards code. | [optional] 
 **filter_currency_type** | [**list[str]**](str.md)| Filtration by currency type. | [optional] 
 **filter_category** | [**list[str]**](str.md)| Filtration by category. | [optional] 
 **sort** | [**list[str]**](str.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  | [optional] 

### Return type

[**CurrenciesResponse**](CurrenciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currencies_id_get**
> CurrencyResponse currencies_id_get(id)

Currency by ID

Returns currency with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import openfintech_sdk
from openfintech_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openfintech_sdk.CurrenciesApi()
id = 'id_example' # str | Unique ID.

try: 
    # Currency by ID
    api_response = api_instance.currencies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**CurrencyResponse**](CurrencyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

