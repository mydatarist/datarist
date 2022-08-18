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

# DOCS/GETTING-STARTED/

@app.route('/docs/getting-started/introduction/')
def docs_getting_started_introduction():
    return render_template('docs/getting-started/introduction.html')


# DOCS/STATISTICS/GRAPHICS/

@app.route('/docs/statistics/graphics/3d-plots/')
def docs_statistics_graphics_three_d_plots():
    return render_template('docs/statistics/graphics/3d-plots.html')

@app.route('/docs/statistics/graphics/bar-charts/')
def docs_statistics_graphics_bar_charts():
    return render_template('docs/statistics/graphics/bar-charts.html')

@app.route('/docs/statistics/graphics/bland-altman-plots/')
def docs_statistics_graphics_bland_altman_plots():
    return render_template('docs/statistics/graphics/bland-altman-plots.html')

@app.route('/docs/statistics/graphics/box-plots/')
def docs_statistics_graphics_box_plots():
    return render_template('docs/statistics/graphics/box-plots.html')

@app.route('/docs/statistics/graphics/circular-data-plots/')
def docs_statistics_graphics_circular_data_plots():
    return render_template('docs/statistics/graphics/circular-data-plots.html')

@app.route('/docs/statistics/graphics/contour-plots/')
def docs_statistics_graphics_contour_plots():
    return render_template('docs/statistics/graphics/contour-plots.html')

@app.route('/docs/statistics/graphics/curve-fitting/')
def docs_statistics_graphics_curve_fitting():
    return render_template('docs/statistics/graphics/curve-fitting.html')
	
@app.route('/docs/statistics/graphics/dendrograms/')
def docs_statistics_graphics_dendrograms():
    return render_template('docs/statistics/graphics/dendrograms.html')
	
@app.route('/docs/statistics/graphics/density-plots/')
def docs_statistics_graphics_density_plots():
    return render_template('docs/statistics/graphics/density-plots.html')
	
@app.route('/docs/statistics/graphics/dot-plots/')
def docs_statistics_graphics_dot_plots():
    return render_template('docs/statistics/graphics/dot-plots.html')
	
@app.route('/docs/statistics/graphics/error-bar-charts/')
def docs_statistics_graphics_error_bar_charts():
    return render_template('docs/statistics/graphics/error-bar-charts.html')
	
@app.route('/docs/statistics/graphics/forecasting/')
def docs_statistics_graphics_forecasting():
    return render_template('docs/statistics/graphics/forecasting.html')
	
@app.route('/docs/statistics/graphics/forest-plots/')
def docs_statistics_graphics_forest_plots():
    return render_template('docs/statistics/graphics/forest-plots.html')
	
@app.route('/docs/statistics/graphics/function-plots/')
def docs_statistics_graphics_function_plots():
    return render_template('docs/statistics/graphics/function-plots.html')
	
@app.route('/docs/statistics/graphics/heat-maps/')
def docs_statistics_graphics_heat_maps():
    return render_template('docs/statistics/graphics/heat-maps.html')
	
@app.route('/docs/statistics/graphics/histograms/')
def docs_statistics_graphics_histograms():
    return render_template('docs/statistics/graphics/histograms.html')
	
@app.route('/docs/statistics/graphics/kaplan-meier-curves/')
def docs_statistics_graphics_kaplan_meier_curves():
    return render_template('docs/statistics/graphics/kaplan-meier-curves.html')
	
@app.route('/docs/statistics/graphics/line-charts/')
def docs_statistics_graphics_line_charts():
    return render_template('docs/statistics/graphics/line-charts.html')
	
@app.route('/docs/statistics/graphics/mosaic-plots/')
def docs_statistics_graphics_mosaic_plots():
    return render_template('docs/statistics/graphics/mosaic-plots.html')
	
@app.route('/docs/statistics/graphics/percentile-plots/')
def docs_statistics_graphics_percentile_plots():
    return render_template('docs/statistics/graphics/percentile-plots.html')
	
@app.route('/docs/statistics/graphics/pie-charts/')
def docs_statistics_graphics_pie_charts():
    return render_template('docs/statistics/graphics/pie-charts.html')

