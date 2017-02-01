# coding: utf-8

"""
    OpenFinTech.io API

    # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://s3-eu-west-1.amazonaws.com/uploads-eu.hipchat.com/386820/4572695/rRdwJEYiMkoJrSR/Openfintech%20Design%20Model%20Public.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io     Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-01-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Exanple of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=alias`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=alias`] points to ascending sorting, negative  [e.g. `?sort=-alias`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=alias, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 

    OpenAPI spec version: 2017-01-24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import io
import json
import ssl
import certifi
import logging
import re

# python 2 and python 3 compatibility library
from six import PY3
from six.moves.urllib.parse import urlencode

from .configuration import Configuration

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """
        Returns a dictionary of the response headers.
        """
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """
        Returns a given response header.
        """
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, pools_size=4, maxsize=4):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680
        # maxsize is the number of requests to host that are allowed in parallel
        # ca_certs vs cert_file vs key_file
        # http://stackoverflow.com/a/23957365/2985775

        # cert_reqs
        if Configuration().verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if Configuration().ssl_ca_cert:
            ca_certs = Configuration().ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        # cert_file
        cert_file = Configuration().cert_file

        # key file
        key_file = Configuration().key_file

        # https pool manager
        self.pool_manager = urllib3.PoolManager(
            num_pools=pools_size,
            maxsize=maxsize,
            cert_reqs=cert_reqs,
            ca_certs=ca_certs,
            cert_file=cert_file,
            key_file=key_file
        )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True, _request_timeout=None):
        """
        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will be returned without
                                 reading/decoding response data. Default is True.
        :param _request_timeout: timeout setting for this request. If one number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, ) if PY3 else (int, long)):
                timeout = urllib3.Timeout(total=_request_timeout)
            elif isinstance(_request_timeout, tuple) and len(_request_timeout) == 2:
                timeout = urllib3.Timeout(connect=_request_timeout[0], read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = None
                    if body:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(method, url,
                                                  body=request_body,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=False,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct Content-Type
                    # which generated by urllib3 will be overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(method, url,
                                                  fields=post_params,
                                                  encode_multipart=True,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is provided
                # in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(method, url,
                                                  body=request_body,
                                                  preload_content=_preload_content,
                                                  timeout=timeout,
                                                  headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided arguments.
                             Please check that your arguments match declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # In the python 3, the response.data is bytes.
            # we need to decode it to string.
            if PY3:
                r.data = r.data.decode('utf8')

            # log response body
            logger.debug("response body: %s", r.data)

        if r.status not in range(200, 206):
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None, _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
             _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
            _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
              _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """
        Custom error messages for exception
        """
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
