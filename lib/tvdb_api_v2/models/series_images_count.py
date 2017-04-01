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


class SeriesImagesCount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, fanart=None, poster=None, season=None, seasonwide=None, series=None):
        """
        SeriesImagesCount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fanart': 'int',
            'poster': 'int',
            'season': 'int',
            'seasonwide': 'int',
            'series': 'int'
        }

        self.attribute_map = {
            'fanart': 'fanart',
            'poster': 'poster',
            'season': 'season',
            'seasonwide': 'seasonwide',
            'series': 'series'
        }

        self._fanart = fanart
        self._poster = poster
        self._season = season
        self._seasonwide = seasonwide
        self._series = series

    @property
    def fanart(self):
        """
        Gets the fanart of this SeriesImagesCount.


        :return: The fanart of this SeriesImagesCount.
        :rtype: int
        """
        return self._fanart

    @fanart.setter
    def fanart(self, fanart):
        """
        Sets the fanart of this SeriesImagesCount.


        :param fanart: The fanart of this SeriesImagesCount.
        :type: int
        """

        self._fanart = fanart

    @property
    def poster(self):
        """
        Gets the poster of this SeriesImagesCount.


        :return: The poster of this SeriesImagesCount.
        :rtype: int
        """
        return self._poster

    @poster.setter
    def poster(self, poster):
        """
        Sets the poster of this SeriesImagesCount.


        :param poster: The poster of this SeriesImagesCount.
        :type: int
        """

        self._poster = poster

    @property
    def season(self):
        """
        Gets the season of this SeriesImagesCount.


        :return: The season of this SeriesImagesCount.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """
        Sets the season of this SeriesImagesCount.


        :param season: The season of this SeriesImagesCount.
        :type: int
        """

        self._season = season

    @property
    def seasonwide(self):
        """
        Gets the seasonwide of this SeriesImagesCount.


        :return: The seasonwide of this SeriesImagesCount.
        :rtype: int
        """
        return self._seasonwide

    @seasonwide.setter
    def seasonwide(self, seasonwide):
        """
        Sets the seasonwide of this SeriesImagesCount.


        :param seasonwide: The seasonwide of this SeriesImagesCount.
        :type: int
        """

        self._seasonwide = seasonwide

    @property
    def series(self):
        """
        Gets the series of this SeriesImagesCount.


        :return: The series of this SeriesImagesCount.
        :rtype: int
        """
        return self._series

    @series.setter
    def series(self, series):
        """
        Sets the series of this SeriesImagesCount.


        :param series: The series of this SeriesImagesCount.
        :type: int
        """

        self._series = series

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
