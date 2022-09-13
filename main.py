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

# /STATISTICS/

@app.route('/statistics/')
def statistics_index():
    return render_template('statistics/index.html')

# /STATISTICS/ANOVA/

@app.route('/statistics/anova/')
def statistics_anova_index():
    return render_template('statistics/anova/index.html')

@app.route('/statistics/anova/analysis-of-covariance-with-two-groups/')
def statistics_anova_analysis_of_covariance_with_two_groups():
    return render_template('statistics/anova/analysis-of-covariance-with-two-groups.html')

@app.route('/statistics/anova/analysis-of-two-level-designs/')
def statistics_anova_analysis_of_two_level_designs():
    return render_template('statistics/anova/analysis-of-two-level-designs.html')

@app.route('/statistics/anova/area-under-curve/')
def statistics_anova_area_under_curve():
    return render_template('statistics/anova/area-under-curve.html')

@app.route('/statistics/anova/balanced-design-analysis-of-variance/')
def statistics_anova_balanced_design_analysis_of_variance():
    return render_template('statistics/anova/balanced-design-analysis-of-variance.html')

@app.route('/statistics/anova/box-cox-transformation-for-two-or-more/')
def statistics_anova_box_cox_transformation_for_two_or_more():
    return render_template('statistics/anova/box-cox-transformation-for-two-or-more.html')

@app.route('/statistics/anova/general-linear-models-for-fixed-factors/')
def statistics_anova_general_linear_models_for_fixed_factors():
    return render_template('statistics/anova/general-linear-models-for-fixed-factors.html')

@app.route('/statistics/anova/general-linear-models/')
def statistics_anova_general_linear_models():
    return render_template('statistics/anova/general-linear-models.html')

@app.route('/statistics/anova/groups/')
def statistics_anova_groups():
    return render_template('statistics/anova/groups.html')

@app.route('/statistics/anova/multivariate-analysis-of-variance/')
def statistics_anova_multivariate_analysis_of_variance():
    return render_template('statistics/anova/multivariate-analysis-of-variance.html')

@app.route('/statistics/anova/nondetects-data-group-comparison/')
def statistics_anova_nondetects_data_group_comparison():
    return render_template('statistics/anova/nondetects-data-group-comparison.html')

@app.route('/statistics/anova/one-way-analysis-of-covariance/')
def statistics_anova_one_way_analysis_of_covariance():
    return render_template('statistics/anova/one-way-analysis-of-covariance.html')

@app.route('/statistics/anova/one-way-analysis-of-variance/')
def statistics_anova_one_way_analysis_of_variance():
    return render_template('statistics/anova/one-way-analysis-of-variance.html')

@app.route('/statistics/anova/repeated-measures-analysis-of-variance/')
def statistics_anova_repeated_measures_analysis_of_variance():
    return render_template('statistics/anova/repeated-measures-analysis-of-variance.html')

# /STATISTICS/APPRAISAL/

@app.route('/statistics/appraisal/')
def statistics_appraisal_index():
    return render_template('statistics/appraisal/index')

@app.route('/statistics/appraisal/appraisal-ratio-studies/')
def statistics_appraisal_appraisal_ratio_studies():
    return render_template('statistics/appraisal/appraisal-ratio-studies.html')

@app.route('/statistics/appraisal/comparables-appraisal/')
def statistics_appraisal_comparables_appraisal():
    return render_template('statistics/appraisal/comparables-appraisal.html')

@app.route('/statistics/appraisal/descriptive-statistics/')
def statistics_appraisal_descriptive_statistics():
    return render_template('statistics/appraisal/descriptive-statistics.html')

@app.route('/statistics/appraisal/hybrid-appraisal-models/')
def statistics_appraisal_hybrid_appraisal_models():
    return render_template('statistics/appraisal/hybrid-appraisal-models.html')

@app.route('/statistics/appraisal/linear-regression-and-correlation/')
def statistics_appraisal_linear_regression_and_correlation():
    return render_template('statistics/appraisal/linear-regression-and-correlation.html')

@app.route('/statistics/appraisal/multiple-regression/')
def statistics_appraisal_multiple_regression():
    return render_template('statistics/appraisal/multiple-regression.html')

@app.route('/statistics/appraisal/nonlinear-regression/')
def statistics_appraisal_nonlinear_regression():
    return render_template('statistics/appraisal/nonlinear-regression.html')

# /STATISTICS/CLUSTER-ANALYSIS/

@app.route('/statistics/cluster-analysis/')
def statistics_cluster_analysis_index():
    return render_template('statistics/cluster-analysis/index.html')

@app.route('/statistics/cluster-analysis/clustered-heat-maps/')
def statistics_cluster_analysis_clustered_heat_maps():
    return render_template('statistics/cluster-analysis/clustered-heat-maps.html')

@app.route('/statistics/cluster-analysis/fuzzy-clustering/')
def statistics_cluster_analysis_fuzzy_clustering():
    return render_template('statistics/cluster-analysis/fuzzy-clustering.html')

@app.route('/statistics/cluster-analysis/hierarchical-clustering/')
def statistics_cluster_analysis_hierarchical_clustering():
    return render_template('statistics/cluster-analysis/hierarchical-clustering.html')

@app.route('/statistics/cluster-analysis/k-means-clustering/')
def statistics_cluster_analysis_k_means_clustering():
    return render_template('statistics/cluster-analysis/k-means-clustering.html')

@app.route('/statistics/cluster-analysis/medoid-partitioning/')
def statistics_cluster_analysis_medoid_partitioning():
    return render_template('statistics/cluster-analysis/medoid-partitioning.html')

