import pkg_resources
import pymongo
import yaml
import smtplib
import os
import starflyer

import postmeister

from jinja2 import Environment, PackageLoader, PrefixLoader
from logbook import Logger

def setup(**kw):
    """setup the application. 

    :param kw: optional keyword arguments to override certain values of the 
        settings section of the configuration

    :return: a configuration object to be passed into the application
    """

    config = starflyer.Configuration()
    config.register_sections('dbs', 'logs', 'mail', 'i18n')
    config.register_snippet_names('header', 'footer')
    config.register_template_chains("main", "emails")

    ## various constants
    config.update_settings({
        #'log_name' : "participate",
        'virtual_host' : "http://localhost:8223",
        'virtual_path' : "/",
        'title' : "Participate!",
        'description' : "a tool for fostering citizen participation in political processes",
        'mongodb_name' : "participate",
        'mongodb_port' : 27017,
        'mongodb_host' : "localhost",
        'cookie_secret' : "cs8$$$9887cs6c8s67c98s7cd698c7s6cd9876cds89c768cs76cs8gsubajhv",
        'session_cookie_name' : "ps",
        'message_cookie_name' : "pm",
        'from_addr' : "noreply@example.org"
    })
    config.update_settings(kw) # update with data from ini file

    ## routing
    config.routes.extend([
        #('/', 'index', main.IndexView),
    ])

    ## databases
    config.dbs.db = pymongo.Connection(
        config.settings.mongodb_host,
        config.settings.mongodb_port
    )[config.settings.mongodb_name]

    ## templates
    config.templates.main.append(PackageLoader("participate","templates"))

    ## static resources like JS, CSS, images
    static_file_path = pkg_resources.resource_filename(__name__, 'static')
    config.register_static_path("/css", os.path.join(static_file_path, 'css'))
    config.register_static_path("/js", os.path.join(static_file_path, 'js'))
    config.register_static_path("/img", os.path.join(static_file_path, 'img'))

    return config

def test_snippet(*args, **kwargs):
    return "MY SNIPPET"

def um_setup(config, **kw):
    from starflyer.contrib import snippets
    static_file_path = pkg_resources.resource_filename(__name__, 'static')
    config.register_static_path("/participate_css", os.path.join(static_file_path, 'css'))
    config.snippets.header.append(snippets.css_link(config, "/participate_css/userbase.css"))
    config.settings.title = "Participate User Manager"
    return config
