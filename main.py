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

# DOCS/STATISTICS/GRAPHICS/

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
	
@app.route('/docs/statistics/graphics/dendrograms/')
def dendrograms():
    return render_template('docs/statistics/graphics/dendrograms.html')
	
@app.route('/docs/statistics/graphics/density-plots/')
def density_plots():
    return render_template('docs/statistics/graphics/density-plots.html')
	
@app.route('/docs/statistics/graphics/dot-plots/')
def dot_plots():
    return render_template('docs/statistics/graphics/dot-plots.html')
	
@app.route('/docs/statistics/graphics/error-bar-charts/')
def error_bar_charts():
    return render_template('docs/statistics/graphics/error-bar-charts.html')
	
@app.route('/docs/statistics/graphics/forecasting/')
def forecasting():
    return render_template('docs/statistics/graphics/forecasting.html')
	
@app.route('/docs/statistics/graphics/forest-plots/')
def forest_plots():
    return render_template('docs/statistics/graphics/forest-plots.html')
	
@app.route('/docs/statistics/graphics/function-plots/')
def function_plots():
    return render_template('docs/statistics/graphics/function-plots.html')
	
@app.route('/docs/statistics/graphics/heat-maps/')
def heat_maps():
    return render_template('docs/statistics/graphics/heat-maps.html')
	
@app.route('/docs/statistics/graphics/histograms/')
def histograms():
    return render_template('docs/statistics/graphics/histograms.html')
	
@app.route('/docs/statistics/graphics/kaplan-meier-curves/')
def kaplan_meier_curves():
    return render_template('docs/statistics/graphics/kaplan-meier-curves.html')
	
@app.route('/docs/statistics/graphics/line-charts/')
def line_charts():
    return render_template('docs/statistics/graphics/line-charts.html')
	
@app.route('/docs/statistics/graphics/mosaic-plots/')
def mosaic_plots():
    return render_template('docs/statistics/graphics/mosaic-plots.html')
	
@app.route('/docs/statistics/graphics/percentile-plots/')
def percentile_plots():
    return render_template('docs/statistics/graphics/percentile-plots.html')
	
@app.route('/docs/statistics/graphics/pie-charts/')
def pie_charts():
    return render_template('docs/statistics/graphics/pie-charts.html')

@app.route('/docs/statistics/graphics/probability-plots/')
def probability_plots():
    return render_template('docs/statistics/graphics/probability-plots.html')
	
@app.route('/docs/statistics/graphics/quality-control-charts/')
def quality_control_charts():
    return render_template('docs/statistics/graphics/quality-control-charts.html')

@app.route('/docs/statistics/graphics/roc-curves/')
def rock_curves():
    return render_template('docs/statistics/graphics/roc-curves.html')
	
@app.route('/docs/statistics/graphics/scatter-plots/')
def scatter_plots():
    return render_template('docs/statistics/graphics/scatter_plots.html')
	
@app.route('/docs/statistics/graphics/stem-and-leaf-plots/')
def stem_and_leaf_plots():
    return render_template('docs/statistics/graphics/stem-and-leaf-plots.html')
	
@app.route('/docs/statistics/graphics/surface-plots/')
def surface_plots():
    return render_template('docs/statistics/graphics/surface-plots.html')
	
@app.route('/docs/statistics/graphics/time-series/')
def time_series():
    return render_template('docs/statistics/graphics/time-series.html')
	
@app.route('/docs/statistics/graphics/violin-plots/')
def violin_plots():
    return render_template('docs/statistics/graphics/violin-plots.html')

# DOCS/STATISTICS/PROCEDURES/

@app.route('/docs/statistics/procedures/analysis-of-variance/')
def procedure_analysis_of_variance():
    return render_template('docs/statistics/procedures/analysis-of-variance.html')
	
@app.route('/docs/statistics/procedures/appraisal/')
def procedure_appraisal():
    return render_template('docs/statistics/procedures/appraisal.html')
	
@app.route('/docs/statistics/procedures/cluster-analysis/')
def procedure_cluster_analysis():
    return render_template('docs/statistics/procedures/cluster-analysis.html')
	
@app.route('/docs/statistics/procedures/correlation/')
def procedure_correlation():
    return render_template('docs/statistics/procedures/correlation.html')
	