@app.route('/docs/statistics/graphics/probability-plots/')
def docs_statistics_graphics_probability_plots():
    return render_template('docs/statistics/graphics/probability-plots.html')
	
@app.route('/docs/statistics/graphics/quality-control-charts/')
def docs_statistics_graphics_quality_control_charts():
    return render_template('docs/statistics/graphics/quality-control-charts.html')

@app.route('/docs/statistics/graphics/roc-curves/')
def docs_statistics_graphics_roc_curves():
    return render_template('docs/statistics/graphics/roc-curves.html')
	
@app.route('/docs/statistics/graphics/scatter-plots/')
def docs_statistics_graphics_scatter_plots():
    return render_template('docs/statistics/graphics/scatter_plots.html')
	
@app.route('/docs/statistics/graphics/stem-and-leaf-plots/')
def docs_statistics_graphics_stem_and_leaf_plots():
    return render_template('docs/statistics/graphics/stem-and-leaf-plots.html')
	
@app.route('/docs/statistics/graphics/surface-plots/')
def docs_statistics_graphics_surface_plots():
    return render_template('docs/statistics/graphics/surface-plots.html')
	
@app.route('/docs/statistics/graphics/time-series/')
def docs_statistics_graphics_time_series():
    return render_template('docs/statistics/graphics/time-series.html')
	
@app.route('/docs/statistics/graphics/violin-plots/')
def docs_statistics_graphics_violin_plots():
    return render_template('docs/statistics/graphics/violin-plots.html')

# DOCS/STATISTICS/PROCEDURES/

@app.route('/docs/statistics/procedures/analysis-of-variance/')
def docs_statistics_procedures_analysis_of_variance():
    return render_template('docs/statistics/procedures/analysis-of-variance.html')
	
@app.route('/docs/statistics/procedures/appraisal/')
def docs_statistics_procedures_appraisal():
    return render_template('docs/statistics/procedures/appraisal.html')
	
@app.route('/docs/statistics/procedures/cluster-analysis/')
def docs_statistics_procedures_cluster_analysis():
    return render_template('docs/statistics/procedures/cluster-analysis.html')
	
@app.route('/docs/statistics/procedures/correlation/')
def docs_statistics_procedures_correlation():
    return render_template('docs/statistics/procedures/correlation.html')
	
@app.route('/docs/statistics/procedures/curve-fitting/')
def docs_statistics_procedures_curve_fitting():
    return render_template('docs/statistics/procedures/curve-fitting.html')
	
@app.route('/docs/statistics/procedures/descriptive-statistics/')
def docs_statistics_procedures_descriptive_statistics():
    return render_template('docs/statistics/procedures/descriptive-statistics.html')
	
@app.route('/docs/statistics/procedures/design-of-experiments/')
def docs_statistics_procedures_design_of_experiments():
    return render_template('docs/statistics/procedures/design-of-experiments.html')
	
@app.route('/docs/statistics/procedures/diagnostic-tests/')
def docs_statistics_procedures_diagnostic_tests():
    return render_template('docs/statistics/procedures/diagnostic-tests.html')
	
@app.route('/docs/statistics/procedures/distribution-fitting/')
def docs_statistics_procedures_distribution_fitting():
    return render_template('docs/statistics/procedures/distribution-fitting.html')
	
@app.route('/docs/statistics/procedures/forecasting/')
def docs_statistics_procedures_forecasting():
    return render_template('docs/statistics/procedures/forecasting.html')
	
@app.route('/docs/statistics/procedures/group-sequential/')
def docs_statistics_procedures_group_sequential():
    return render_template('docs/statistics/procedures/group-sequential.html')
	
@app.route('/docs/statistics/procedures/item-analysis/')
def docs_statistics_procedures_item_analysis():
    return render_template('docs/statistics/procedures/item-analysis.html')
	
@app.route('/docs/statistics/procedures/meta-analysis/')
def docs_statistics_procedures_meta_analysis():
    return render_template('docs/statistics/procedures/meta-analysis.html')
	