@app.route('/statistics/cluster-analysis/regression-clustering/')
def statistics_cluster_analysis_regression_clustering():
    return render_template('statistics/cluster-analysis/regression-clustering.html')

# /STATISTICS/CORRELATION/

@app.route('/statistics/correlation/')
def statistics_correlation_index():
    return render_template('statistics/correlation/index.html')

@app.route('/statistics/correlation/bland-altman-plot-and-analysis/')
def statistics_correlation_bland_altman_plot_and_analysis():
    return render_template('statistics/correlation/bland-altman-plot-and-analysis.html')

@app.route('/statistics/correlation/box-cox-transformation-for-simple-linear-regression/')
def statistics_correlation_box_cox_transformation_for_simple_linear_regression():
    return render_template('statistics/correlation/box-cox-transformation-for-simple-linear-regression.html')

@app.route('/statistics/correlation/canonical-correlation/')
def statistics_correlation_canonical_correlation():
    return render_template('statistics/correlation/canonical-correlation.html')

@app.route('/statistics/correlation/circular-data-correlation/')
def statistics_correlation_circular_data_correlation():
    return render_template('statistics/correlation/circular-data-correlation.html')

@app.route('/statistics/correlation/correlation-matrix/')
def statistics_correlation_correlation_matrix():
    return render_template('statistics/correlation/correlation-matrix.html')

@app.route('/statistics/correlation/correlation/')
def statistics_correlation_correlation():
    return render_template('statistics/correlation/correlation.html')

@app.route('/statistics/correlation/item-analysis/')
def statistics_correlation_item_analysis():
    return render_template('statistics/correlation/item-analysis.html')

@app.route('/statistics/correlation/linear-regression-and-correlation/')
def statistics_correlation_linear_regression_and_correlation():
    return render_template('statistics/correlation/linear-regression-and-correlation.html')

@app.route('/statistics/correlation/lins-concordance-correlation-coefficient/')
def statistics_correlation_lins_concordance_correlation_coefficient():
    return render_template('statistics/correlation/lins-concordance-correlation-coefficient.html')

@app.route('/statistics/correlation/point-biserial-and-biserial-correlations/')
def statistics_correlation_point_biserial_and_biserial_correlations():
    return render_template('statistics/correlation/point-biserial-and-biserial-correlations.html')

# /STATISTICS/CURVE-FITTING/

@app.route('/statistics/curve-fitting/')
def statistics_curve_fitting_index():
    return render_template('statistics/curve-fitting/index.html')

@app.route('/statistics/curve-fitting/curve-fitting/')
def statistics_curve_fitting_curve_fitting():
    return render_template('statistics/curve-fitting/curve-fitting.html')

@app.route('/statistics/curve-fitting/fractional-polynomial-regression/')
def statistics_curve_fitting_fractional_polynomial_regression():
    return render_template('statistics/curve-fitting/fractional-polynomial-regression.html')

@app.route('/statistics/curve-fitting/function-plots/')
def statistics_curve_fitting_function_plots():
    return render_template('statistics/curve-fitting/function-plots.html')

@app.route('/statistics/curve-fitting/introduction-to-curve-fitting/')
def statistics_curve_fitting_introduction_to_curve_fitting():
    return render_template('statistics/curve-fitting/introduction-to-curve-fitting.html')

@app.route('/statistics/curve-fitting/michaelis-menten-equation/')
def statistics_curve_fitting_michaelis_menten_equation():
    return render_template('statistics/curve-fitting/michaelis-menten-equation.html')

@app.route('/statistics/curve-fitting/nonlinear-regression/')
def statistics_curve_fitting_nonlinear_regression():
    return render_template('statistics/curve-fitting/nonlinear-regression.html')

@app.route('/statistics/curve-fitting/ratio-of-polynomials-fit-many-variable/')
def statistics_curve_fitting_ratio_of_polynomials_fit_many_variable():
    return render_template('statistics/curve-fitting/ratio-of-polynomials-fit-many-variable.html')

@app.route('/statistics/curve-fitting/ratio-of-polynomials-fit-one-variable/')
def statistics_curve_fitting_ratio_of_polynomials_fit_one_variable():
    return render_template('statistics/curve-fitting/ratio-of-polynomials-fit-one-variable.html')

@app.route('/statistics/curve-fitting/')
def statistics_curve_fitting_index():
    return render_template('statistics/curve-fitting/index.html')

@app.route('/statistics/curve-fitting/')
def statistics_curve_fitting_index():
    return render_template('statistics/curve-fitting/index.html')

@app.route('/statistics/curve-fitting/')
def statistics_curve_fitting_index():
    return render_template('statistics/curve-fitting/index.html')

@app.route('/statistics/curve-fitting/')
def statistics_curve_fitting_index():
    return render_template('statistics/curve-fitting/index.html')

@app.route('/statistics/curve-fitting/')
def statistics_curve_fitting_index():
    return render_template('statistics/curve-fitting/index.html')

# /GRAPHICS/

@app.route('/graphics/')
def graphics_index():
    return render_template('graphics/index.html')

# /SAMPLE-SIZE/

@app.route('/sample-size/')
def sample_size_index():
    return render_template('sample-size/index.html')

# /TOOLS/

@app.route('/tools/')
def tools_index():
    return render_template('tools/index.html')

# /ABOUT/

@app.route('/about/')
def about_index():
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
	
# /TERMS/

@app.route('/terms/')
def terms_index():
    return render_template('terms/index.html')

# /PRIVACY/

@app.route('/privacy/')
def privacy_index():
    return render_template('privacy/index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
