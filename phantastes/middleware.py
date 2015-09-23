from django.shortcuts import redirect

class ForumMiddleware(object):

    def process_request(self, request):
        if "forum" in request.path:
            if request.user.is_authenticated():
                return None
            else:
                return redirect('/account/login')
        else:
            return None