@app.route('/docs/statistics/procedures/method-comparison/')
def docs_statistics_procedures_method_comparison():
    return render_template('docs/statistics/procedures/method-comparison.html')
	
@app.route('/docs/statistics/procedures/mixed-models/')
def docs_statistics_procedures_mixed_models():
    return render_template('docs/statistics/procedures/mixed-models.html')
	
@app.route('/docs/statistics/procedures/multivariate-analysis/')
def docs_statistics_procedures_multivariate_analysis():
    return render_template('docs/statistics/procedures/multivariate-analysis.html')
	
@app.route('/docs/statistics/procedures/nondetects-data/')
def docs_statistics_procedures_nondetects_data():
    return render_template('docs/statistics/procedures/nondetects-data.html')
	
@app.route('/docs/statistics/procedures/nonparametric/')
def docs_statistics_procedures_nonparametric():
    return render_template('docs/statistics/procedures/nonparametric.html')
	
@app.route('/docs/statistics/procedures/operations-research/')
def docs_statistics_procedures_operations_research():
    return render_template('docs/statistics/procedures/operations-research.html')
	
@app.route('/docs/statistics/procedures/proportions/')
def docs_statistics_procedures_proportions():
    return render_template('docs/statistics/procedures/proportions.html')
	
@app.route('/docs/statistics/procedures/quality-control/')
def docs_statistics_procedures_quality_control():
    return render_template('docs/statistics/procedures/quality-control.html')
	
@app.route('/docs/statistics/procedures/reference-intervals/')
def docs_statistics_procedures_reference_intervals():
    return render_template('docs/statistics/procedures/reference-intervals.html')
	
@app.route('/docs/statistics/procedures/regression/')
def docs_statistics_procedures_regression():
    return render_template('docs/statistics/procedures/regression.html')
	
@app.route('/docs/statistics/procedures/roc-curves/')
def docs_statistics_procedures_roc_curves():
    return render_template('docs/statistics/procedures/roc-curves.html')
	
@app.route('/docs/statistics/procedures/survey-data/')
def docs_statistics_procedures_survey_data():
    return render_template('docs/statistics/procedures/survey-data.html')
	
@app.route('/docs/statistics/procedures/survival-analysis-reliability/')
def docs_statistics_procedures_survival_analysis_reliability():
    return render_template('docs/statistics/procedures/survival-analysis-reliability.html')
	
@app.route('/docs/statistics/procedures/time-series/')
def docs_statistics_procedures_time_series():
    return render_template('docs/statistics/procedures/time-series.html')
	
@app.route('/docs/statistics/procedures/t-tests/')
def docs_statistics_procedures_t_tests():
    return render_template('docs/statistics/procedures/t-tests.html')
	
@app.route('/docs/statistics/procedures/two-way-tables/')
def docs_statistics_procedures_two_way_tables():
    return render_template('docs/statistics/procedures/two-way-tables.html')
		
# SAMPLE SIZE

@app.route('/docs/statistics/sample-size/bland-altman-method/')
def docs_statistics_sample_size_bland_altman_method():
    return render_template('docs/statistics/sample-size/bland-altman-method.html')
		
@app.route('/docs/statistics/sample-size/bridging-studies/')
def docs_statistics_sample_size_bridging_studies():
    return render_template('docs/statistics/sample-size/bridging-studies.html')
		
@app.route('/docs/statistics/sample-size/cluster-randomized-designs/')
def docs_statistics_sample_size_cluster_randomized_designs():
    return render_template('docs/statistics/sample-size/cluster-randomized-designs.html')
		
@app.route('/docs/statistics/sample-size/conditional-power/')
def docs_statistics_sample_size_conditional_power():
    return render_template('docs/statistics/sample-size/conditional-power.html')
		
@app.route('/docs/statistics/sample-size/confidence-intervals/')
def docs_statistics_sample_size_confidence_intervals():
    return render_template('docs/statistics/sample-size/confidence-intervals.html')
		
