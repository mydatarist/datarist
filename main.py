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
def graphics_three_d_plots():
    return render_template('docs/statistics/graphics/3d-plots.html')

@app.route('/docs/statistics/graphics/bar-charts/')
def graphics_bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')

@app.route('/docs/statistics/graphics/bland-altman-plots/')
def graphics_bland_altman_plots():
    return render_template('docs/statistics/graphics/bland-altman-plots.html')

@app.route('/docs/statistics/graphics/box-plots/')
def graphics_box_plots():
    return render_template('docs/statistics/graphics/box-plots.html')

@app.route('/docs/statistics/graphics/circular-data-plots/')
def graphics_circular_data_plots():
    return render_template('docs/statistics/graphics/circular-data-plots.html')

@app.route('/docs/statistics/graphics/contour-plots/')
def graphics_contour_plots():
    return render_template('docs/statistics/graphics/contour-plots.html')

@app.route('/docs/statistics/graphics/curve-fitting/')
def graphics_curve_fitting():
    return render_template('docs/statistics/graphics/curve-fitting.html')
	
@app.route('/docs/statistics/graphics/dendrograms/')
def graphics_dendrograms():
    return render_template('docs/statistics/graphics/dendrograms.html')
	
@app.route('/docs/statistics/graphics/density-plots/')
def graphics_density_plots():
    return render_template('docs/statistics/graphics/density-plots.html')
	
@app.route('/docs/statistics/graphics/dot-plots/')
def graphics_dot_plots():
    return render_template('docs/statistics/graphics/dot-plots.html')
	
@app.route('/docs/statistics/graphics/error-bar-charts/')
def graphics_error_bar_charts():
    return render_template('docs/statistics/graphics/error-bar-charts.html')
	
@app.route('/docs/statistics/graphics/forecasting/')
def graphics_forecasting():
    return render_template('docs/statistics/graphics/forecasting.html')
	
@app.route('/docs/statistics/graphics/forest-plots/')
def graphics_forest_plots():
    return render_template('docs/statistics/graphics/forest-plots.html')
	
@app.route('/docs/statistics/graphics/function-plots/')
def graphics_function_plots():
    return render_template('docs/statistics/graphics/function-plots.html')
	
@app.route('/docs/statistics/graphics/heat-maps/')
def graphics_heat_maps():
    return render_template('docs/statistics/graphics/heat-maps.html')
	
@app.route('/docs/statistics/graphics/histograms/')
def graphics_histograms():
    return render_template('docs/statistics/graphics/histograms.html')
	
@app.route('/docs/statistics/graphics/kaplan-meier-curves/')
def graphics_kaplan_meier_curves():
    return render_template('docs/statistics/graphics/kaplan-meier-curves.html')
	
@app.route('/docs/statistics/graphics/line-charts/')
def graphics_line_charts():
    return render_template('docs/statistics/graphics/line-charts.html')
	
@app.route('/docs/statistics/graphics/mosaic-plots/')
def graphics_mosaic_plots():
    return render_template('docs/statistics/graphics/mosaic-plots.html')
	
@app.route('/docs/statistics/graphics/percentile-plots/')
def graphics_percentile_plots():
    return render_template('docs/statistics/graphics/percentile-plots.html')
	
@app.route('/docs/statistics/graphics/pie-charts/')
def graphics_pie_charts():
    return render_template('docs/statistics/graphics/pie-charts.html')

@app.route('/docs/statistics/graphics/probability-plots/')
def graphics_probability_plots():
    return render_template('docs/statistics/graphics/probability-plots.html')
	
@app.route('/docs/statistics/graphics/quality-control-charts/')
def graphics_quality_control_charts():
    return render_template('docs/statistics/graphics/quality-control-charts.html')

@app.route('/docs/statistics/graphics/roc-curves/')
def graphics_roc_curves():
    return render_template('docs/statistics/graphics/roc-curves.html')
	
@app.route('/docs/statistics/graphics/scatter-plots/')
def graphics_scatter_plots():
    return render_template('docs/statistics/graphics/scatter_plots.html')
	
