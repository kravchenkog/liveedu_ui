import random

import requests
import json


class APIHelper:

    def general_get(self, app, route):
        url = str(app.env.base_url) + str(route)

        response = requests.request("GET", url, headers=app.env.headers)
        try:
            response_dict = json.loads(response.text)
            print(response_dict)
            print(url)
            print(app.env.headers)
            return response_dict

        except:
            print(str(response))

    def general_post(self, app, route, data):
        url = str(app.env.base_url) + str(route)
        if data is None:
            data = {}
        if len(app.env.headers) > 1:
            data = json.dumps(data)

        responce = requests.request("POST", url, data=data, headers=app.env.headers)
        try:
            responce_j = json.loads(responce.text)
            responce_j['status_code'] = responce.status_code
            print(responce_j)
            print(url)
            print(app.env.headers)
            print(data)
            return responce_j
        except:
            print("_____________________________ERROR_JSON_LOADS_______________________________")
            print(responce.text)

    def get_all_slug_topics(self, app, route):
        topics = self.general_get(app, route)
        slugs = []
        for topic in topics['results']:

           slugs.append(topic['slug'])

        return slugs

    def get_random_slug_topic(self, app):
        list_of_slugs = self.get_all_slug_topics(app, route=app.route.topics)
        random_slug = list_of_slugs[random.randint(0, len(list_of_slugs) - 1)]
        return random_slug

    def get_random_list_of_slugs(self, app):
        list_of_all = self.get_all_slug_topics(app, route=app.route.topics)
        no_el = random.randint(0, len(list_of_all) - 1)
        list_slugs = []
        for el in range(no_el):
            x = random.choice(list_of_all)
            list_slugs.append(x)
            list_of_all.remove(x)
        return list_slugs
