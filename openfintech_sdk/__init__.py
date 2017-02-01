# coding: utf-8

"""
    OpenFinTech.io API

    # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://s3-eu-west-1.amazonaws.com/uploads-eu.hipchat.com/386820/4572695/rRdwJEYiMkoJrSR/Openfintech%20Design%20Model%20Public.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io     Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-01-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Exanple of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=alias`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=alias`] points to ascending sorting, negative  [e.g. `?sort=-alias`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=alias, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 

    OpenAPI spec version: 2017-01-24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.bank import Bank
from .models.bank_attributes import BankAttributes
from .models.bank_organization import BankOrganization
from .models.bank_organization_data import BankOrganizationData
from .models.bank_organization_links import BankOrganizationLinks
from .models.bank_relationships import BankRelationships
from .models.bank_response import BankResponse
from .models.banks_response import BanksResponse
from .models.countries_response import CountriesResponse
from .models.country import Country
from .models.country_attributes import CountryAttributes
from .models.country_relationships import CountryRelationships
from .models.country_response import CountryResponse
from .models.country_translations import CountryTranslations
from .models.country_translations_links import CountryTranslationsLinks
from .models.currencies_response import CurrenciesResponse
from .models.currency import Currency
from .models.currency_attributes import CurrencyAttributes
from .models.currency_countries import CurrencyCountries
from .models.currency_country_links import CurrencyCountryLinks
from .models.currency_issuer_organization import CurrencyIssuerOrganization
from .models.currency_issuer_organization_data import CurrencyIssuerOrganizationData
from .models.currency_issuer_organization_links import CurrencyIssuerOrganizationLinks
from .models.currency_parent import CurrencyParent
from .models.currency_parent_data import CurrencyParentData
from .models.currency_parent_links import CurrencyParentLinks
from .models.currency_relationships import CurrencyRelationships
from .models.currency_response import CurrencyResponse
from .models.exchanger import Exchanger
from .models.exchanger_attributes import ExchangerAttributes
from .models.exchanger_attributes_organization import ExchangerAttributesOrganization
from .models.exchanger_organization import ExchangerOrganization
from .models.exchanger_organization_data import ExchangerOrganizationData
from .models.exchanger_organization_links import ExchangerOrganizationLinks
from .models.exchanger_relationships import ExchangerRelationships
from .models.exchanger_response import ExchangerResponse
from .models.exchangers_response import ExchangersResponse
from .models.industries_response import IndustriesResponse
from .models.industry import Industry
from .models.industry_attributes import IndustryAttributes
from .models.industry_response import IndustryResponse
from .models.issuer import Issuer
from .models.issuer_attribute import IssuerAttribute
from .models.issuer_organization import IssuerOrganization
from .models.issuer_organization_data import IssuerOrganizationData
from .models.issuer_organization_links import IssuerOrganizationLinks
from .models.issuer_relationships import IssuerRelationships
from .models.issuer_response import IssuerResponse
from .models.issuers_response import IssuersResponse
from .models.merchant_industries_response import MerchantIndustriesResponse
from .models.merchant_industry import MerchantIndustry
from .models.merchant_industry_attributes import MerchantIndustryAttributes
from .models.merchant_industry_response import MerchantIndustryResponse
from .models.organization import Organization
from .models.organization_active import OrganizationActive
from .models.organization_active_links import OrganizationActiveLinks
from .models.organization_address import OrganizationAddress
from .models.organization_attributes import OrganizationAttributes
from .models.organization_contacts import OrganizationContacts
from .models.organization_hq import OrganizationHq
from .models.organization_hq_links import OrganizationHqLinks
from .models.organization_relationships import OrganizationRelationships
from .models.organization_response import OrganizationResponse
from .models.organization_social import OrganizationSocial
from .models.organization_source import OrganizationSource
from .models.organization_source_links import OrganizationSourceLinks
from .models.organizations_response import OrganizationsResponse
from .models.payment_method import PaymentMethod
from .models.payment_method_attributes import PaymentMethodAttributes
from .models.payment_method_processor import PaymentMethodProcessor
from .models.payment_method_processor_data import PaymentMethodProcessorData
from .models.payment_method_processor_links import PaymentMethodProcessorLinks
from .models.payment_method_relationships import PaymentMethodRelationships
from .models.payment_method_response import PaymentMethodResponse
from .models.payment_methods_response import PaymentMethodsResponse
from .models.payment_processor import PaymentProcessor
from .models.payment_processor_attributes import PaymentProcessorAttributes
from .models.payment_processor_organization import PaymentProcessorOrganization
from .models.payment_processor_organization_data import PaymentProcessorOrganizationData
from .models.payment_processor_organization_links import PaymentProcessorOrganizationLinks
from .models.payment_processor_relationships import PaymentProcessorRelationships
from .models.payment_processor_response import PaymentProcessorResponse
from .models.payment_processors_response import PaymentProcessorsResponse
from .models.payment_provider import PaymentProvider
from .models.payment_provider_attributes import PaymentProviderAttributes
from .models.payment_provider_organization import PaymentProviderOrganization
from .models.payment_provider_organization_data import PaymentProviderOrganizationData
from .models.payment_provider_organization_links import PaymentProviderOrganizationLinks
from .models.payment_provider_relationships import PaymentProviderRelationships
from .models.payment_provider_response import PaymentProviderResponse
from .models.payment_providers_response import PaymentProvidersResponse
from .models.response_links import ResponseLinks
from .models.response_meta import ResponseMeta
from .models.self_links import SelfLinks

# import apis into sdk package
from .apis.banks_api import BanksApi
from .apis.countries_api import CountriesApi
from .apis.currencies_api import CurrenciesApi
from .apis.exchangers_api import ExchangersApi
from .apis.industries_api import IndustriesApi
from .apis.issuers_api import IssuersApi
from .apis.merchant_industries_api import MerchantIndustriesApi
from .apis.organizations_api import OrganizationsApi
from .apis.payment_methods_api import PaymentMethodsApi
from .apis.payment_processors_api import PaymentProcessorsApi
from .apis.payment_providers_api import PaymentProvidersApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
