# coding: utf-8

"""
    OpenFinTech.io API

    # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://s3-eu-west-1.amazonaws.com/uploads-eu.hipchat.com/386820/4572695/rRdwJEYiMkoJrSR/Openfintech%20Design%20Model%20Public.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io     Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-01-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Exanple of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=alias`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=alias`] points to ascending sorting, negative  [e.g. `?sort=-alias`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=alias, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 

    OpenAPI spec version: 2017-01-24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .bank import Bank
from .bank_attributes import BankAttributes
from .bank_organization import BankOrganization
from .bank_organization_data import BankOrganizationData
from .bank_organization_links import BankOrganizationLinks
from .bank_relationships import BankRelationships
from .bank_response import BankResponse
from .banks_response import BanksResponse
from .countries_response import CountriesResponse
from .country import Country
from .country_attributes import CountryAttributes
from .country_relationships import CountryRelationships
from .country_response import CountryResponse
from .country_translations import CountryTranslations
from .country_translations_links import CountryTranslationsLinks
from .currencies_response import CurrenciesResponse
from .currency import Currency
from .currency_attributes import CurrencyAttributes
from .currency_countries import CurrencyCountries
from .currency_country_links import CurrencyCountryLinks
from .currency_issuer_organization import CurrencyIssuerOrganization
from .currency_issuer_organization_data import CurrencyIssuerOrganizationData
from .currency_issuer_organization_links import CurrencyIssuerOrganizationLinks
from .currency_parent import CurrencyParent
from .currency_parent_data import CurrencyParentData
from .currency_parent_links import CurrencyParentLinks
from .currency_relationships import CurrencyRelationships
from .currency_response import CurrencyResponse
from .exchanger import Exchanger
from .exchanger_attributes import ExchangerAttributes
from .exchanger_attributes_organization import ExchangerAttributesOrganization
from .exchanger_organization import ExchangerOrganization
from .exchanger_organization_data import ExchangerOrganizationData
from .exchanger_organization_links import ExchangerOrganizationLinks
from .exchanger_relationships import ExchangerRelationships
from .exchanger_response import ExchangerResponse
from .exchangers_response import ExchangersResponse
from .industries_response import IndustriesResponse
from .industry import Industry
from .industry_attributes import IndustryAttributes
from .industry_response import IndustryResponse
from .issuer import Issuer
from .issuer_attribute import IssuerAttribute
from .issuer_organization import IssuerOrganization
from .issuer_organization_data import IssuerOrganizationData
from .issuer_organization_links import IssuerOrganizationLinks
from .issuer_relationships import IssuerRelationships
from .issuer_response import IssuerResponse
from .issuers_response import IssuersResponse
from .merchant_industries_response import MerchantIndustriesResponse
from .merchant_industry import MerchantIndustry
from .merchant_industry_attributes import MerchantIndustryAttributes
from .merchant_industry_response import MerchantIndustryResponse
from .organization import Organization
from .organization_active import OrganizationActive
from .organization_active_links import OrganizationActiveLinks
from .organization_address import OrganizationAddress
from .organization_attributes import OrganizationAttributes
from .organization_contacts import OrganizationContacts
from .organization_hq import OrganizationHq
from .organization_hq_links import OrganizationHqLinks
from .organization_relationships import OrganizationRelationships
from .organization_response import OrganizationResponse
from .organization_social import OrganizationSocial
from .organization_source import OrganizationSource
from .organization_source_links import OrganizationSourceLinks
from .organizations_response import OrganizationsResponse
from .payment_method import PaymentMethod
from .payment_method_attributes import PaymentMethodAttributes
from .payment_method_processor import PaymentMethodProcessor
from .payment_method_processor_data import PaymentMethodProcessorData
from .payment_method_processor_links import PaymentMethodProcessorLinks
from .payment_method_relationships import PaymentMethodRelationships
from .payment_method_response import PaymentMethodResponse
from .payment_methods_response import PaymentMethodsResponse
from .payment_processor import PaymentProcessor
from .payment_processor_attributes import PaymentProcessorAttributes
from .payment_processor_organization import PaymentProcessorOrganization
from .payment_processor_organization_data import PaymentProcessorOrganizationData
from .payment_processor_organization_links import PaymentProcessorOrganizationLinks
from .payment_processor_relationships import PaymentProcessorRelationships
from .payment_processor_response import PaymentProcessorResponse
from .payment_processors_response import PaymentProcessorsResponse
from .payment_provider import PaymentProvider
from .payment_provider_attributes import PaymentProviderAttributes
from .payment_provider_organization import PaymentProviderOrganization
from .payment_provider_organization_data import PaymentProviderOrganizationData
from .payment_provider_organization_links import PaymentProviderOrganizationLinks
from .payment_provider_relationships import PaymentProviderRelationships
from .payment_provider_response import PaymentProviderResponse
from .payment_providers_response import PaymentProvidersResponse
from .response_links import ResponseLinks
from .response_meta import ResponseMeta
from .self_links import SelfLinks
