from keycloak import KeycloakAdmin
from config import ConfigClass
import requests
class OperationsAdmin:
    def __init__(
        self, 
        realm_name,
        server_url=ConfigClass.KEYCLOAK_SERVER_URL, 
        username=ConfigClass.ADMIN_USERNAME, 
        password=ConfigClass.ADMIN_PASSWORD, 
        client_id=ConfigClass.KEYCLOAK['canarie'][0],
        client_secret_key=ConfigClass.KEYCLOAK['canarie'][1], 
        verify=True):
        self.keycloak_admin = KeycloakAdmin(
            server_url=server_url,
            client_id=client_id,
            client_secret_key=client_secret_key,
            realm_name=realm_name,
            verify = verify,
            username = username, 
            password = password)
            
    # create_user
    def create_user(
        self, 
        username, 
        password, 
        email, 
        firstname,
        lastname, 
        role,
        cred_type = "password",
        enabled = True):
        new_user = self.keycloak_admin.create_user(
            {
                "email": email,
                "username":username,
                "enabled": enabled,
                "firstName": firstname,
                "lastName": lastname,
                "attributes": {"user_role":role},
                "credentials": [{"value": password,"type": cred_type}]
            }
        ) 
        return new_user

    # list users
    def list_user(self, params):
        users = self.keycloak_admin.get_users(params)
        return users

    def get_role(self, user_id, client_id='admin-cli'):
        role = self.keycloak_admin.get_client_roles_of_user(user_id=user_id, client_id='canarie2.0')
        return role
        
    def get_user_id(self, username):
        user_id = self.keycloak_admin.get_user_id(username)
        return user_id
    
    def get_user_info(self, userid):
        user = self.keycloak_admin.get_user(userid)
        return user 

    def update_user(self, userid, payload):
        res = self.keycloak_admin.update_user(user_id=userid, payload = payload)
        return res

    def set_user_password(self, userid, password, temporary=False):
        res = self.keycloak_admin.set_user_password(user_id=userid, password=password, temporary=temporary)
        return res

        




