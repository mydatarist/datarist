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

@app.route('/statistics/curve-fitting/ratio-of-polynomials-search-many-variable/')
def statistics_curve_fitting_ratio_of_polynomials_search_many_variable():
    return render_template('statistics/curve-fitting/ratio-of-polynomials-search-many-variable.html')

@app.route('/statistics/curve-fitting/ratio-of-polynomials-search-one-variable/')
def statistics_curve_fitting_ratio_of_polynomials_search_one_variable():
    return render_template('statistics/curve-fitting/ratio-of-polynomials-search-one-variable.html')

@app.route('/statistics/curve-fitting/reference-intervals-age-specific/')
def statistics_curve_fitting_reference_intervals_age_specific():
    return render_template('statistics/curve-fitting/reference-intervals-age-specific.html')

@app.route('/statistics/curve-fitting/scatterplot-matrix-for-curve-fitting/')
def statistics_curve_fitting_scatterplot_matrix_for_curve_fitting():
    return render_template('statistics/curve-fitting/scatterplot-matrix-for-curve-fitting.html')

@app.route('/statistics/curve-fitting/sum-of-functions-models/')
def statistics_curve_fitting_sum_of_functions_models():
    return render_template('statistics/curve-fitting/sum-of-functions-models.html')

# /STATISTICS/DESCRIPTIVE-STATISTICS/

@app.route('/statistics/descriptive-statistics/')
def statistics_descriptive_statistics_index():
    return render_template('statistics/descriptive-statistics/index.html')

@app.route('/statistics/descriptive-statistics/area-under-curve/')
def statistics_descriptive_statistics_area_under_curve():
    return render_template('statistics/descriptive-statistics/area-under-curve.html')

@app.route('/statistics/descriptive-statistics/box-cox-transformation/')
def statistics_descriptive_statistics_box_cox_transformation():
    return render_template('statistics/descriptive-statistics/box-cox-transformation.html')

@app.route('/statistics/descriptive-statistics/circular-data-analysis/')
def statistics_descriptive_statistics_circular_data_analysis():
    return render_template('statistics/descriptive-statistics/circular-data-analysis.html')

@app.route('/statistics/descriptive-statistics/cluster-randomization/')
def statistics_descriptive_statistics_cluster_randomization():
    return render_template('statistics/descriptive-statistics/cluster-randomization.html')

@app.route('/statistics/descriptive-statistics/contingency-tables/')
def statistics_descriptive_statistics_contingency_tables():
    return render_template('statistics/descriptive-statistics/contingency-tables.html')

@app.route('/statistics/descriptive-statistics/data-screening/')
def statistics_descriptive_statistics_data_screening():
    return render_template('statistics/descriptive-statistics/data-screening.html')

@app.route('/statistics/descriptive-statistics/data-simulation/')
def statistics_descriptive_statistics_data_simulation():
    return render_template('statistics/descriptive-statistics/data-simulation.html')

@app.route('/statistics/descriptive-statistics/frequency-tables/')
def statistics_descriptive_statistics_frequency_tables():
    return render_template('statistics/descriptive-statistics/frequency-tables.html')

@app.route('/statistics/descriptive-statistics/grubbs-outlier-test/')
def statistics_descriptive_statistics_grubbs_outlier_test():
    return render_template('statistics/descriptive-statistics/grubbs-outlier-test.html')

@app.route('/statistics/descriptive-statistics/normality-tests/')
def statistics_descriptive_statistics_normality_tests():
    return render_template('statistics/descriptive-statistics/normality-tests.html')

@app.route('/statistics/descriptive-statistics/tolerance-intervals/')
def statistics_descriptive_statistics_tolerance_intervals():
    return render_template('statistics/descriptive-statistics/tolerance-intervals.html')

# /STATISTICS/DESIGN-OF-EXPERIMENTS/

@app.route('/statistics/design-of-experiments/')
def statistics_design_of_experiments_index():
    return render_template('statistics/design-of-experiments/index.html')

@app.route('/statistics/design-of-experiments/analysis-of-two-level-designs/')
def statistics_design_of_experiments_analysis_of_two_level_designs():
    return render_template('statistics/design-of-experiments/analysis-of-two-level-designs.html')

