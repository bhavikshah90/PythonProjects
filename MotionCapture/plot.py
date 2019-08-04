from motion_capture import df

#import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show

#create figure object
f = figure(x_axis_type='datetime',height=100,width=500, sizing_mode='scale_width', title="Capture Motion Graph")
f.yaxis.minor_tick_line_color = None
f.ygrid[0].ticker.desired_num_ticks = 1

q = f.quad(left=df["Start"], right=df["End"],bottom=0,top=1,color="green")

#prepare output file
output_file("MotionGraph.html")
show(f)