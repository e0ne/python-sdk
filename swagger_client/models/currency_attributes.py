# coding: utf-8

"""
    OpenFinTech.io API

    # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://s3-eu-west-1.amazonaws.com/uploads-eu.hipchat.com/386820/4572695/rRdwJEYiMkoJrSR/Openfintech%20Design%20Model%20Public.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io     Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-01-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Exanple of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=alias`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=alias`] points to ascending sorting, negative  [e.g. `?sort=-alias`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=alias, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 

    OpenAPI spec version: 2017-01-24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CurrencyAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, currency_type=None, code_iso_alpha3=None, code_iso_numeric3=None, name=None, symbol=None, native_symbol=None, decimal_e=None, code_estandarts_alpha=None, code_json_alpha=None, category=None, created=None, icon=None, issuer=None):
        """
        CurrencyAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'currency_type': 'str',
            'code_iso_alpha3': 'str',
            'code_iso_numeric3': 'int',
            'name': 'str',
            'symbol': 'str',
            'native_symbol': 'str',
            'decimal_e': 'str',
            'code_estandarts_alpha': 'str',
            'code_json_alpha': 'str',
            'category': 'str',
            'created': 'str',
            'icon': 'str',
            'issuer': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'currency_type': 'currency_type',
            'code_iso_alpha3': 'code_iso_alpha3',
            'code_iso_numeric3': 'code_iso_numeric3',
            'name': 'name',
            'symbol': 'symbol',
            'native_symbol': 'native_symbol',
            'decimal_e': 'decimal_e',
            'code_estandarts_alpha': 'code_estandarts_alpha',
            'code_json_alpha': 'code_json_alpha',
            'category': 'category',
            'created': 'created',
            'icon': 'icon',
            'issuer': 'issuer'
        }

        self._code = code
        self._currency_type = currency_type
        self._code_iso_alpha3 = code_iso_alpha3
        self._code_iso_numeric3 = code_iso_numeric3
        self._name = name
        self._symbol = symbol
        self._native_symbol = native_symbol
        self._decimal_e = decimal_e
        self._code_estandarts_alpha = code_estandarts_alpha
        self._code_json_alpha = code_json_alpha
        self._category = category
        self._created = created
        self._icon = icon
        self._issuer = issuer

    @property
    def code(self):
        """
        Gets the code of this CurrencyAttributes.
        Currency system code

        :return: The code of this CurrencyAttributes.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CurrencyAttributes.
        Currency system code

        :param code: The code of this CurrencyAttributes.
        :type: str
        """

        self._code = code

    @property
    def currency_type(self):
        """
        Gets the currency_type of this CurrencyAttributes.
        Type of currencies [national, digital, virtual, metal, energy]

        :return: The currency_type of this CurrencyAttributes.
        :rtype: str
        """
        return self._currency_type

    @currency_type.setter
    def currency_type(self, currency_type):
        """
        Sets the currency_type of this CurrencyAttributes.
        Type of currencies [national, digital, virtual, metal, energy]

        :param currency_type: The currency_type of this CurrencyAttributes.
        :type: str
        """

        self._currency_type = currency_type

    @property
    def code_iso_alpha3(self):
        """
        Gets the code_iso_alpha3 of this CurrencyAttributes.
        Currency ISO code

        :return: The code_iso_alpha3 of this CurrencyAttributes.
        :rtype: str
        """
        return self._code_iso_alpha3

    @code_iso_alpha3.setter
    def code_iso_alpha3(self, code_iso_alpha3):
        """
        Sets the code_iso_alpha3 of this CurrencyAttributes.
        Currency ISO code

        :param code_iso_alpha3: The code_iso_alpha3 of this CurrencyAttributes.
        :type: str
        """

        self._code_iso_alpha3 = code_iso_alpha3

    @property
    def code_iso_numeric3(self):
        """
        Gets the code_iso_numeric3 of this CurrencyAttributes.
        Currency ISO numeric code

        :return: The code_iso_numeric3 of this CurrencyAttributes.
        :rtype: int
        """
        return self._code_iso_numeric3

    @code_iso_numeric3.setter
    def code_iso_numeric3(self, code_iso_numeric3):
        """
        Sets the code_iso_numeric3 of this CurrencyAttributes.
        Currency ISO numeric code

        :param code_iso_numeric3: The code_iso_numeric3 of this CurrencyAttributes.
        :type: int
        """

        self._code_iso_numeric3 = code_iso_numeric3

    @property
    def name(self):
        """
        Gets the name of this CurrencyAttributes.
        Currency description

        :return: The name of this CurrencyAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CurrencyAttributes.
        Currency description

        :param name: The name of this CurrencyAttributes.
        :type: str
        """

        self._name = name

    @property
    def symbol(self):
        """
        Gets the symbol of this CurrencyAttributes.
        Currency’s symbol. In general, only for nationals currencies

        :return: The symbol of this CurrencyAttributes.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this CurrencyAttributes.
        Currency’s symbol. In general, only for nationals currencies

        :param symbol: The symbol of this CurrencyAttributes.
        :type: str
        """

        self._symbol = symbol

    @property
    def native_symbol(self):
        """
        Gets the native_symbol of this CurrencyAttributes.
        Currency’s symbol. In general, only for nationals currencies

        :return: The native_symbol of this CurrencyAttributes.
        :rtype: str
        """
        return self._native_symbol

    @native_symbol.setter
    def native_symbol(self, native_symbol):
        """
        Sets the native_symbol of this CurrencyAttributes.
        Currency’s symbol. In general, only for nationals currencies

        :param native_symbol: The native_symbol of this CurrencyAttributes.
        :type: str
        """

        self._native_symbol = native_symbol

    @property
    def decimal_e(self):
        """
        Gets the decimal_e of this CurrencyAttributes.
        Number of digits after the decimal separator

        :return: The decimal_e of this CurrencyAttributes.
        :rtype: str
        """
        return self._decimal_e

    @decimal_e.setter
    def decimal_e(self, decimal_e):
        """
        Sets the decimal_e of this CurrencyAttributes.
        Number of digits after the decimal separator

        :param decimal_e: The decimal_e of this CurrencyAttributes.
        :type: str
        """

        self._decimal_e = decimal_e

    @property
    def code_estandarts_alpha(self):
        """
        Gets the code_estandarts_alpha of this CurrencyAttributes.

        :return: The code_estandarts_alpha of this CurrencyAttributes.
        :rtype: str
        """
        return self._code_estandarts_alpha

    @code_estandarts_alpha.setter
    def code_estandarts_alpha(self, code_estandarts_alpha):
        """
        Sets the code_estandarts_alpha of this CurrencyAttributes.

        :param code_estandarts_alpha: The code_estandarts_alpha of this CurrencyAttributes.
        :type: str
        """

        self._code_estandarts_alpha = code_estandarts_alpha

    @property
    def code_json_alpha(self):
        """
        Gets the code_json_alpha of this CurrencyAttributes.

        :return: The code_json_alpha of this CurrencyAttributes.
        :rtype: str
        """
        return self._code_json_alpha

    @code_json_alpha.setter
    def code_json_alpha(self, code_json_alpha):
        """
        Sets the code_json_alpha of this CurrencyAttributes.

        :param code_json_alpha: The code_json_alpha of this CurrencyAttributes.
        :type: str
        """

        self._code_json_alpha = code_json_alpha

    @property
    def category(self):
        """
        Gets the category of this CurrencyAttributes.
        Currency category

        :return: The category of this CurrencyAttributes.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this CurrencyAttributes.
        Currency category

        :param category: The category of this CurrencyAttributes.
        :type: str
        """

        self._category = category

    @property
    def created(self):
        """
        Gets the created of this CurrencyAttributes.
        Created in system

        :return: The created of this CurrencyAttributes.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this CurrencyAttributes.
        Created in system

        :param created: The created of this CurrencyAttributes.
        :type: str
        """

        self._created = created

    @property
    def icon(self):
        """
        Gets the icon of this CurrencyAttributes.
        Link to currency`s icon

        :return: The icon of this CurrencyAttributes.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this CurrencyAttributes.
        Link to currency`s icon

        :param icon: The icon of this CurrencyAttributes.
        :type: str
        """

        self._icon = icon

    @property
    def issuer(self):
        """
        Gets the issuer of this CurrencyAttributes.
        Currency`s issuer

        :return: The issuer of this CurrencyAttributes.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this CurrencyAttributes.
        Currency`s issuer

        :param issuer: The issuer of this CurrencyAttributes.
        :type: str
        """

        self._issuer = issuer

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