@app.route('/docs/statistics/procedures/curve-fitting/')
def procedure_curve_fitting():
    return render_template('docs/statistics/procedures/curve-fitting.html')
	
@app.route('/docs/statistics/procedures/descriptive-statistics/')
def procedure_descriptive_statistics():
    return render_template('docs/statistics/procedures/descriptive-statistics.html')
	
@app.route('/docs/statistics/procedures/design-of-experiments/')
def procedure_design_of_experiments():
    return render_template('docs/statistics/procedures/design-of-experiments.html')
	
@app.route('/docs/statistics/procedures/diagnostic-tests/')
def procedure_diagnostic_tests():
    return render_template('docs/statistics/procedures/diagnostic-tests.html')
	
@app.route('/docs/statistics/procedures/distribution-fitting/')
def procedure_distribution_fitting():
    return render_template('docs/statistics/procedures/distribution-fitting.html')
	
@app.route('/docs/statistics/procedures/forecasting/')
def procedure_forecasting():
    return render_template('docs/statistics/procedures/forecasting.html')
	
@app.route('/docs/statistics/procedures/group-sequential/')
def procedure_group_sequential():
    return render_template('docs/statistics/procedures/group-sequential.html')
	
@app.route('/docs/statistics/procedures/item-analysis/')
def procedure_item_analysis():
    return render_template('docs/statistics/procedures/item-analysis.html')
	
@app.route('/docs/statistics/procedures/meta-analysis/')
def procedure_meta_analysis():
    return render_template('docs/statistics/procedures/meta-analysis.html')
	
@app.route('/docs/statistics/procedures/method-comparison/')
def procedure_method_comparison():
    return render_template('docs/statistics/procedures/method-comparison.html')
	
@app.route('/docs/statistics/procedures/mixed-models/')
def procedure_mixed_models():
    return render_template('docs/statistics/procedures/mixed-models.html')
	
@app.route('/docs/statistics/procedures/multivariate-analysis/')
def procedure_multivariate_analysis():
    return render_template('docs/statistics/procedures/multivariate-analysis.html')
	
@app.route('/docs/statistics/procedures/nondetects-data/')
def procedure_nondetects_data():
    return render_template('docs/statistics/procedures/nondetects-data.html')
	
@app.route('/docs/statistics/procedures/nonparametric/')
def procedure_nonparametric():
    return render_template('docs/statistics/procedures/nonparametric.html')
	
@app.route('/docs/statistics/procedures/operations-research/')
def procedure_operations_research():
    return render_template('docs/statistics/procedures/operations-research.html')
	
@app.route('/docs/statistics/procedures/proportions/')
def procedure_proportions():
    return render_template('docs/statistics/procedures/proportions.html')
	
@app.route('/docs/statistics/procedures/quality-control/')
def procedure_quality_control():
    return render_template('docs/statistics/procedures/quality-control.html')
	
@app.route('/docs/statistics/procedures/reference-intervals/')
def procedure_reference_intervals():
    return render_template('docs/statistics/procedures/reference-intervals.html')
	
@app.route('/docs/statistics/procedures/regression/')
def procedure_regression():
    return render_template('docs/statistics/procedures/regression.html')
	
@app.route('/docs/statistics/procedures/roc-curves/')
def procedure_roc_curves():
    return render_template('docs/statistics/procedures/roc-curves.html')
	
@app.route('/docs/statistics/procedures/survey-data/')
def procedure_survey_data():
    return render_template('docs/statistics/procedures/survey-data.html')
	
@app.route('/docs/statistics/procedures/survival-analysis-reliability/')
def procedure_survival_analysis_reliability():
    return render_template('docs/statistics/procedures/survival-analysis-reliability.html')
	
@app.route('/docs/statistics/procedures/time-series/')
def procedure_time_series():
    return render_template('docs/statistics/procedures/time-series.html')
	
@app.route('/docs/statistics/procedures/t-tests/')
def procedure_t_tests():
    return render_template('docs/statistics/procedures/t-tests.html')
	
@app.route('/docs/statistics/procedures/two-way-tables/')
def procedure_two_way_tables():
    return render_template('docs/statistics/procedures/two-way-tables.html')
		
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
