import pycurl
from io import BytesIO
import os


class CurlHelper:

    @staticmethod
    def get_curl_string(link):
        """
        Returns string after doing curl on provided link
        :returns string
        """
        b_obj = BytesIO()
        crl = pycurl.Curl()
        crl.setopt(crl.URL, link)
        crl.setopt(crl.WRITEDATA, b_obj)
        crl.setopt(pycurl.HTTPHEADER, ['Authorization: token {}'.format(os.getenv("GITHUB_TOKEN")),
                                       'Content-Type: application/json'])
        crl.perform()
        crl.close()
        get_body = b_obj.getvalue()
        print("getting info from {} \n".format(link))
        print("received: {} \n".format(get_body.decode('utf8')))
        return get_body.decode('utf8')
