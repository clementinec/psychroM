from chart import gen_points_in_constant_relative_humidity,GetStandardAtmPressure
from cp import PsychroChart, load_config


def custstyle(figsize=[6,6],fontsize=6):
    custom_style = {
    "figure": {
        "figsize": figsize,
        "base_fontsize": fontsize,
        "title": "",
#         "x_label": None,
#         "y_label": None,
        "partial_axis": False,
        "x_axis": {"color": [0.0, 0.0, 0.0], "linewidth": 1.5, "linestyle": "-"},
        "x_axis_labels": {"color": [0.0, 0.0, 0.0], "fontsize": 6},
        "x_axis_ticks": {"direction": "out", "color": [0.0, 0.0, 0.0]},
        "y_axis": {"color": [0.0, 0.0, 0.0], "linewidth": 1.5, "linestyle": "-"},
        "y_axis_labels": {"color": [0.0, 0.0, 0.0], "fontsize": 6},
        "y_axis_ticks": {"direction": "out", "color": [0.0, 0.0, 0.0]},
    },
    "limits": {
        "range_temp_c": [10, 50],
        "range_humidity_g_kg": [0, 25],
        "altitude_m": 900,
        "step_temp": .5
    },
    "saturation": {"color": [0, 0, 0], "linewidth": 1}, #Saturation line
    "constant_rh": {"color": [0.0, 0.498, 1.0, .7], "linewidth": 2.5,
                    "linestyle": ":"},
    "chart_params": {
        "with_constant_rh": True,
        "constant_rh_curves": [10, 25, 50, 75],
        "constant_rh_labels": [25, 50, 75],
        
        "range_vol_m3_kg": [0.9, 1.],
        "constant_v_labels": [0.9, 0.94, 0.98],
        "with_constant_v": False,
        "with_constant_wet_temp": False,
        "with_constant_dry_temp": False,
        "with_constant_humidity": False,
        
        "with_constant_h": False,
        "with_constant_wet_temp": False,
        "with_zones": False
    }
}
    return custom_style


def plotarrow(chartobj,pointa,pointb,altitude=900):
	a = pointa[0],gen_points_in_constant_relative_humidity(pointa[0],pointa[1],GetStandardAtmPressure(altitude))
	b = pointb[0],gen_points_in_constant_relative_humidity(pointb[0],pointb[1],GetStandardAtmPressure(altitude))
	return chartobj._axes.annotate("",a,xytext=b,arrowprops=dict(arrowstyle='->'))


adju_style = {
    "figure": {
        "figsize": [5, 5],
        "base_fontsize": 8,
        "title": "",
#         "x_label": None,
#         "y_label": None,
        "partial_axis": False,
        "x_axis": {"color": [0.0, 0.0, 0.0], "linewidth": 1.5, "linestyle": "-"},
        "x_axis_labels": {"color": [0.0, 0.0, 0.0], "fontsize": 6},
        "x_axis_ticks": {"direction": "out", "color": [0.0, 0.0, 0.0]},
        "y_axis": {"color": [0.0, 0.0, 0.0], "linewidth": 1.5, "linestyle": "-"},
        "y_axis_labels": {"color": [0.0, 0.0, 0.0], "fontsize": 6},
        "y_axis_ticks": {"direction": "out", "color": [0.0, 0.0, 0.0]},
    },
    "limits": {
        "range_temp_c": [10, 50],
        "range_humidity_g_kg": [0, 25],
        "altitude_m": 900,
        "step_temp": .5
    },
    "saturation": {"color": [0, 0, 0], "linewidth": 1}, #Saturation line
    "constant_rh": {"color": [0.0, 0.498, 1.0, .7], "linewidth": 2.5,
                    "linestyle": ":"},
    "constant_h": {"color":[0,0.1,0.2,0.35], "linewidth": 1.5, "linestyle":":"},
    "chart_params": {
        "with_constant_rh": True,
        "constant_rh_curves": [10, 25, 50, 75],
        "constant_rh_labels": [10, 25, 50, 75],
        
        "range_vol_m3_kg": [0.9, 1.],
        "constant_v_labels": [0.9, 0.94, 0.98],
        "with_constant_v": False,
        "with_constant_wet_temp": False,
        "with_constant_dry_temp": False,
        "with_constant_humidity": False,
        
        "with_constant_h": True,
        "with_constant_wet_temp": False,
        "with_zones": False
    }
}
#Define the three default points. Can be further adapted if given specific points
A = (31.06, 10.)
B = (29.42, 50.)
C = (20.47, 25.)

def construct(a = A,b = B,c = C):
    pts = {
        'exterior': {
            'label': 'Exterior',
            'style': {'color': [0.855, 0.004, 0.278, 0.8],'marker': 'X', 'markersize': 15},
            'xy': (a[0],a[1])
            },
        'exterior_estimated': {
            'label': 'Estimated (Weather service)',
            'style': {'color': [0.573, 0.106, 0.318, 0.5],'marker': 'x', 'markersize': 10},
            'xy': (b[0],b[1])
            },
        'interior': {
            'label': 'Interior',
            'style': {'color': [0.592, 0.745, 0.051, 0.9],'marker': 'o', 'markersize': 30},
            'xy': (c[0], c[1])
            }
        }

    # points = {'exterior': {'label': 'Exterior',
    #                    'style': {'color': [0.855, 0.004, 0.278, 0.8],
    #                              'marker': 'X', 'markersize': 15},
    #                    'xy': (31.06, 32.9)},
    #       'exterior_estimated': {
    #           'label': 'Estimated (Weather service)',
    #           'style': {'color': [0.573, 0.106, 0.318, 0.5],
    #                     'marker': 'x', 'markersize': 10},
    #           'xy': (36.7, 25.0)},
    #       'interior': {'label': 'Interior',
    #                    'style': {'color': [0.592, 0.745, 0.051, 0.9],
    #                              'marker': 'o', 'markersize': 30},
    #                    'xy': (29.42, 52.34)}}
    return pts

def pointsarrow(chartobj,A,B):
    a = (A[0],gen_points_in_constant_relative_humidity(A[0],A[1],GetStandardAtmPressure(900)))
    b = (B[0],gen_points_in_constant_relative_humidity(B[0],B[1],GetStandardAtmPressure(900)))
    return chartobj._axes.annotate("",a,xytext=b,arrowprops=dict(arrowstyle='->'))

def update(tar,a,b):
    tar._handlers_annotations.append(pointsarrow(tar,a,b))



def testchart3(a=A,b=B,c=C):
    chart = PsychroChart(adju_style)
    ax = chart.plot()
    update(chart,a,b)
    update(chart,b,c)
    update(chart,c,a)
    points=construct(a,b,c)
    chart.plot_points_dbt_rh(points)
#     ax.get_figure()
    chart._fig.savefig('newchart.png',dpi=150)

# chart = PsychroChart(adju_style)
# ax = chart.plot()
# update(chart,A,B)
# update(chart,B,C)
# ax.get_figure()