@app.route('/statistics/design-of-experiments/balanced-incomplete-block-designs/')
def statistics_design_of_experiments_balanced_incomplete_block_designs():
    return render_template('statistics/design-of-experiments/balanced-incomplete-block-designs.html')

@app.route('/statistics/design-of-experiments/d-optimal-designs/')
def statistics_design_of_experiments_d_optimal_designs():
    return render_template('statistics/design-of-experiments/d-optimal-designs.html')

@app.route('/statistics/design-of-experiments/design-generator/')
def statistics_design_of_experiments_design_generator():
    return render_template('statistics/design-of-experiments/design-generator.html')

@app.route('/statistics/design-of-experiments/fractional-factorial-designs/')
def statistics_design_of_experiments_fractional_factorial_designs():
    return render_template('statistics/design-of-experiments/fractional-factorial-designs.html')

@app.route('/statistics/design-of-experiments/latin-square-designs/')
def statistics_design_of_experiments_latin_square_designs():
    return render_template('statistics/design-of-experiments/latin-square-designs.html')

@app.route('/statistics/design-of-experiments/randomization-lists/')
def statistics_design_of_experiments_randomization_lists():
    return render_template('statistics/design-of-experiments/randomization-lists.html')

@app.route('/statistics/design-of-experiments/response-surface-designs/')
def statistics_design_of_experiments_response_surface_designs():
    return render_template('statistics/design-of-experiments/response-surface-designs.html')

@app.route('/statistics/design-of-experiments/response-surface-regression/')
def statistics_design_of_experiments_response_surface_regression():
    return render_template('statistics/design-of-experiments/response-surface-regression.html')

@app.route('/statistics/design-of-experiments/screening-designs/')
def statistics_design_of_experiments_screening_designs():
    return render_template('statistics/design-of-experiments/screening-designs.html')

@app.route('/statistics/design-of-experiments/taguchi-designs/')
def statistics_design_of_experiments_taguchi_designs():
    return render_template('statistics/design-of-experiments/taguchi-designs.html')

@app.route('/statistics/design-of-experiments/two-level-designs/')
def statistics_design_of_experiments_two_level_designs():
    return render_template('statistics/design-of-experiments/two-level-designs.html')

# /STATISTICS/DIAGNOSTIC-TESTS/

@app.route('/statistics/diagnostic-tests/')
def statistics_diagnostic_tests_index():
    return render_template('statistics/diagnostic-tests/index.html')

@app.route('/statistics/diagnostic-tests/binary-diagnostic-tests-clustered-samples/')
def statistics_diagnostic_tests_binary_diagnostic_tests_clustered_samples():
    return render_template('statistics/diagnostic-tests/binary-diagnostic-tests-clustered-samples.html')

@app.route('/statistics/diagnostic-tests/binary-diagnostic-tests-paired-samples/')
def statistics_diagnostic_tests_binary_diagnostic_tests_paired_samples():
    return render_template('statistics/diagnostic-tests/binary-diagnostic-tests-paired-samples.html')

@app.route('/statistics/diagnostic-tests/binary-diagnostic-tests-single-sample/')
def statistics_diagnostic_tests_binary_diagnostic_tests_single_sample():
    return render_template('statistics/diagnostic-tests/binary-diagnostic-tests-single-sample.html')

@app.route('/statistics/diagnostic-tests/binary-diagnostic-tests-two-independent-samples/')
def statistics_diagnostic_tests_binary_diagnostic_tests_two_independent_samples():
    return render_template('statistics/diagnostic-tests/binary-diagnostic-tests-two-independent-samples.html')

@app.route('/statistics/diagnostic-tests/comparing-two-roc-curves-independent-groups-design/')
def statistics_diagnostic_tests_comparing_two_roc_curves_independent_groups_design():
    return render_template('statistics/diagnostic-tests/comparing-two-roc-curves-independent-groups-design.html')

@app.route('/statistics/diagnostic-tests/comparing-two-roc-curves-paired-design/')
def statistics_diagnostic_tests_comparing_two_roc_curves_paired_design():
    return render_template('statistics/diagnostic-tests/comparing-two-roc-curves-paired-design.html')

@app.route('/statistics/diagnostic-tests/one-roc-curve-and-cutoff-analysis/')
def statistics_diagnostic_tests_one_roc_curve_and_cutoff_analysis():
    return render_template('statistics/diagnostic-tests/one-roc-curve-and-cutoff-analysis.html')

