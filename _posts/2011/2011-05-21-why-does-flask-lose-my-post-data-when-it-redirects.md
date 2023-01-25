---
title: "Why Does Flask Lose My Post Data When It Redirects?"
date: 2011-05-21 23:08:09
year: 2011
---
I'm trying to decide which Python web programming framework to use in the Software Carpentry course. Simplicity is the main criterion: in fact, other than "still a live project", it's the <em>only</em> criterion. Flask is a strong contender despite the fact that its documentation is written for people who already understand web programming–I can fill that in.  What I'm struggling with now, though, is that the same "hide the details" approach that makes it approachable is also making debugging difficult.

For example, here's a simple application:
<pre>from flask import Flask, render_template, request
DEBUGGING = True
app = Flask(__name__)

def load_data():
    return [
        [True, "luke", "2011-05-03", "luke", "Figure this out"],
        [True, "luke", "2011-05-03", "yele", "Figure this out"],
        [False, "luke", "2011-05-03", "gvwilson", "Figure this out"]
    ]

@app.route('/show/', methods=['POST', 'GET'])
def show():
    data = load_data()
    try:
        items = request.form['item']
        count = str(len(items))
    except KeyError:
        count = "no items"
    return render_template('show.html', data=data, count=count)

if __name__ == '__main__':
    app.run(debug=DEBUGGING)</pre>
which I put in <code>show.py</code>.  Here's the corresponding template, which I put in <code>templates/show.html</code>:
<pre>&lt;html&gt;
&lt;body&gt;
  &lt;p&gt;&lt;strong&gt;count: {{ count }}&lt;/strong&gt;&lt;/p&gt;
  &lt;form name="todo" action="/show" method="POST"&gt;
  &lt;table border="1"&gt;
    &lt;tr&gt;
      &lt;th colspan="6"&gt;Active&lt;/th&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
      &lt;th&gt;Select&lt;/th&gt;
      &lt;th&gt;Number&lt;/th&gt;
      &lt;th&gt;Creator&lt;/th&gt;
      &lt;th&gt;Created&lt;/th&gt;
      &lt;th&gt;Owner&lt;/th&gt;
      &lt;th&gt;Task&lt;/th&gt;
    &lt;/tr&gt;
    {% for item in data %}
      {% if item[0] %}
        &lt;tr class="active"&gt;
          &lt;td&gt;&lt;input type="checkbox" name="item" value="{{ loop.index0 }}"/&gt;&lt;/td&gt;
          &lt;td&gt;{{ loop.index0 }}&lt;/td&gt;
          &lt;td&gt;{{ item[1] }} &lt;/td&gt;
          &lt;td&gt;{{ item[2] }} &lt;/td&gt;
          &lt;td&gt;{{ item[3] }} &lt;/td&gt;
          &lt;td&gt;{{ item[4] }} &lt;/td&gt;
        &lt;/tr&gt;
      {% endif %}
    {% endfor %}
    &lt;tr&gt;
      &lt;th colspan="6"&gt;Completed&lt;/th&gt;
    &lt;/tr&gt;
  &lt;p&gt;&lt;input type="submit" value="make active" /&gt;&lt;/p&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>
I run the application:
<pre>$ python show.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader...</pre>
and then point my browser at <code>http://127.0.0.1:5000/show/</code> (note the trailing slash).  As expected, Firebug tells me there has been one GET request, with no parameters.

I then tick off the first of the checkboxes and click "Submit".  According to Firebug, this causes a POST with "item=0" as the submitted data (good), which immediately redirects (code 301) to a GET to the same URL, but <em>without</em> any of the posted data.  Now, according to the section on "Unique URLs / Redirection Behaviour" in the <a href="http://flask.pocoo.org/docs/quickstart/#routing">Flask documentation</a>, if the URL specified in <code>app.route</code> has a trailing '/', then accessing the URL <em>without</em> the trailing slash automatically redirects to the URL <em>with</em> the trailing slash.  But I'm submitting a URL <em>with</em> a trailing slash, so there shouldn't be a redirect, and even if there is, why is the posted data being thrown away?

I'm clearly doing something wrong, and if it wasn't a warm Saturday afternoon, I'd probably have figured it out by now.  (But please don't let that stop you from sending me tips :-).  What I'd really like to know, though, is how the hell to explain whatever is going on to someone who's new to web programming.  I've tried teaching raw CGI programming to grad students in science and engineering–it usually fails because there are too many low-level details to master.  I'd hoped that high-level frameworks like Flask and web2py would make this stuff more accessible, but the <a href="http://www.joelonsoftware.com/articles/LeakyAbstractions.html">law of leaky abstractions</a> may put them out of practical reach as well: if things that look like they ought to work don't, and there's no easy way for someone who is just learning this stuff to debug it, we're dead in the water.