@app.route('/docs/statistics/graphics/stem-and-leaf-plots/')
def graphics_stem_and_leaf_plots():
    return render_template('docs/statistics/graphics/stem-and-leaf-plots.html')
	
@app.route('/docs/statistics/graphics/surface-plots/')
def graphics_surface_plots():
    return render_template('docs/statistics/graphics/surface-plots.html')
	
@app.route('/docs/statistics/graphics/time-series/')
def graphics_time_series():
    return render_template('docs/statistics/graphics/time-series.html')
	
@app.route('/docs/statistics/graphics/violin-plots/')
def graphics_violin_plots():
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
		
# SAMPLE SIZE

@app.route('/docs/statistics/sample-size/bland-altman-method/')
def sample_size_bland_altman_method():
    return render_template('docs/statistics/sample-size/bland-altman-method.html')
		
@app.route('/docs/statistics/sample-size/bridging-studies/')
def sample_size_bridging_studies():
    return render_template('docs/statistics/sample-size/bridging-studies.html')
		
@app.route('/docs/statistics/sample-size/cluster-randomized-designs/')
def sample_size_cluster_randomized_designs():
    return render_template('docs/statistics/sample-size/cluster-randomized-designs.html')
		
@app.route('/docs/statistics/sample-size/conditional-power/')
def sample_size_conditional_power():
    return render_template('docs/statistics/sample-size/conditional-power.html')
		
@app.route('/docs/statistics/sample-size/confidence-intervals/')
def sample_size_confidence_intervals():
    return render_template('docs/statistics/sample-size/confidence-intervals.html')
		
@app.route('/docs/statistics/sample-size/correlation/')
def sample_size_correlation():
    return render_template('docs/statistics/sample-size/correlation.html')
		
@app.route('/docs/statistics/sample-size/cross-over-designs/')
def sample_size_cross_over_designs():
    return render_template('docs/statistics/sample-size/cross-over-designs.html')
		
@app.route('/docs/statistics/sample-size/design-of-experiments/')
def sample_size_design_of_experiments():
    return render_template('docs/statistics/sample-size/design-of-experiments.html')
		
@app.route('/docs/statistics/sample-size/equivalence/')
def sample_size_equivalence():
    return render_template('docs/statistics/sample-size/equivalence.html')
		
@app.route('/docs/statistics/sample-size/exponential-distribution-parameter/')
def sample_size_exponential_distribution_parameter():
    return render_template('docs/statistics/sample-size/exponential-distribution-parameter.html')
		
@app.route('/docs/statistics/sample-size/group-sequential-tests/')
def sample_size_group_sequential_tests():
    return render_template('docs/statistics/sample-size/group-sequential-tests.html')
		
@app.route('/docs/statistics/sample-size/means-one/')
def sample_size_means_one():
    return render_template('docs/statistics/sample-size/means-one.html')
		
@app.route('/docs/statistics/sample-size/means-two-independent/')
def sample_size_means_two_independent():
    return render_template('docs/statistics/sample-size/means-two-independent.html')
		
@app.route('/docs/statistics/sample-size/means-two-correlated-or-paired/')
def sample_size_means_two_correlated_or_paired():
    return render_template('docs/statistics/sample-size/means-two-correlated-or-paired.html')
		
@app.route('/docs/statistics/sample-size/means-2x2-cross-over-designs/')
def sample_size_means_2x2_cross_over_designs():
    return render_template('docs/statistics/sample-size/means-2x2-cross-over-designs.html')
		
@app.route('/docs/statistics/sample-size/means-high-order-cross-over-designs/')
def sample_size_means_high_order_cross_over_designs():
    return render_template('docs/statistics/sample-size/means-high-order-cross-over-designs.html')
		
@app.route('/docs/statistics/sample-size/means-many/')
def sample_size_means_many():
    return render_template('docs/statistics/sample-size/means-many.html')
		
