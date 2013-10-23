# coding: utf-8

import json

from flask import Blueprint, current_app, jsonify, request, Response

import haul


app = current_app
api = Blueprint('api', __name__)


class APIErrorResponse(Exception):
    def __init__(self, message, status_code=400):
        Exception.__init__(self)

        self.message = message
        self.status_code = status_code

    def to_dict(self):
        data = {}
        data['error'] = {}
        data['error']['message'] = self.message
        data['error']['status_code'] = self.status_code

        return data


@api.errorhandler(APIErrorResponse)
def handle_api_error_response(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code

    return response


@api.route('/find_images/', methods=['GET', 'POST'])
def find_images():
    if u'application/json' in request.headers.get('Content-Type', None):
        data = request.get_json()
        url = data.get('url')
        extend = data.get('extend')
    else:
        url = request.values.get('url')
        extend = request.values.get('extend') in ['on', 'true', '1']

    app.logger.info('[find_images] url: %s' % (url))

    try:
        result = haul.find_images(url, extend=extend)
    except haul.exceptions.InvalidParameterError as e:
        raise APIErrorResponse('This URL is invalid')
    except haul.exceptions.ContentTypeNotSupported as e:
        raise APIErrorResponse('Content-Type is not supported: %s' % (e.content_type))
    except haul.exceptions.RetrieveError:
        raise APIErrorResponse('Can not fetch this URL')

    output = result.to_ordered_dict()

    # jsonify() don't preserve dict order
    json_output = json.dumps(output, indent=2)
    response = Response(response=json_output, status=200, mimetype='application/json')

    return response
