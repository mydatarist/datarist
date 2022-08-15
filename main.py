# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_now():
  return { 'now': datetime.utcnow() }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs/')
def docs():
    return render_template('docs.html')

@app.route('/docs/statistics/graphics/3d-plots/')
def three_d_plots():
    return render_template('docs/statistics/graphics/3d-plots.html')

@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')

@app.route('/docs/statistics/graphics/bland-altman-plots/')
def bland_altman_plots():
    return render_template('docs/statistics/graphics/bland-altman-plots.html')

@app.route('/docs/statistics/graphics/box-plots/')
def box_plots():
    return render_template('docs/statistics/graphics/box-plots.html')

@app.route('/docs/statistics/graphics/circular-data-plots/')
def circular_data_plots():
    return render_template('docs/statistics/graphics/circular-data-plots.html')

@app.route('/docs/statistics/graphics/contour-plots/')
def contour_plots():
    return render_template('docs/statistics/graphics/contour-plots.html')

@app.route('/docs/statistics/graphics/curve-fitting/')
def curve_fitting():
    return render_template('docs/statistics/graphics/curve-fitting.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')

@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')

@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/docs/statistics/graphics/bar-charts/')
def bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')
	
@app.route('/terms/')
def terms():
    return render_template('terms.html')

@app.route('/privacy/')
def privacy():
    return render_template('privacy.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
