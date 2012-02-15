from starflyer import Handler, ashtml
from userbase import LoginManager

class IndexView(Handler):
    """an index handler"""
    
    template = "index.html"

    def prepare(self):
        """prepare the handler"""
        super(IndexView, self).prepare()
        self.login_manager = LoginManager(
            self, # our handler so we have access to request
            userbase_config = self.config.userbase_config, # we simply store everything here we need, like cookie name, login url, database etc.

            # login_url : URL to POST to in the login form
            # cookie: name of cookie to be used for login information
            # logged_in_url: URL to redirect to in case of successful login
            #
        )

    def prepare_render(self, params):
        """provide more information to the render method"""
        params = super(IndexView, self).prepare_render(params)
        params.txt = self.config.i18n.de                                                                                                                                                         
        return params


    @ashtml()
    def get(self):
        """
        LOGIC:
            - if user is logged in, show the login information in the area

            From now on we assume the user is not logged in:
            - if it's no POST request, show the login form
            - if it's a POST request, check the if the credentials are valid, if not, show the login form with error again
            - if credentials are valid, redirect the user to the ``logged_in_url``

            This probably can be done in a frame, too but the logged_in URL needs to redirect the top frame then.

            JS on the fly validation: Can be done by simply setting the classes and ids and the host application need to provide
            the JS for it. 

        """
        if not self.login_manager.logged_in:
            form = self.login_manager.rendered_form()
            return self.render(
                form = form,
            )

    def register(self):
        """example for an registration form

        LOGIC:
            - normal form submission but with online validation possibility"
