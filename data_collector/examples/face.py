import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "629c31b208da4f7d9acda254ed2f9fe5"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

def getFaceAttributes(image_url):
    # Set image_url to the URL of an image that you want to analyze.
    image_url; #'https://how-old.net/Images/faces2/main007.jpg'
    faceAttributes = []

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
        'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    }
    data = {'url': image_url}
    response = requests.post(face_api_url, params=params, headers=headers, json=data)
    faces = response.json()
    # Display the original image and overlay it with the face information.
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.figure(figsize=(8, 8))
    ax = plt.imshow(image, alpha=0.6)
    temp = {}
    for face in faces:
        print(face['faceAttributes']['gender']+" - "+ str(face['faceAttributes']['age']))
        temp.update({'gender':face['faceAttributes']['gender']})
        print(temp)
        faceAttributes.append(temp)
    return faceAttributes
