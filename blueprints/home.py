from flask import render_template, Blueprint, current_app, make_response, jsonify
from flask_babel import _
from flask_login import current_user
from util import sysutil
import models,time

from extensions import db

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    # 查询后修改
    #ModifyDt = session.query(Mybase).filter_by(myid='asd').first()
    # ModifyDt.price='bbbb'
    #models.session.commit()
    return render_template('index.html')


@home_bp.route('/intro')
def intro():
    return render_template('_intro.html')


@home_bp.route('/set-locale/<locale>')
def set_locale(locale):
    if locale not in current_app.config['TODOISM_LOCALES']:
        return jsonify(message=_('Invalid locale.')), 404

    response = make_response(jsonify(message=_('Setting updated.')))
    if current_user.is_authenticated:
        current_user.locale = locale
        db.session.commit()
    else:
        response.set_cookie('locale', locale, max_age=60 * 60 * 24 * 30)
    return response

@home_bp.route('/xx')
def xx():
    httputil=sysutil.httputil()
    url="http://123.127.164.20:21935"

    name=models.session.query(models.User).filter_by(locale='http://123.127.164.20:21935').first().username
    pas=models.session.query(models.User).filter_by(locale='http://123.127.164.20:21935').first().password_hash
    #pas=models.session.query().filter_by(name='ed').first()
    t=httputil.login(url,name,pas)
    #httputil.driver.get(url)
    time.sleep(2)
    httputil.driver.get_screenshot_as_file("/home/h/.png")
    print (t)
    lis = httputil.bytag(httputil.driver.current_url, "ul", "li")
    for li in lis:
        print(li.text)
    print(httputil.driver.find_element_by_id("runtime").text)
    ats = httputil.bytag_att(httputil.driver.current_url, "a")
    for at in ats:
        url=at.get_attribute("href")
        time.sleep(2)
        if not url is None:
            js = "window.open(%s)"%(url)
            print(url)
            #httputil.driver.execute_script(js)
        print(at.text, "url:", url)
    return render_template('xxbase.html')