import logging
from flask import render_template
from flask import Flask
from reqData.get_request import get_request
from reqData.helloAnalytics import helloAnalytics
<<<<<<< HEAD
from pytrends.request import TrendReq
from datetime import date
=======

>>>>>>> 0dbd267ccf7d73d6d69fb66b8dee423f7f152ed6

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-251000346-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' UA-251000346-1');
    </script>
    """
    return prefix_google + render_template('index.html')

@app.route('/log', methods=["GET"])
def logger():
    
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-251000346-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' UA-251000346-1');
    </script>
    """
    
    return prefix_google + render_template('logger.html', value='This is warning')


@app.route('/visitor', methods=["GET","POST"])
def number_visitor():
    with app.app_context():
        prefix_google = """
        <!-- Google tag (gtag.js) -->
        <script async
        src="https://www.googletagmanager.com/gtag/js?id=UA-251000346-1"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', ' UA-251000346-1');
        </script>
        """
        res=get_request.get_data('https://www.google.com')
        res2=get_request.get_data("https://analytics.google.com/analytics/web/#/report-home/a251000346w345081152p281219536")


        # Define the auth scopes to request.
        scope = 'https://www.googleapis.com/auth/analytics.readonly'
        key_file_location = 'key.json'

        # Authenticate and construct service.
        service = helloAnalytics.get_service(
                api_name='analytics',
                api_version='v3',
                scopes=[scope],
                key_file_location=key_file_location)

        #profile_id = helloAnalytics.get_first_profile_id(service)
        helloAnalytics.print_results(helloAnalytics.get_results(service, '281219536')) #here is the id of the view
        #data=helloAnalytics.get_results(service, profile_id) this can't be use for the id of profile
        data=helloAnalytics.get_results(service, '281219536')
        evt=data.get('rows')[0][0]
        vist=data.get('rows')[0][1]
<<<<<<< HEAD
        return prefix_google + render_template('cookie.html', value=res.cookie, analytic=res2.text, event= evt, visit= vist)

@app.route('/trend', methods=["GET", "POST"])
def google_trend():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-251000346-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' UA-251000346-1');
    </script>
    """



    pytrend = TrendReq()


    kw_list = ["chine","sintomas covid"]
    pytrend.build_payload(kw_list=kw_list,timeframe=f'2022-10-26 {date.today()}', geo='BR')

 
    # Interest Over Time
    trend_data=pytrend.interest_over_time()
    
    print(trend_data)
    print(trend_data.chine)
    print(trend_data["sintomas covid"])
    return prefix_google + render_template('trend.html',trend=trend_data)
=======
        return prefix_google + render_template('cookie.html', value=res.cookie, analytic=res2.text, event= evt, visit= vist)
>>>>>>> 0dbd267ccf7d73d6d69fb66b8dee423f7f152ed6
