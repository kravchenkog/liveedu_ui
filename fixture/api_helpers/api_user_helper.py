import random
import requests
import json
import time

class APIHelper:

    def general_get(self, app, route):
        url = str(app.env.base_url) + str(route)

        response = requests.request("GET", url, headers=app.env.headers, params=app.env.params, cookies = app.env.cookies)
        try:
            responce_j = json.loads(response.text)
            responce_j['status_code'] = response.status_code

            return responce_j

        except:
            print(str(response))

    def general_post(self, app, route, data):
        url = str(app.env.base_url) + str(route)
        if data is None:
            data = {}
        if len(app.env.headers) > 1:
            data = json.dumps(data)

        responce = requests.request("POST", url, data=data, headers=app.env.headers, cookies = app.env.cookies)
        try:
            responce_j = json.loads(responce.text)
            responce_j['status_code'] = responce.status_code

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

    def get_all_names_topics(self, app, route):
        topics = self.general_get(app, route)
        slugs = []
        for topic in topics['results']:

           slugs.append(topic['name'])

        return slugs

    def get_random_slug_topic(self, app):
        list_of_slugs = self.get_all_slug_topics(app, route=app.route.topics)
        random_slug = list_of_slugs[random.randint(0, len(list_of_slugs) - 1)]
        return random_slug

    def get_random_name_topic(self, app):
        list_of_names = self.get_all_names_topics(app, route=app.route.topics)
        random_name = list_of_names[random.randint(0, len(list_of_names) - 1)]
        return random_name

    def get_random_list_of_slugs(self, app):
        list_of_all = self.get_all_slug_topics(app, route=app.route.topics)
        no_el = random.randint(1, len(list_of_all) - 1)
        list_slugs = []
        for el in range(no_el):
            x = random.choice(list_of_all)
            list_slugs.append(x)
            list_of_all.remove(x)
        return list_slugs

    def get_registered_user(self, app, user, role):
        user.password1, user.password2 = app.string.get_random_two_passwords()
        user.email = app.string.get_random_email()
        user.username = app.string.get_random_username()
        user.userrole = role
        user.slug = self.get_random_list_of_slugs(app)
        data = {'email': user.email,
                'password1': user.password1,
                'password2': user.password2,
                'username': user.username,
                'user_role': user.userrole,
                'want_learn': user.slug,
                'skype': '123',
                'hangouts': 'sdfsdf'}
        response_reg = self.general_post(app=app, route=app.route.register, data=data)
        print(str(data))
        print(str(response_reg))
        return user

    def email_confirmation(self, app, user):
        data_confirm = {'email': user.email, 'key': '992927E5B1C8A237875C70A302A34E22'}
        return self.general_post(app=app, route=app.route.email_confirmation, data=data_confirm)

    def get_confirmed_user(self, app, user, role='streamer'):
        user = self.get_registered_user(app, user, role)
        time.sleep(1)
        response = self.email_confirmation(app, user)
        print("____________________________________")
        print(response)
        print(user.email)
        print("____________________________________")
        return user

    def login_perform(self, app):
        response_login = self.general_post(
            app=app,
            route=app.route.login,
            data={
                'username': app.user_data.username,
                'password': app.user_data.password1
                  })
        return response_login

    def login_perform_and_parse_fields(self, app):
        resp_log = self.login_perform(app=app)
        resp_log['user']['token'] = resp_log['token']
        app.user_parse.parse_user_properties(resp_dict=resp_log['user'], app=app)
        return app
