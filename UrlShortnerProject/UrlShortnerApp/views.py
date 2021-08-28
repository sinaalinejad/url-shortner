from django.http.response import HttpResponse , JsonResponse
from django.shortcuts import redirect, render
import math
from django.core.handlers.wsgi import WSGIRequest
from .models import Url
import ast
# Create your views here.

class URLGenerator:
    BASE = 62
    UPPERCASE_OFFSET = 55
    LOWERCASE_OFFSET = 61
    DIGIT_OFFSET = 48

    def generate_unique_key(self, integer):
        """
        Turn an integer [integer] into a base [BASE] number
        in string representation
        """

        # we won't step into the while if integer is 0
        # so we just solve for that case here
        if integer == 0:
            return '0'

        string = ""
        remainder: int = 0
        while integer > 0:
            remainder = integer % self.BASE
            string = self._true_chr(remainder) + string
            integer = int(integer / self.BASE)
        return string

    def get_id(self, key):
        """
        Turn the base [BASE] number [key] into an integer
        """
        int_sum = 0
        reversed_key = key[::-1]
        for idx, char in enumerate(reversed_key):
            int_sum += self._true_ord(char) * int(math.pow(self.BASE, idx))
        return int_sum

    def _true_ord(self, char):
        """
        Turns a digit [char] in character representation
        from the number system with base [BASE] into an integer.
        """

        if char.isdigit():
            return ord(char) - self.DIGIT_OFFSET
        elif 'A' <= char <= 'Z':
            return ord(char) - self.UPPERCASE_OFFSET
        elif 'a' <= char <= 'z':
            return ord(char) - self.LOWERCASE_OFFSET
        else:
            raise ValueError("%s is not a valid character" % char)

    def _true_chr(self, integer):
        """
        Turns an integer [integer] into digit in base [BASE]
        as a character representation.
        """
        if integer < 10:
            return chr(integer + self.DIGIT_OFFSET)
        elif 10 <= integer <= 35:
            return chr(integer + self.UPPERCASE_OFFSET)
        elif 36 <= integer < 62:
            return chr(integer + self.LOWERCASE_OFFSET)
        else:
            raise ValueError(
                "%d is not a valid integer in the range of base %d" % (integer, self.BASE))


def view_func_main(request , temp) :
    urlObj = URLGenerator()
    myid = urlObj.get_id(temp)
    url = Url.objects.get(id=myid).mainUrl
    return redirect(url)
def get_short_url(request:WSGIRequest) :
    print(type(request))
    if request.method == 'POST' :
        data = request.body.decode("UTF-8")
        urls = ast.literal_eval(data)['url']
        id = Url.objects.create(mainUrl=urls).pk
        urlObj = URLGenerator()
        shortUrl = urlObj.generate_unique_key(id)
        result = "http://127.0.0.1:8000/app/" + shortUrl
        res = {
            'your short url' : result
        }
        return JsonResponse(res)
