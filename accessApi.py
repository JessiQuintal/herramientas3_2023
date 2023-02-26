import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
def llamarservicio():
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    data =  {
      "Inputs": {
        "data": [
          {
            "age": 25,
            "job": "unknown",
            "marital": "single",
            "education": "high.school",
            "default": "yes",
            "housing": "yes",
            "loan": "yes",
            "contact": "cellular",
            "month": "jan",
            "duration": 4900,
            "campaign": 50,
            "pdays": 999,
            "previous": 6,
            "poutcome": "nonexistent",
            "emp.var.rate": 1,
            "cons.price.idx": 93,
            "cons.conf.idx": -40,
            "euribor3m": 2.5,
            "nr.employed": 5030
          }
        ]
      },
      "GlobalParameters": {
        "method": "predict"
      }
    }

    body = str.encode(json.dumps(data))

    url = 'https://fca-regression.eastus2.inference.ml.azure.com/score'
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = 'AnVcIXbYyV9KbCKmAGmbV2gNhpMAdmXg'
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'fca-deploy2' }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))