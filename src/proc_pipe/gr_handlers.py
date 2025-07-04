import gradio as gr



# filter FMEA by cause or component

def filter_fmea_by_cause (fmea_df, cause):
    return fmea_df[fmea_df['Cause'] == cause]

def filter_fmea_by_component (fmea_df, component):
    return fmea_df[fmea_df['Component'] == component]

def filter_fmea_by_sub_component (fmea_df, sub_component):
    return fmea_df[fmea_df['Sub-Component'] == sub_component]

def filter_fmea_by_failure_mode (fmea_df, failure_mode):
    return fmea_df[fmea_df['Failure Mode'] == failure_mode]

def filter_fmea_by_failure_mode_and_component (fmea_df, failure_mode, component):
    return fmea_df[fmea_df['Failure Mode'] == failure_mode & fmea_df['Component'] == component]

def filter_fmea_by_failure_mode_and_sub_component (fmea_df, failure_mode, sub_component):
    return fmea_df[fmea_df['Failure Mode'] == failure_mode & fmea_df['Sub-Component'] == sub_component]

def filter_fmea_by_failure_mode_and_cause (fmea_df, failure_mode, cause):
    return fmea_df[fmea_df['Failure Mode'] == failure_mode & fmea_df['Cause'] == cause]

def filter_fmea_for_maintenance_event (fmea_df, maintenance_event):
    # get failure mode, component from mainteance event.
    # OR get failure mode, component from anomaly.
    ret_df = fmea_df[fmea_df['Failure Mode'] == maintenance_event['Failure Mode'] | fmea_df['Component'] == maintenance_event['Component']]
    return ret_df

def filter_fmea_for_anomaly (fmea_df, anomaly):
    # get failure mode, component from anomaly.
    ret_df = fmea_df[fmea_df['Failure Mode'] == anomaly['Failure Mode'] & fmea_df['Component'] == anomaly['Component']]
    return ret_df
## AGENT CALLS

# fmea agent

# data-mining agent

# general agent

# components_agent
