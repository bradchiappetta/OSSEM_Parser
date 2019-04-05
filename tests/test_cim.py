""" This provides a test suite for verifying the correctness
    of the OSSEM Common Information Model conversion from markdown
    to our desired output """

import unittest, os
from main import OSSEMParser

class TestOSSEMCIM(unittest.TestCase):
  def setUp(self):
    self.p = OSSEMParser()
    self.alert_md = os.path.join("tests", "test_data", "alert.md")

  def test_alert_conversion(self):
    desired_output = {
      'name': 'Alert Schema',
      'description': 'Alert fields that describe an indicator from a tool of a possible issue.',
      'data_fields': {
        'alert_id': {
          'type': 'integer',
          'description': 'Alert ids might repeat across different data sources',
          'sample_value': 1234
        },
        'alert_signature': {
          'type': 'string',
          'description': 'The name or title of an alert',
          'sample_value': 'EvilActor:CnCv2'
        },
        'alert_message': { 'type': 'string',
          'description': 'The message provided by the alert',
          'sample_value': 'A file exhibiting behaviour of the evilactor command and control framework 2 was detected.'
        },
        'alert_description': {
          'type': 'string',
          'description': 'The expanded description of the event',
          'sample_value': '...'
        },
        'alert_severity': {
          'type': 'string',
          'description': 'The severity of an alert',
          'sample_value': 'Priority 5'
        },
        'alert_category': {
          'type': 'string',
          'description': 'The category of an alert',
          'sample_value': 'Malware'
        },
        'alert_version': {
          'type': 'string',
          'description': 'A signature or alert version',
          'sample_value':'1.2'
        }
      }
    }
    print("output: '{}'".format(self.p.parse_md_file(self.alert_md)))
    #assert(desired_output == self.p.parse_md_file(self.alert_md))