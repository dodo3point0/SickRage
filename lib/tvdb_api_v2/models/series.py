# coding: utf-8

"""
    TheTVDB API v2

    API v2 targets v1 functionality with a few minor additions.
    The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.

    OpenAPI spec version: 2.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Series(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, series_name=None, aliases=None, banner=None, series_id=None, status=None, first_aired=None, network=None, network_id=None, runtime=None, genre=None, overview=None, last_updated=None, airs_day_of_week=None, airs_time=None, rating=None, imdb_id=None, zap2it_id=None, added=None, site_rating=None, site_rating_count=None):
        """
        Series - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'series_name': 'str',
            'aliases': 'list[str]',
            'banner': 'str',
            'series_id': 'int',
            'status': 'str',
            'first_aired': 'str',
            'network': 'str',
            'network_id': 'str',
            'runtime': 'str',
            'genre': 'list[str]',
            'overview': 'str',
            'last_updated': 'int',
            'airs_day_of_week': 'str',
            'airs_time': 'str',
            'rating': 'str',
            'imdb_id': 'str',
            'zap2it_id': 'str',
            'added': 'str',
            'site_rating': 'float',
            'site_rating_count': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'series_name': 'seriesName',
            'aliases': 'aliases',
            'banner': 'banner',
            'series_id': 'seriesId',
            'status': 'status',
            'first_aired': 'firstAired',
            'network': 'network',
            'network_id': 'networkId',
            'runtime': 'runtime',
            'genre': 'genre',
            'overview': 'overview',
            'last_updated': 'lastUpdated',
            'airs_day_of_week': 'airsDayOfWeek',
            'airs_time': 'airsTime',
            'rating': 'rating',
            'imdb_id': 'imdbId',
            'zap2it_id': 'zap2itId',
            'added': 'added',
            'site_rating': 'siteRating',
            'site_rating_count': 'siteRatingCount'
        }

        self._id = id
        self._series_name = series_name
        self._aliases = aliases
        self._banner = banner
        self._series_id = series_id
        self._status = status
        self._first_aired = first_aired
        self._network = network
        self._network_id = network_id
        self._runtime = runtime
        self._genre = genre
        self._overview = overview
        self._last_updated = last_updated
        self._airs_day_of_week = airs_day_of_week
        self._airs_time = airs_time
        self._rating = rating
        self._imdb_id = imdb_id
        self._zap2it_id = zap2it_id
        self._added = added
        self._site_rating = site_rating
        self._site_rating_count = site_rating_count

    @property
    def id(self):
        """
        Gets the id of this Series.


        :return: The id of this Series.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Series.


        :param id: The id of this Series.
        :type: int
        """

        self._id = id

    @property
    def series_name(self):
        """
        Gets the series_name of this Series.


        :return: The series_name of this Series.
        :rtype: str
        """
        return self._series_name

    @series_name.setter
    def series_name(self, series_name):
        """
        Sets the series_name of this Series.


        :param series_name: The series_name of this Series.
        :type: str
        """

        self._series_name = series_name

    @property
    def aliases(self):
        """
        Gets the aliases of this Series.


        :return: The aliases of this Series.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this Series.


        :param aliases: The aliases of this Series.
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def banner(self):
        """
        Gets the banner of this Series.


        :return: The banner of this Series.
        :rtype: str
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """
        Sets the banner of this Series.


        :param banner: The banner of this Series.
        :type: str
        """

        self._banner = banner

    @property
    def series_id(self):
        """
        Gets the series_id of this Series.


        :return: The series_id of this Series.
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """
        Sets the series_id of this Series.


        :param series_id: The series_id of this Series.
        :type: int
        """

        self._series_id = series_id

    @property
    def status(self):
        """
        Gets the status of this Series.


        :return: The status of this Series.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Series.


        :param status: The status of this Series.
        :type: str
        """

        self._status = status

    @property
    def first_aired(self):
        """
        Gets the first_aired of this Series.


        :return: The first_aired of this Series.
        :rtype: str
        """
        return self._first_aired

    @first_aired.setter
    def first_aired(self, first_aired):
        """
        Sets the first_aired of this Series.


        :param first_aired: The first_aired of this Series.
        :type: str
        """

        self._first_aired = first_aired

    @property
    def network(self):
        """
        Gets the network of this Series.


        :return: The network of this Series.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """
        Sets the network of this Series.


        :param network: The network of this Series.
        :type: str
        """

        self._network = network

    @property
    def network_id(self):
        """
        Gets the network_id of this Series.


        :return: The network_id of this Series.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """
        Sets the network_id of this Series.


        :param network_id: The network_id of this Series.
        :type: str
        """

        self._network_id = network_id

    @property
    def runtime(self):
        """
        Gets the runtime of this Series.


        :return: The runtime of this Series.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtime of this Series.


        :param runtime: The runtime of this Series.
        :type: str
        """

        self._runtime = runtime

    @property
    def genre(self):
        """
        Gets the genre of this Series.


        :return: The genre of this Series.
        :rtype: list[str]
        """
        return self._genre

    @genre.setter
    def genre(self, genre):
        """
        Sets the genre of this Series.


        :param genre: The genre of this Series.
        :type: list[str]
        """

        self._genre = genre

    @property
    def overview(self):
        """
        Gets the overview of this Series.


        :return: The overview of this Series.
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """
        Sets the overview of this Series.


        :param overview: The overview of this Series.
        :type: str
        """

        self._overview = overview

    @property
    def last_updated(self):
        """
        Gets the last_updated of this Series.


        :return: The last_updated of this Series.
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this Series.


        :param last_updated: The last_updated of this Series.
        :type: int
        """

        self._last_updated = last_updated

    @property
    def airs_day_of_week(self):
        """
        Gets the airs_day_of_week of this Series.


        :return: The airs_day_of_week of this Series.
        :rtype: str
        """
        return self._airs_day_of_week

    @airs_day_of_week.setter
    def airs_day_of_week(self, airs_day_of_week):
        """
        Sets the airs_day_of_week of this Series.


        :param airs_day_of_week: The airs_day_of_week of this Series.
        :type: str
        """

        self._airs_day_of_week = airs_day_of_week

    @property
    def airs_time(self):
        """
        Gets the airs_time of this Series.


        :return: The airs_time of this Series.
        :rtype: str
        """
        return self._airs_time

    @airs_time.setter
    def airs_time(self, airs_time):
        """
        Sets the airs_time of this Series.


        :param airs_time: The airs_time of this Series.
        :type: str
        """

        self._airs_time = airs_time

    @property
    def rating(self):
        """
        Gets the rating of this Series.


        :return: The rating of this Series.
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """
        Sets the rating of this Series.


        :param rating: The rating of this Series.
        :type: str
        """

        self._rating = rating

    @property
    def imdb_id(self):
        """
        Gets the imdb_id of this Series.


        :return: The imdb_id of this Series.
        :rtype: str
        """
        return self._imdb_id

    @imdb_id.setter
    def imdb_id(self, imdb_id):
        """
        Sets the imdb_id of this Series.


        :param imdb_id: The imdb_id of this Series.
        :type: str
        """

        self._imdb_id = imdb_id

    @property
    def zap2it_id(self):
        """
        Gets the zap2it_id of this Series.


        :return: The zap2it_id of this Series.
        :rtype: str
        """
        return self._zap2it_id

    @zap2it_id.setter
    def zap2it_id(self, zap2it_id):
        """
        Sets the zap2it_id of this Series.


        :param zap2it_id: The zap2it_id of this Series.
        :type: str
        """

        self._zap2it_id = zap2it_id

    @property
    def added(self):
        """
        Gets the added of this Series.


        :return: The added of this Series.
        :rtype: str
        """
        return self._added

    @added.setter
    def added(self, added):
        """
        Sets the added of this Series.


        :param added: The added of this Series.
        :type: str
        """

        self._added = added

    @property
    def site_rating(self):
        """
        Gets the site_rating of this Series.


        :return: The site_rating of this Series.
        :rtype: float
        """
        return self._site_rating

    @site_rating.setter
    def site_rating(self, site_rating):
        """
        Sets the site_rating of this Series.


        :param site_rating: The site_rating of this Series.
        :type: float
        """

        self._site_rating = site_rating

    @property
    def site_rating_count(self):
        """
        Gets the site_rating_count of this Series.


        :return: The site_rating_count of this Series.
        :rtype: int
        """
        return self._site_rating_count

    @site_rating_count.setter
    def site_rating_count(self, site_rating_count):
        """
        Sets the site_rating_count of this Series.


        :param site_rating_count: The site_rating_count of this Series.
        :type: int
        """

        self._site_rating_count = site_rating_count

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
