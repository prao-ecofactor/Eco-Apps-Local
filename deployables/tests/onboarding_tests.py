from mock import patch
from deployables.partner import user_location_service
from deployables.partner.user_location_service import create_user_location
from webtest import TestApp
import unittest

class UserAndLocationServiceTests(unittest.TestCase):

    @patch('deployables.partner.user_location_service.invoke')
    @patch('deployables.partner.user_location_service.get_param')
    def test_user_location_service(self,mock_get_param,mock_invoke): 
        mock_get_param.return_value = {},{}
        mock_invoke.return_value = True
        result = create_user_location()
        assert result==True
       
    @patch('deployables.partner.user_location_service.invoke')
    @patch('deployables.partner.user_location_service.get_param')   
    def test_rest_controller_user_location_service(self,mock_get_param,mock_invoke):
        mock_get_param.return_value = {},{}
        mock_invoke.return_value = {"user_id":123}
        test_app=TestApp(user_location_service.app)
        results = test_app.post_json('/services/CMCSA/data/v1.0/user',{'name':"test"})
        self.assertEqual(results.status_int, 200)
        self.assertEqual(results.json['user_id'],123)