@app.route('/statistics/diagnostic-tests/roc-curves/')
def statistics_diagnostic_tests_roc_curves():
    return render_template('statistics/diagnostic-tests/roc-curves.html')

# /STATISTICS/DISTRIBUTION-FITTING/

@app.route('/statistics/distribution-fitting/')
def statistics_distribution_fitting_index():
    return render_template('statistics/distribution-fitting/index.html')

@app.route('/statistics/distribution-fitting/beta-distribution-fitting/')
def statistics_distribution_fitting_beta_distribution_fitting():
    return render_template('statistics/distribution-fitting/beta-distribution-fitting.html')

@app.route('/statistics/distribution-fitting/chi-square-probability-plots/')
def statistics_distribution_fitting_chi_square_probability_plots():
    return render_template('statistics/distribution-fitting/chi-square-probability-plots.html')

@app.route('/statistics/distribution-fitting/distribution-weibull-fitting/')
def statistics_distribution_fitting_distribution_weibull_fitting():
    return render_template('statistics/distribution-fitting/distribution-weibull-fitting.html')

@app.route('/statistics/distribution-fitting/exponential-probability-plots/')
def statistics_distribution_fitting_exponential_probability_plots():
    return render_template('statistics/distribution-fitting/exponential-probability-plots.html')

@app.route('/statistics/distribution-fitting/gamma-distribution-fitting/')
def statistics_distribution_fitting_gamma_distribution_fitting():
    return render_template('statistics/distribution-fitting/gamma-distribution-fitting.html')

@app.route('/statistics/distribution-fitting/gamma-probability-plots/')
def statistics_distribution_fitting_gamma_probability_plots():
    return render_template('statistics/distribution-fitting/gamma-probability-plots.html')

@app.route('/statistics/distribution-fitting/grubbs-outlier-test/')
def statistics_distribution_fitting_grubbs_outlier_test():
    return render_template('statistics/distribution-fitting/grubbs-outlier-test.html')

@app.route('/statistics/distribution-fitting/half-normal-probability-plots/')
def statistics_distribution_fitting_half_normal_probability_plots():
    return render_template('statistics/distribution-fitting/half-normal-probability-plots.html')

@app.route('/statistics/distribution-fitting/log-normal-probability-plots/')
def statistics_distribution_fitting_log_normal_probability_plots():
    return render_template('statistics/distribution-fitting/log-normal-probability-plots.html')

@app.route('/statistics/distribution-fitting/normal-probability-plots/')
def statistics_distribution_fitting_normal_probability_plots():
    return render_template('statistics/distribution-fitting/normal-probability-plots.html')

@app.route('/statistics/distribution-fitting/normality-tests/')
def statistics_distribution_fitting_normality_tests():
    return render_template('statistics/distribution-fitting/normality-tests.html')

@app.route('/statistics/distribution-fitting/probability-plot-comparison/')
def statistics_distribution_fitting_probability_plot_comparison():
    return render_template('statistics/distribution-fitting/probability-plot-comparison.html')

@app.route('/statistics/distribution-fitting/uniform-probability-plots/')
def statistics_distribution_fitting_uniform_probability_plots():
    return render_template('statistics/distribution-fitting/uniform-probability-plots.html')

@app.route('/statistics/distribution-fitting/weibull-probability-plots/')
def statistics_distribution_fitting_weibull_probability_plots():
    return render_template('statistics/distribution-fitting/weibull-probability-plots.html')

# /STATISTICS/FORECASTING/

@app.route('/statistics/forecasting/')
def statistics_forecasting_index():
    return render_template('statistics/forecasting/index.html')

@app.route('/statistics/forecasting/analysis-of-runs/')
def statistics_forecasting_analysis_of_runs():
    return render_template('statistics/forecasting/analysis-of-runs.html')

@app.route('/statistics/forecasting/arima/')
def statistics_forecasting_arima():
    return render_template('statistics/forecasting/arima.html')

@app.route('/statistics/forecasting/autocorrelations/')
def statistics_forecasting_autocorrelations():
    return render_template('statistics/forecasting/autocorrelations.html')

