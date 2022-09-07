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

# STATISTICS

@app.route('/statistics/')
def route_statistics():
    return render_template('statistics/index.html')

# GRAPHICS

@app.route('/graphics/')
def route_graphics():
    return render_template('graphics/index.html')

# SAMPLE SIZE

@app.route('/sample-size/')
def route_sample_size():
    return render_template('sample-size/index.html')

# TOOLS

@app.route('/tools/')
def route_tools():
    return render_template('tools/index.html')

# ABOUT

@app.route('/about/')
def about():
    return render_template('about/index.html')		

@app.route('/about/team/')
def about_team():
    return render_template('about/team.html')		

@app.route('/about/brand/')
def about_brand():
    return render_template('about/brand.html')		

@app.route('/about/license/')
def about_license():
    return render_template('about/license.html')	
	
# TERMS

@app.route('/terms/')
def terms():
    return render_template('terms/index.html')

# PRIVACY

@app.route('/privacy/')
def privacy():
    return render_template('privacy/index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