@app.route('/docs/statistics/sample-size/correlation/')
def docs_statistics_sample_size_correlation():
    return render_template('docs/statistics/sample-size/correlation.html')
		
@app.route('/docs/statistics/sample-size/cross-over-designs/')
def docs_statistics_sample_size_cross_over_designs():
    return render_template('docs/statistics/sample-size/cross-over-designs.html')
		
@app.route('/docs/statistics/sample-size/design-of-experiments/')
def docs_statistics_sample_size_design_of_experiments():
    return render_template('docs/statistics/sample-size/design-of-experiments.html')
		
@app.route('/docs/statistics/sample-size/equivalence/')
def docs_statistics_sample_size_equivalence():
    return render_template('docs/statistics/sample-size/equivalence.html')
		
@app.route('/docs/statistics/sample-size/exponential-distribution-parameter/')
def docs_statistics_sample_size_exponential_distribution_parameter():
    return render_template('docs/statistics/sample-size/exponential-distribution-parameter.html')
		
@app.route('/docs/statistics/sample-size/group-sequential-tests/')
def docs_statistics_sample_size_group_sequential_tests():
    return render_template('docs/statistics/sample-size/group-sequential-tests.html')
		
@app.route('/docs/statistics/sample-size/means-one/')
def docs_statistics_sample_size_means_one():
    return render_template('docs/statistics/sample-size/means-one.html')
		
@app.route('/docs/statistics/sample-size/means-two-independent/')
def docs_statistics_sample_size_means_two_independent():
    return render_template('docs/statistics/sample-size/means-two-independent.html')
		
@app.route('/docs/statistics/sample-size/means-two-correlated-or-paired/')
def docs_statistics_sample_size_means_two_correlated_or_paired():
    return render_template('docs/statistics/sample-size/means-two-correlated-or-paired.html')
		
@app.route('/docs/statistics/sample-size/means-2x2-cross-over-designs/')
def docs_statistics_sample_size_means_2x2_cross_over_designs():
    return render_template('docs/statistics/sample-size/means-2x2-cross-over-designs.html')
		
@app.route('/docs/statistics/sample-size/means-higher-order-cross-over-designs/')
def docs_statistics_sample_size_means_higher_order_cross_over_designs():
    return render_template('docs/statistics/sample-size/means-higher-order-cross-over-designs.html')
		
@app.route('/docs/statistics/sample-size/means-many/')
def docs_statistics_sample_size_means_many():
    return render_template('docs/statistics/sample-size/means-many.html')
		
@app.route('/docs/statistics/sample-size/mediation-effects/')
def docs_statistics_sample_size_mediation_effects():
    return render_template('docs/statistics/sample-size/mediation-effects.html')
		
@app.route('/docs/statistics/sample-size/michaelis-menten-parameters/')
def docs_statistics_sample_size_michaelis_menten_parameters():
    return render_template('docs/statistics/sample-size/michaelis-menten-parameters.html')
		
@app.route('/docs/statistics/sample-size/mixed-models/')
def docs_statistics_sample_size_mixed_models():
    return render_template('docs/statistics/sample-size/mixed-models.html')
		
@app.route('/docs/statistics/sample-size/non-inferiority/')
def docs_statistics_sample_size_non_inferiority():
    return render_template('docs/statistics/sample-size/non-inferiority.html')
		
@app.route('/docs/statistics/sample-size/nonparametric/')
def docs_statistics_sample_size_nonparametric():
    return render_template('docs/statistics/sample-size/nonparametric.html')
		
@app.route('/docs/statistics/sample-size/non-zero-and-non-unity-null-tests/')
def docs_statistics_sample_size_non_zero_and_non_unity_null_tests():
    return render_template('docs/statistics/sample-size/non-zero-and-non-unity-null-tests.html')
		
@app.route('/docs/statistics/sample-size/normality-tests/')
def docs_statistics_sample_size_normality_tests():
    return render_template('docs/statistics/sample-size/normality-tests.html')
		
@app.route('/docs/statistics/sample-size/pilot-studies/')
def docs_statistics_sample_size_pilot_studies():
    return render_template('docs/statistics/sample-size/pilot-studies.html')
		