@app.route('/statistics/forecasting/box-jenkins-method/')
def statistics_forecasting_box_jenkins_method():
    return render_template('statistics/forecasting/box-jenkins-method.html')

@app.route('/statistics/forecasting/cross-correlations/')
def statistics_forecasting_cross_correlations():
    return render_template('statistics/forecasting/cross-correlations.html')

@app.route('/statistics/forecasting/decomposition-forecasting/')
def statistics_forecasting_decomposition_forecasting():
    return render_template('statistics/forecasting/decomposition-forecasting.html')

@app.route('/statistics/forecasting/exponential-smoothing/')
def statistics_forecasting_exponential_smoothing():
    return render_template('statistics/forecasting/exponential-smoothing.html')

@app.route('/statistics/forecasting/harmonic-regression/')
def statistics_forecasting_harmonic_regression():
    return render_template('statistics/forecasting/harmonic-regression.html')

@app.route('/statistics/forecasting/spectral-analysis/')
def statistics_forecasting_spectral_analysis():
    return render_template('statistics/forecasting/spectral-analysis.html')

@app.route('/statistics/forecasting/time-series-plots/')
def statistics_forecasting_time_series_plots():
    return render_template('statistics/forecasting/time-series-plots.html')

# /STATISTICS/GROUP-SEQUENTIAL/

@app.route('/statistics/group-sequential/')
def statistics_group_sequential_index():
    return render_template('statistics/group-sequential/index.html')

@app.route('/statistics/group-sequential/one-hazard-rate/')
def statistics_group_sequential_one_hazard_rate():
    return render_template('statistics/group-sequential/one-hazard-rate.html')

@app.route('/statistics/group-sequential/one-mean/')
def statistics_group_sequential_one_mean():
    return render_template('statistics/group-sequential/one-mean.html')

@app.route('/statistics/group-sequential/one-poisson-rate/')
def statistics_group_sequential_one_poisson_rate():
    return render_template('statistics/group-sequential/one-poisson-rate.html')

@app.route('/statistics/group-sequential/one-proportion/')
def statistics_group_sequential_one_proportion():
    return render_template('statistics/group-sequential/one-proportion.html')

@app.route('/statistics/group-sequential/two-hazard-rates/')
def statistics_group_sequential_two_hazard_rates():
    return render_template('statistics/group-sequential/two-hazard-rates.html')

@app.route('/statistics/group-sequential/two-means/')
def statistics_group_sequential_two_means():
    return render_template('statistics/group-sequential/two-means.html')

@app.route('/statistics/group-sequential/two-poisson-rates/')
def statistics_group_sequential_two_poisson_rates():
    return render_template('statistics/group-sequential/two-poisson-rates.html')

@app.route('/statistics/group-sequential/two-proportions/')
def statistics_group_sequential_two_proportions():
    return render_template('statistics/group-sequential/two-proportions.html')

# /STATISTICS/ITEM-ANALYSIS/

@app.route('/statistics/item-analysis/')
def statistics_item_analysis_index():
    return render_template('statistics/item-analysis/index.html')

@app.route('/statistics/item-analysis/item-response-analysis/')
def statistics_item_analysis_item_response_analysis():
    return render_template('statistics/item-analysis/item-response-analysis.html')

# /STATISTICS/META-ANALYSIS/

@app.route('/statistics/meta-analysis/')
def statistics_meta_analysis_index():
    return render_template('statistics/meta-analysis/index.html')

@app.route('/statistics/meta-analysis/forest-plots/')
def statistics_meta_analysis_forest_plots():
    return render_template('statistics/meta-analysis/forest-plots.html')

@app.route('/statistics/meta-analysis/meta-analysis-of-correlated-proportions/')
def statistics_meta_analysis_meta_analysis_of_correlated_proportions():
    return render_template('statistics/meta-analysis/meta-analysis-of-correlated-proportions.html')

@app.route('/statistics/meta-analysis/')
def statistics_meta_analysis_index():
    return render_template('statistics/meta-analysis/index.html')

@app.route('/statistics/meta-analysis/')
def statistics_meta_analysis_index():
    return render_template('statistics/meta-analysis/index.html')

@app.route('/statistics/meta-analysis/')
def statistics_meta_analysis_index():
    return render_template('statistics/meta-analysis/index.html')

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
