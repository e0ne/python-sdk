# swagger_client.CountriesApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countries_get**](CountriesApi.md#countries_get) | **GET** /countries | List of countries
[**countries_id_get**](CountriesApi.md#countries_id_get) | **GET** /countries/{id} | Country by ID


# **countries_get**
> CountriesResponse countries_get(page_number=page_number, page_size=page_size, filter_region=filter_region, filter_sub_region=filter_sub_region, sort=sort)

List of countries

Returns all available countries. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CountriesApi()
page_number = 56 # int | Current page number. (optional)
page_size = 56 # int | Page size.<br>*Default value: 100*  (optional)
filter_region = ['filter_region_example'] # list[str] | Filtration by region. (optional)
filter_sub_region = ['filter_sub_region_example'] # list[str] | Filtration by sub region. (optional)
sort = ['sort_example'] # list[str] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | area | -area | | population | -population | | region | -region | | sub_region | -sub_region |  (optional)

try: 
    # List of countries
    api_response = api_instance.countries_get(page_number=page_number, page_size=page_size, filter_region=filter_region, filter_sub_region=filter_sub_region, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->countries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page number. | [optional] 
 **page_size** | **int**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filter_region** | [**list[str]**](str.md)| Filtration by region. | [optional] 
 **filter_sub_region** | [**list[str]**](str.md)| Filtration by sub region. | [optional] 
 **sort** | [**list[str]**](str.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | area | -area | | population | -population | | region | -region | | sub_region | -sub_region |  | [optional] 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countries_id_get**
> CountryResponse countries_id_get(id)

Country by ID

Returns country with specific ID. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CountriesApi()
id = 'id_example' # str | Unique ID.

try: 
    # Country by ID
    api_response = api_instance.countries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->countries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID. | 

### Return type

[**CountryResponse**](CountryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

