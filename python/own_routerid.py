from helper_functions import functions
class own_routerinfo:

    def routerId(self):
        object=functions()
        soup=object.get_table_htmlfile('http://127.0.0.1:7657/netdb?r=.')
        router_identity_element = soup.find('th', {'id': 'our-info'})
        router_identity_value = router_identity_element.find('code').text
        print("Router Identity:", router_identity_value)
        return router_identity_value