@app.route('/docs/statistics/sample-size/mediation-effects/')
def sample_size_mediation_effects():
    return render_template('docs/statistics/sample-size/mediation-effects.html')
		
@app.route('/docs/statistics/sample-size/michaelis-menten-parameters/')
def sample_size_michaelis_menten_parameters():
    return render_template('docs/statistics/sample-size/michaelis-menten-parameters.html')
		
@app.route('/docs/statistics/sample-size/mixed-models/')
def sample_size_mixed_models():
    return render_template('docs/statistics/sample-size/mixed-models.html')
		
@app.route('/docs/statistics/sample-size/non-inferiority/')
def sample_size_non_inferiority():
    return render_template('docs/statistics/sample-size/non-inferiority.html')
		
@app.route('/docs/statistics/sample-size/nonparametric/')
def sample_size_nonparametric():
    return render_template('docs/statistics/sample-size/nonparametric.html')
		
@app.route('/docs/statistics/sample-size/non-zero-and-non-unity-null-tests/')
def sample_size_non_zero_and_non_unity_null_tests():
    return render_template('docs/statistics/sample-size/non-zero-and-non-unity-null-tests.html')
		
@app.route('/docs/statistics/sample-size/normality-tests/')
def sample_size_normality_tests():
    return render_template('docs/statistics/sample-size/normality-tests.html')
		
@app.route('/docs/statistics/sample-size/pilot-studies/')
def sample_size_pilot_studies():
    return render_template('docs/statistics/sample-size/pilot-studies.html')
		
@app.route('/docs/statistics/sample-size/proportions-one/')
def sample_size_proportions_one():
    return render_template('docs/statistics/sample-size/proportions-one.html')
		
@app.route('/docs/statistics/sample-size/proportions-two-independent/')
def sample_size_proportions_two_independent():
    return render_template('docs/statistics/sample-size/proportions-two-independent.html')
		
@app.route('/docs/statistics/sample-size/proportions-correlated-or-paired/')
def sample_size_proportions_correlated_or_paired():
    return render_template('docs/statistics/sample-size/proportions-correlated-or-paired.html')
		
@app.route('/docs/statistics/sample-size/proportions-cross-over-designs/')
def sample_size_proportions_cross_over_designs():
    return render_template('docs/statistics/sample-size/proportions_cross_over_designs.html')
		
@app.route('/docs/statistics/sample-size/proportions-sensitivity-and-specificity/')
def sample_size_proportions_sensitivity_and_specificity():
    return render_template('docs/statistics/sample-size/proportions-sensitivity-and-specificity.html')
		
@app.route('/docs/statistics/sample-size/proportions-many/')
def sample_size_proportions_many():
    return render_template('docs/statistics/sample-size/proportions-many.html')
		
@app.route('/docs/statistics/sample-size/quality-control/')
def sample_size_quality_control():
    return render_template('docs/statistics/sample-size/quality-control.html')
		
@app.route('/docs/statistics/sample-size/rates-and-counts/')
def sample_size_rates_and_counts():
    return render_template('docs/statistics/sample-size/rates-and-counts.html')
		
@app.route('/docs/statistics/sample-size/reference-intervals/')
def sample_size_reference_intervals():
    return render_template('docs/statistics/sample-size/reference-intervals.html')
		
@app.route('/docs/statistics/sample-size/regression/')
def sample_size_regression():
    return render_template('docs/statistics/sample-size/regression.html')
		
@app.route('/docs/statistics/sample-size/roc_curves/')
def sample_size_roc_curves():
    return render_template('docs/statistics/sample-size/roc-curves.html')
		
@app.route('/docs/statistics/sample-size/superiority_by_a_margin_test/')
def sample_size_superiority_by_a_margin_test():
    return render_template('docs/statistics/sample-size/superiority-by-a-margin-test.html')
		
@app.route('/docs/statistics/sample-size/survival-analysis/')
def sample_size_survival_analysis():
    return render_template('docs/statistics/sample-size/survival-analysis.html')
		