@app.route('/docs/statistics/sample-size/proportions-one/')
def docs_statistics_sample_size_proportions_one():
    return render_template('docs/statistics/sample-size/proportions-one.html')
		
@app.route('/docs/statistics/sample-size/proportions-two-independent/')
def docs_statistics_sample_size_proportions_two_independent():
    return render_template('docs/statistics/sample-size/proportions-two-independent.html')
		
@app.route('/docs/statistics/sample-size/proportions-correlated-or-paired/')
def docs_statistics_sample_size_proportions_correlated_or_paired():
    return render_template('docs/statistics/sample-size/proportions-correlated-or-paired.html')
		
@app.route('/docs/statistics/sample-size/proportions-cross-over-designs/')
def docs_statistics_sample_size_proportions_cross_over_designs():
    return render_template('docs/statistics/sample-size/proportions_cross_over_designs.html')
		
@app.route('/docs/statistics/sample-size/proportions-sensitivity-and-specificity/')
def docs_statistics_sample_size_proportions_sensitivity_and_specificity():
    return render_template('docs/statistics/sample-size/proportions-sensitivity-and-specificity.html')
		
@app.route('/docs/statistics/sample-size/proportions-many/')
def docs_statistics_sample_size_proportions_many():
    return render_template('docs/statistics/sample-size/proportions-many.html')
		
@app.route('/docs/statistics/sample-size/quality-control/')
def docs_statistics_sample_size_quality_control():
    return render_template('docs/statistics/sample-size/quality-control.html')
		
@app.route('/docs/statistics/sample-size/rates-and-counts/')
def docs_statistics_sample_size_rates_and_counts():
    return render_template('docs/statistics/sample-size/rates-and-counts.html')
		
@app.route('/docs/statistics/sample-size/reference-intervals/')
def docs_statistics_sample_size_reference_intervals():
    return render_template('docs/statistics/sample-size/reference-intervals.html')
		
@app.route('/docs/statistics/sample-size/regression/')
def docs_statistics_sample_size_regression():
    return render_template('docs/statistics/sample-size/regression.html')
		
@app.route('/docs/statistics/sample-size/roc_curves/')
def docs_statistics_sample_size_roc_curves():
    return render_template('docs/statistics/sample-size/roc-curves.html')
		
@app.route('/docs/statistics/sample-size/superiority_by_a_margin_test/')
def docs_statistics_sample_size_superiority_by_a_margin_test():
    return render_template('docs/statistics/sample-size/superiority-by-a-margin-test.html')
		
@app.route('/docs/statistics/sample-size/survival-analysis/')
def docs_statistics_sample_size_survival_analysis():
    return render_template('docs/statistics/sample-size/survival-analysis.html')
		
@app.route('/docs/statistics/sample-size/tolerance-intervals/')
def docs_statistics_sample_size_tolerance_intervals():
    return render_template('docs/statistics/sample-size/tolerance-intervals.html')
		
@app.route('/docs/statistics/sample-size/two-part-models/')
def docs_statistics_sample_size_two_part_models():
    return render_template('docs/statistics/sample-size/two-part-models.html')
		
@app.route('/docs/statistics/sample-size/variances-and-standard-deviations/')
def docs_statistics_sample_size_variances_and_standard_deviations():
    return render_template('docs/statistics/sample-size/variances-and-standard-deviations.html')
		
@app.route('/docs/statistics/sample-size/bayesian-adjustment/')
def docs_statistics_sample_size_bayesian_adjustment():
    return render_template('docs/statistics/sample-size/bayesian-adjustment.html')		

# TOOLS/PROCEDURE

@app.route('/docs/statistics/tools/procedures/chi-square-effect-size-calculator/')
def docs_statistics_tools_procedures_chi_square_effect_size_calculator():
    return render_template('docs/statistics/tools/procedures/chi-square-effect-size-calculator.html')		

@app.route('/docs/statistics/tools/procedures/odds-ratio-and-proportions-calculator/')
def docs_statistics_tools_procedures_odds_ratio_and_proportions_calculator():
    return render_template('docs/statistics/tools/procedures/odds-ratio-and-proportions-calculator.html')		

