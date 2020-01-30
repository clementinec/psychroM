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

def pointsarrow(chartobj,A,B):
    a = (A[0],gen_points_in_constant_relative_humidity(A[0],A[1],GetStandardAtmPressure(900)))
    b = (B[0],gen_points_in_constant_relative_humidity(B[0],B[1],GetStandardAtmPressure(900)))
    return chartobj._axes.annotate("",a,xytext=b,arrowprops=dict(arrowstyle='->'))

def update(tar,a,b):
    tar._handlers_annotations.append(pointsarrow(tar,a,b))

A = (31.06, 10)
B = (29.42, 50)
C = (20.47, 25)

def testchart(a=A,b=B,c=C):
	chart = PsychroChart(adju_style)
	ax = chart.plot()
	update(chart,A,B)
	update(chart,B,C)
	update(chart,C,A)
	ax.get_figure()
	chart._fig.savefig('newchart.png',dpi=150)

chart = PsychroChart(adju_style)
ax = chart.plot()
update(chart,A,B)
update(chart,B,C)
ax.get_figure()