@app.route('/docs/statistics/sample-size/tolerance-intervals/')
def sample_size_tolerance_intervals():
    return render_template('docs/statistics/sample-size/tolerance-intervals.html')
		
@app.route('/docs/statistics/sample-size/two-part-models/')
def sample_size_two_part_models():
    return render_template('docs/statistics/sample-size/two-part-models.html')
		
@app.route('/docs/statistics/sample-size/variances-and-standard-deviations/')
def sample_size_variances_and_standard_deviations():
    return render_template('docs/statistics/sample-size/variances-and-standard-deviations.html')
		
@app.route('/docs/statistics/sample-size/bayesian-adjustment/')
def sample_size_bayesian_adjustment():
    return render_template('docs/statistics/sample-size/bayesian-adjustment.html')		

# TOOLS

@app.route('/docs/statistics/tools/procedures/chi-square-effect-size-calculator/')
def tools_procedures_chi_square_effect_size_calculator():
    return render_template('docs/statistics/tools/procedures/chi-square-effect-size-calculator.html')		

@app.route('/docs/statistics/tools/procedures/odds-ratio-and-proportions-calculator/')
def tools_procedures_odds_ratio_and_proportions_calculator():
    return render_template('docs/statistics/tools/procedures/odds-ratio-and-proportions-calculator.html')		

@app.route('/docs/statistics/tools/procedures/probability-calculator/')
def tools_procedures_probability_calculator():
    return render_template('docs/statistics/tools/procedures/probability-calculator.html')		

@app.route('/docs/statistics/tools/procedures/standard-deviation-calculator/')
def tools_procedures_standard_deviation_calculator():
    return render_template('docs/statistics/tools/procedures/standard-deviation-calculator.html')		

@app.route('/docs/statistics/tools/procedures/survival-parameter-conversion-tool/')
def tools_procedures_survival_parameter_conversion_tool():
    return render_template('docs/statistics/tools/procedures/survival-parameter-conversion-tool.html')		

# TOOL - SAMPLE SIZE

@app.route('/docs/statistics/tools/sample-size/chi-square-effect-size-estimator/')
def tools_sample_size_chi_square_effect_size_estimator():
    return render_template('docs/statistics/tools/sample-size/chi-square-effect-size-estimator.html')		

@app.route('/docs/statistics/tools/sample-size/data-simulator/')
def tools_sample_size_data_simulator():
    return render_template('docs/statistics/tools/sample-size/data-simulator.html')		

@app.route('/docs/statistics/tools/sample-size/installation-validation-tool-for-installation-qualification/')
def tools_sample_size_installation_validation_tool_for_installation_qualification():
    return render_template('docs/statistics/tools/sample-size/installation-validation-tool-for-installation-qualification.html')		

@app.route('/docs/statistics/tools/sample-size/multinomial-effect-size-estimator/')
def tools_sample_size_multinomial_effect_size_estimator():
    return render_template('docs/statistics/tools/sample-size/multinomial-effect-size-estimator.html')		

@app.route('/docs/statistics/tools/sample-size/xxxx/')
def tools_sample_size_xxxx():
    return render_template('docs/statistics/tools/sample-size/xxxx.html')		

@app.route('/docs/statistics/tools/sample-size/xxxx/')
def tools_sample_size_xxxx():
    return render_template('docs/statistics/tools/sample-size/xxxx.html')		

@app.route('/docs/statistics/tools/sample-size/xxxx/')
def tools_sample_size_xxxx():
    return render_template('docs/statistics/tools/sample-size/xxxx.html')		

@app.route('/docs/statistics/tools/sample-size/xxxx/')
def tools_sample_size_xxxx():
    return render_template('docs/statistics/tools/sample-size/xxxx.html')		

@app.route('/docs/statistics/tools/sample-size/xxxx/')
def tools_sample_size_xxxx():
    return render_template('docs/statistics/tools/sample-size/xxxx.html')		

@app.route('/docs/statistics/tools/sample-size/xxxx/')
def tools_sample_size_xxxx():
    return render_template('docs/statistics/tools/sample-size/xxxx.html')		


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