@app.route('/docs/statistics/tools/procedures/probability-calculator/')
def docs_statistics_tools_procedures_probability_calculator():
    return render_template('docs/statistics/tools/procedures/probability-calculator.html')		

@app.route('/docs/statistics/tools/procedures/standard-deviation-calculator/')
def docs_statistics_tools_procedures_standard_deviation_calculator():
    return render_template('docs/statistics/tools/procedures/standard-deviation-calculator.html')		

@app.route('/docs/statistics/tools/procedures/survival-parameter-conversion-tool/')
def docs_statistics_tools_procedures_survival_parameter_conversion_tool():
    return render_template('docs/statistics/tools/procedures/survival-parameter-conversion-tool.html')		

# TOOLS/SAMPLE SIZE

@app.route('/docs/statistics/tools/sample-size/chi-square-effect-size-estimator/')
def docs_statistics_tools_sample_size_chi_square_effect_size_estimator():
    return render_template('docs/statistics/tools/sample-size/chi-square-effect-size-estimator.html')		

@app.route('/docs/statistics/tools/sample-size/data-simulator/')
def docs_statistics_tools_sample_size_data_simulator():
    return render_template('docs/statistics/tools/sample-size/data-simulator.html')		

@app.route('/docs/statistics/tools/sample-size/installation-validation-tool-for-installation-qualification/')
def docs_statistics_tools_sample_size_installation_validation_tool_for_installation_qualification():
    return render_template('docs/statistics/tools/sample-size/installation-validation-tool-for-installation-qualification.html')		

@app.route('/docs/statistics/tools/sample-size/multinomial-effect-size-estimator/')
def docs_statistics_tools_sample_size_multinomial_effect_size_estimator():
    return render_template('docs/statistics/tools/sample-size/multinomial-effect-size-estimator.html')		

@app.route('/docs/statistics/tools/sample-size/odds-ratio-to-proportions-converter/')
def docs_statistics_tools_sample_size_odds_ratio_to_proportions_converter():
    return render_template('docs/statistics/tools/sample-size/odds-ratio-to-proportions-converter.html')		

@app.route('/docs/statistics/tools/sample-size/probability-calculator/')
def docs_statistics_tools_sample_size_probability_calculator():
    return render_template('docs/statistics/tools/sample-size/probability-calculator.html')		

@app.route('/docs/statistics/tools/sample-size/procedure-validation-tool-for-operations-qualification/')
def docs_statistics_tools_sample_size_procedure_validation_tool_for_operations_qualification():
    return render_template('docs/statistics/tools/sample-size/procedure-validation-tool-for-operations-qualification.html')		

@app.route('/docs/statistics/tools/sample-size/standard-deviation-estimator/')
def docs_statistics_tools_sample_size_standard_deviation_estimator():
    return render_template('docs/statistics/tools/sample-size/standard-deviation-estimator.html')		

@app.route('/docs/statistics/tools/sample-size/standard-deviation-of-means-calculator/')
def docs_statistics_tools_sample_size_standard_deviation_of_means_calculator():
    return render_template('docs/statistics/tools/sample-size/standard-deviation-of-means-calculator.html')		

@app.route('/docs/statistics/tools/sample-size/survival-parameter-conversion-tool/')
def docs_statistics_tools_sample_size_survival_parameter_conversion_tool():
    return render_template('docs/statistics/tools/sample-size/survival-parameter-conversion-tool.html')		

# ABOUT

@app.route('/docs/about/overview/')
def docs_about_overview():
    return render_template('docs/about/overview.html')		

@app.route('/docs/about/team/')
def docs_about_team():
    return render_template('docs/about/team.html')		

@app.route('/docs/about/brand/')
def docs_about_brand():
    return render_template('docs/about/brand.html')		

@app.route('/docs/about/license/')
def docs_about_license():
    return render_template('docs/about/license.html')		

@app.route('/docs/about/translations/')
def docs_about_translations():
    return render_template('docs/about/translations.html')		

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
